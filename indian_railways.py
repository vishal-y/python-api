import requests

url = "https://indianrailways.p.rapidapi.com/findstations.php"

querystring = {"station":"mumbai"}

headers = {
    'x-rapidapi-host': "indianrailways.p.rapidapi.com",
    'x-rapidapi-key': "171b434de4msh9ce09d4c3be544fp1ff4b1jsnb8ae3c020020"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


link = "https://indianrailways.p.rapidapi.com/index.php"

pnr = int(input("enter the pnr number : "))
query = {"pnr":pnr}

header = {
    'x-rapidapi-host': "indianrailways.p.rapidapi.com",
    'x-rapidapi-key': "171b434de4msh9ce09d4c3be544fp1ff4b1jsnb8ae3c020020"
    }

got= requests.request("GET", link, headers=header, params=query)


print(response.text)

print(got.text)
