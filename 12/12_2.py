import requests

#
city = input('What is your city? ')
API_KEY = 'bbb62d7f22db6325a33a57ed2f3ab5e6'
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={API_KEY}"
try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus["weather"][0]["main"],
              json_vastaus["main"]["temp"], '°C')

except requests.exceptions.RequestException as e:
    print('something went wrong')