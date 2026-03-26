import sys
import os

# Add the parent directory to the Python path to import weex_auth
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from weex_auth import make_request

def get_account_balance():
    print("Fetching WEEX Account Balance...")
    try:
        # Private endpoint requires WEEX_API_KEY, WEEX_SECRET_KEY, WEEX_PASSPHRASE
        # Example endpoint for getting spot assets. Please adjust according to actual docs.
        data = make_request("GET", "/api/v3/spot/account/assets")
        
        print("Success! Account Assets:")
        for asset in data:
            print(f"  Coin: {asset.get('coin')}, Available: {asset.get('available')}, Frozen: {asset.get('frozen')}")
            
    except RuntimeError as e:
        print(f"API Error: {e}")
        print("Did you forget to set WEEX_API_KEY, WEEX_SECRET_KEY, and WEEX_PASSPHRASE environment variables?")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_account_balance()
