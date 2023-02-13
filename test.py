import requests
import json

addres = input("Введите Ваш адрес:\n>> ")
url = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={addres}&format=json"
response = requests.get(url).json()

if response:
    index = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
else:
    print("Неверный запрос! Исправьте запрос и повторите попытку")