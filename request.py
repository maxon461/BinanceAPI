import requests
import hashlib
import hmac
import time
from datetime import datetime, timedelta

def get_binance_c2c_order_history(api_key, secret_key):
    base_url = 'https://api.binance.com'
    endpoint = '/sapi/v1/c2c/orderMatch/listUserOrderHistory'
    print(time.time())
    # Calculate start timestamp (20 days ago) in milliseconds
    start_timestamp = int((time.time() - 20 * 24 * 3600) * 1000)

    # Generate timestamp in milliseconds
    timestamp = int(time.time() * 1000)

    # Create the query string
    query_string = f"timestamp={timestamp}&startTime={start_timestamp}"

    # Create the signature
    signature = hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    # Create request URL
    url = f"{base_url}{endpoint}?{query_string}&signature={signature}"

    # Set request headers
    headers = {
        'X-MBX-APIKEY': api_key
    }

    # Send GET request to Binance API
    response = requests.get(url, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
