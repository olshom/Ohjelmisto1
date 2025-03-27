import requests

#https://api.chucknorris.io/jokes/random
pyyntö = ""
try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus['value'])

except requests.exceptions.RequestException as e:
    print('something went wrong')