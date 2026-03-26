import sys
import os

# Add the parent directory to the Python path to import weex_auth
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from weex_auth import make_request

def get_server_time():
    print("Fetching WEEX Server Time...")
    try:
        # Public endpoint does not strictly require auth, but weex_auth handles it smoothly.
        data = make_request("GET", "/api/v3/spot/public/time")
        print(f"Server Time: {data}")
    except RuntimeError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_server_time()
