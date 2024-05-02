import requests

url = "http://127.0.0.1:8000/bus_ip/user/logout/"

payload = {}
headers = {
  '': '',
  'Authorization': 'Token f66d3d923c696d1c56434d16013fd954d631cc88',
  'Cookie': 'csrftoken=PsdLnWTNiqkHETaljcYDf1xPf4bakebS; sessionid=cnhqdxlmtod3utrio04v4vcl7qrttfwx'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())
