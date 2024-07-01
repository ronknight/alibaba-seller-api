import os
import sys
import requests
import hashlib
import time
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve variables from environment
app_key = os.getenv('APP_KEY')
app_secret = os.getenv('APP_SECRET')
session_key = os.getenv('SESSION_KEY')

# Define the log directory
LOG_DIR = 'api_logs/'  # Directory to store log files
os.makedirs(LOG_DIR, exist_ok=True)  # Create directory if it doesn't exist

# API endpoint
url = 'https://eco.taobao.com/router/rest'

# Check if necessary command-line arguments are provided
if len(sys.argv) < 2:
    print("Usage: python script.py <e_trade_id>")
    sys.exit(1)

e_trade_id = sys.argv[1]  # Get e_trade_id from command-line argument

# Parameters for the API call
params = {
    "app_key": app_key,
    "format": "json",
    "method": "alibaba.seller.order.get",
    "partner_id": "apidoc",
    "session": session_key,
    "sign_method": "md5",
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    "v": "2.0",
    "e_trade_id": e_trade_id,
    "data_select": "draft_role",  # Adjust based on your requirements
    "language": "en_US",  # Adjust based on your requirements
}

# Calculate sign
def calculate_sign(params, secret):
    sorted_params = sorted(params.items())
    sign_string = secret + ''.join([f'{k}{v}' for k, v in sorted_params]) + secret
    return hashlib.md5(sign_string.encode('utf-8')).hexdigest().upper()

# Add sign to parameters
params["sign"] = calculate_sign(params, app_secret)

# Remove sensitive information for logging
def remove_sensitive_info(params):
    safe_params = params.copy()
    safe_params.pop("app_key", None)
    safe_params.pop("session", None)
    safe_params.pop("sign", None)
    return safe_params

# Log file names
log_file = f"{LOG_DIR}seller_order_get_logs_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json"
error_log_file = f"{LOG_DIR}seller_order_get_error_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json"

try:
    # Make the API request
    seller_order_get_request = requests.get(url, params=params)
    seller_order_get_response = seller_order_get_request.json()

    # Log API request
    with open(log_file, "w") as f:
        json.dump({
            "request_params": remove_sensitive_info(params),
            "response": seller_order_get_response,
        }, f, indent=4)

    # Example of handling the response data
    if seller_order_get_response.get("error_response"):
        with open(error_log_file, "w") as f:
            json.dump({
                "request_params": remove_sensitive_info(params),
                "response": seller_order_get_response,
            }, f, indent=4)
        print(f"Error: {seller_order_get_response['error_response']['msg']}")
    else:
        print("API call successful.")
        # Process your response data as needed

except requests.exceptions.RequestException as e:
    with open(error_log_file, "w") as f:
        json.dump({
            "request_params": remove_sensitive_info(params),
            "error_message": str(e),
        }, f, indent=4)
    print(f"Request failed: {e}")
