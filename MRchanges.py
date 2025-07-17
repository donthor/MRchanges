# This script updates the name and management interface of Meraki devices with specified serial numbers.

import requests
import json
import ipaddress

API_TOKEN = ''  # Replace with your actual API token

SERIALS = [""]  #List of device serial numbers to update (separated by commas)

STORE_NUMBER = ""
ADDRESS = ""

START_IP = ipaddress.IPv4Address("")
GATEWAY = format(START_IP)
SUBNET_MASK = ""
DNS1 = ""
DNS2 = ""

count = 1

for SERIAL in SERIALS:

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Cisco-Meraki-API-Key': API_TOKEN
    }

    url = f"https://api.meraki.com/api/v1/devices/{SERIAL}"
 
 #Name and Address - Name field is custom for customer
    payload = json.dumps({
    "name": STORE_NUMBER + "-" + "AP" + str(count).zfill(2),
    "address": f"{ADDRESS}"
    })
 
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)
    
#AP variables (found under LAN IP in the Dashboard)
    payload = json.dumps({
    "wan1": {
    "usingStaticIp": "true",
    "staticIp": format(START_IP + count),
    "staticGatewayIp": str(GATEWAY),
    "staticSubnetMask": SUBNET_MASK,
    "staticDns": [
      DNS1,
      DNS2
    ]}
  })
 
    url = f"https://api.meraki.com/api/v1/devices/{SERIAL}/managementInterface"

    response = requests.request("PUT", url, headers=headers, data=payload)

    count += 1
    print(response.text)