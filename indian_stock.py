import requests

url = "https://indianstockexchange.p.rapidapi.com/index.php"

querystring = {"id":"500570"}

headers = {
    'x-rapidapi-host': "indianstockexchange.p.rapidapi.com",
    'x-rapidapi-key': "171b434de4msh9ce09d4c3be544fp1ff4b1jsnb8ae3c020020"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)