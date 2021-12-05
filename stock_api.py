import requests

link = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":"msft","datatype":"json","output_size":"compact"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "your_rapidapi_key_here"
    }

got = requests.request("GET", link, headers=headers, params=querystring)

print(got.text)
