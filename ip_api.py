import json
import requests
inp = input("enter the ip : " )
url=f"http://ip-api.com/json/{inp}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
response = requests.request("GET", url )
parsed = json.loads(response.text)
print(json.dumps(parsed , indent=40))

