import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
inp = input('enter your text : ')
query = f"q={inp}&target=en&source=es"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "your_rapidapi_key_here"
}
response = requests.request("POST", url, data=query, headers=headers)
print(response.text)

