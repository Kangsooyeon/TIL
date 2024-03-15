import requests
import pprint #예쁘게 출력하기

#서울의 위도
lat = 37.56

#서울의 경도
lon = 126.97

api_key = '7f8781b0f082220f76a6ac78bed8edec'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
data = requests.get(url).json()
pprint.pprint(data['weather'][0]['description'])

# 추가 공부 과제 (차이점?)
# data['weather']
# data.get('weather')