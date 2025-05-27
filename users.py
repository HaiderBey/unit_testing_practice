import requests

BASE_URL = f"https://reqres.in/api/users/"
headers = {
    "x-api-key": "reqres-free-v1"
}

def fetch_user_data(user_id):
    url = f"{BASE_URL}{user_id}"
    response = requests.get(url, headers = headers)
    
    if response.status_code != 200:
        raise ValueError("User not found")

    return response.json()

print(fetch_user_data(7)["data"])