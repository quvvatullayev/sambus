import requests

# Yuboriladigan ma'lumotlar
data = {
    'username': 'admin',
    'password': '123'
}

# Login surovini jo'natish
response = requests.post('http://127.0.0.1:8000/auth/login/', data=data)

# Login surovining javobi
print(response.status_code)  # Javob kodi
print(response.json()) 