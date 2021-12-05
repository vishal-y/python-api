import requests

url = "https://indianrailways.p.rapidapi.com/findstations.php"

querystring = {"station":"mumbai"}

headers = {
    'x-rapidapi-host': "indianrailways.p.rapidapi.com",
    'x-rapidapi-key': "your_rapidapi_key_here"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


link = "https://indianrailways.p.rapidapi.com/index.php"

pnr = int(input("enter the pnr number : "))
query = {"pnr":pnr}

header = {
    'x-rapidapi-host': "indianrailways.p.rapidapi.com",
    'x-rapidapi-key': "your_rapidapi_key_here"
    }

got= requests.request("GET", link, headers=header, params=query)


print(response.text)

print(got.text)
