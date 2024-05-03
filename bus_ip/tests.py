import requests

url = "https://findbus.pythonanywhere.com/bus_ip/user/login/"

payload = {}
headers = {
  'Authorization': 'token YWRtaW46MTIz',
  'Cookie': 'csrftoken=p4qk4afWK23zfgT1OQjKjeA4v6IOYHVszdTFLHkwSY1921KrvvK1rbTjzRE23Spd'
}
data = {
    "username":'admin',
    "password":123
}

response = requests.post(url=url, params=data)

print(response.json())