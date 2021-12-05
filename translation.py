import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
inp = input('enter your text : ')
query = f"q={inp}&target=en&source=es"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "171b434de4msh9ce09d4c3be544fp1ff4b1jsnb8ae3c020020"
}
response = requests.request("POST", url, data=query, headers=headers)
print(response.text)

