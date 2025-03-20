import requests

ip = '185.58.129.140'
url = 'https://ipinfo.io/161.185.160.93/geo' + ip +"/geo"

response = requests.get(url)

# if response.status_code == 200:
#     print(response.json())
# else:
#     print('Соединение с сервером провалено')

r = response.json()

print(f"Страна {r['country']}\nГород: {r['city']}\nlot,lon: {r['loc']}\nОрганизация: {r['org']}")
