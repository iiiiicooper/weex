import hashlib
import hmac
import json
import os
import time
from base64 import b64encode
from urllib.parse import urlencode

import requests

BASE_URL_SPOT = "https://api-spot.weex.com"
BASE_URL_CONTRACT = "https://api-contract.weex.com"


def _timestamp() -> str:
    """Returns the current timestamp in milliseconds."""
    return str(int(time.time() * 1000))


def _sign(secret: str, timestamp: str, method: str, path: str, body: str) -> str:
    """Generates the WEEX API signature using HMAC SHA256."""
    pre_sign = timestamp + method.upper() + path + body
    mac = hmac.new(secret.encode(), pre_sign.encode(), hashlib.sha256)
    return b64encode(mac.digest()).decode()


def make_request(
    method: str,
    path: str,
    params: dict | None = None,
    body: dict | None = None,
    is_contract: bool = False,
) -> list | dict:
    """
    Make an authenticated WEEX API V3 request.

    Args:
        method: "GET" or "POST"
        path:   API path, e.g. "/api/v3/spot/public/time"
        params: Query parameters (GET only)
        body:   Request body as dict (POST only)
        is_contract: True if querying contract endpoints

    Returns:
        Parsed JSON response (usually `data` field or full response if `data` is missing).

    Raises:
        RuntimeError: If the API returns an error code.
        requests.HTTPError: If the HTTP request itself fails.
    """
    method = method.upper()
    api_key = os.environ.get("WEEX_API_KEY", "")
    secret = os.environ.get("WEEX_SECRET_KEY", "")
    passphrase = os.environ.get("WEEX_PASSPHRASE", "")

    base_url = BASE_URL_CONTRACT if is_contract else BASE_URL_SPOT

    query_string = ""
    if params:
        query_string = "?" + urlencode(params)
    full_path = path + query_string

    body_str = ""
    if body and method == "POST":
        body_str = json.dumps(body)

    timestamp = _timestamp()

    # Headers for WEEX API
    headers = {
        "ACCESS-KEY": api_key,
        "ACCESS-SIGN": _sign(secret, timestamp, method, full_path, body_str),
        "ACCESS-TIMESTAMP": timestamp,
        "ACCESS-PASSPHRASE": passphrase,
    }

    if method == "POST":
        headers["Content-Type"] = "application/json"

    url = base_url + full_path
    response = requests.request(
        method,
        url,
        headers=headers,
        data=body_str if method == "POST" else None,
        timeout=10,
    )
    response.raise_for_status()

    result = response.json()
    code = result.get("code", "0")
    
    # WEEX typical error codes are negative, e.g. -1121. "0" or "200" usually means success.
    if str(code) not in ["0", "00000", "200"] and int(code) != 0: 
        raise RuntimeError(
            f"WEEX API error {code}: {result.get('msg', 'unknown error')}\n"
            f"Full response: {json.dumps(result, indent=2)}"
        )

    return result.get("data", result)


if __name__ == "__main__":
    # Smoke test: Check server time (Public endpoint)
    print("Testing WEEX API connection...")
    try:
        data = make_request("GET", "/api/v3/spot/public/time")
        print("Success! Server time data:", data)
    except Exception as e:
        import sys
        print(f"Request failed: {e}", file=sys.stderr)
        sys.exit(1)
