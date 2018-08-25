#!/user/bin/env python3 

import requests

url = "https://api.uptimerobot.com/v2/getMonitors"

payload = "api_key=m780055887-550dfc26f6ee216a371cc446&format=json"
headers = {
         'content-type': "application/x-www-form-urlencoded",
         'cache-control': "no-cache"
         }

response = requests.request("POST", url, data=payload, headers=headers)

site_json = response.json()
print("Site Status: ", site_json["stat"])



