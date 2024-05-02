import requests

# CSRF tokenini olish uchun login sahifasiga GET so'rov yuborish
response = requests.get('http://127.0.0.1:8000/login/')

# HTML matnidan CSRF tokenini izlash
csrf_token = response.text.split('name="csrfmiddlewaretoken" value="')

for i in csrf_token:
    print(i[1])
    break


# # Yuboriladigan ma'lumotlar
# data = {
#     'username': 'ogabek',
#     'password': '123',
#     'csrfmiddlewaretoken': csrf_token  # CSRF tokenini qo'shish
# }

# # Login so'rovi jo'natish
# response = requests.post('http://127.0.0.1:8000/login/', data=data)

# # Login so'rovi javobi
# print(response.status_code)  # Javob kodi
# print(response.json())  # Javobning JSON formatdagi matni
