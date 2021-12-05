import requests

link = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":"msft","datatype":"json","output_size":"compact"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "171b434de4msh9ce09d4c3be544fp1ff4b1jsnb8ae3c020020"
    }

got = requests.request("GET", link, headers=headers, params=querystring)

print(got.text)
