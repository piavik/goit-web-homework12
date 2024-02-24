import json
import requests
from  faker import Faker

def generate_fake_data(num):
    fake = Faker()
    fake_users = []

    for _ in range(num):
        user = {"username": fake.user_name(),
                "email":    fake.email(),
                "password": fake.password()
                }
        fake_users.append(user)
    return fake_users

def put_date_to_DB(users):
    base_url = "http://192.168.0.222:8000"
    headers = {'Content-type': 'application/json'}
    for user in users:
        print(f"{user['email']} - {user['password']}")
        response = requests.post(f'{base_url}/auth/signup/', 
                                data=json.dumps(user), 
                                headers=headers
                                )


if __name__ == "__main__":
    fake_users = generate_fake_data(5)
    put_date_to_DB(fake_users)
