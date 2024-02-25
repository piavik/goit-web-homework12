import json
import requests
import logging

# from  random import randint
from  faker import Faker

logging.basicConfig(level=logging.INFO)

def generate_fake_users(num):
    fake = Faker()
    fake_users = []

    for _ in range(num):
        user = {"username": fake.user_name(),
                "email":    fake.email(),
                "password": fake.password()
                }
        fake_users.append(user)
    return fake_users

def create_users_via_api(users):
    base_url = "http://192.168.0.222:8000"
    headers = {'Content-type': 'application/json'}
    for user in users:
        logging.info(f"{user['username']=} /n {user['email']=} /n {user['password']}")      # for interactive use
        response = requests.post(f'{base_url}/auth/signup', 
                                data=json.dumps(user), 
                                headers=headers
                                )

def login_and_get_token(user):
    base_url = "http://192.168.0.222:8000"
    # headers = {'Content-type': 'application/json'}
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    logging.info(user)
    response = requests.post(f'{base_url}/auth/login', 
                                data=json.dumps({"username": user['email'], "password": user['password']}), 
                                headers=headers
                                )
    logging.info(f'login with /auth/login responce:   {response.text}')
    return response.text

def generate_fake_contacts(num):
    fake = Faker()
    fake_contacts = []

    for _ in range(num):
        contact = { "first_name":   fake.first_name(),
                    "last_name":    fake.last_name(),
                    "email":        fake.email(),
                    "phone":        fake.msisdn(),
                    "birthday":     fake.date(),
                    "notes":        fake.sentence(),
                  }
        fake_contacts.append(contact)
    return fake_contacts

def put_contacts_to_DB(contacts, token):
    base_url = "http://192.168.0.222:8000"
    headers = {'Content-type': 'application/json',
               'Authorization': 'Bearer ' + token
                }
    for contact in contacts:
        response = requests.post(f'{base_url}/api/contacts', 
                                data=json.dumps(contact), 
                                headers=headers
                                )


if __name__ == "__main__":
    #test
    user = {"username": 'khall',
            "email":    'abrown@example.com',
            "password": 'J2tF5nHf)p'
            }
    # fake_users = generate_fake_users(1)
    # create_users_via_api(fake_users)
    # for user in fake_users:
    token_json = login_and_get_token(user)
    logging.info(f'{token_json=}')
        # fake_contacts = generate_fake_contacts(10)
        # put_contacts_to_DB(fake_contacts, token_json['access_token'])

