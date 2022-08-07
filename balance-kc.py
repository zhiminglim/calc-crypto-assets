import time
import hmac
import hashlib
import base64
import requests
import json
import os
import datetime

# Import env variables
API_KEY = os.environ.get('API_KEY')
API_SECRET = os.environ.get('API_SECRET')
API_PASSPHRASE = os.environ.get('API_PASSPHRASE')
BASEURL = os.environ.get('BASEURL')

# Initialize global epoch timestamp (current) in ms
now = int(time.time() * 1000)
print(f"current datetime: {datetime.datetime.fromtimestamp(now/1000).strftime('%Y-%m-%d %H:%M:%S')}")

###############################
### Define helper functions ###
###############################
def get_signed(s):
  return base64.b64encode(hmac.new(API_SECRET.encode('utf-8'), s.encode('utf-8'), hashlib.sha256).digest())

def get_headers(s):
  headers = {
    "KC-API-SIGN": get_signed(s),
    "KC-API-TIMESTAMP": str(now),
    "KC-API-KEY": API_KEY,
    "KC-API-PASSPHRASE": get_signed(API_PASSPHRASE),
    "KC-API-KEY-VERSION": "2"
  }
  return headers

def getResource(api):
  str_to_sign = str(now) + 'GET' + api
  h = get_headers(str_to_sign)
  response = requests.request('get', BASEURL+api, headers=h)
  print(f"response code={response.status_code} when hitting {api}")
  # Uncomment the below line to view output json data from the API request
  # print(json.dumps(response.json(), sort_keys=True, indent=2))
  return response.json().get('data')


#####################################
### Define a main function to run ###
#####################################
def main():
  print("\nInitializing main function...")
  price_dict = getResource(api='/api/v1/prices')
  account_list = getResource(api='/api/v1/accounts')
  
  # Initialize empty var
  total_asset_values = 0

  print("\nComputing sum of all asset values...")
  for account in account_list:
    # Check only assets with existing balance
    if (float(account.get('balance')) > 0):
      print(f"holding of {account.get('currency')} has balance of {account.get('balance')} with market price ${price_dict.get(account.get('currency'))}")
      asset_value = float(account.get('balance')) * float(price_dict.get(account.get('currency')))
      total_asset_values += asset_value

  print(f"\ntotal asset values (USD) = ${total_asset_values}")


#############################
### Execute main function ###
#############################
main()