import requests

url = "https://indianstockexchange.p.rapidapi.com/index.php"

querystring = {"id":"500570"}

headers = {
    'x-rapidapi-host': "indianstockexchange.p.rapidapi.com",
    'x-rapidapi-key': "your_rapidapi_key_here"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
