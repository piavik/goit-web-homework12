import json
import requests
from  faker import Faker

def generate_fake_data(num):
    fake = Faker()
    fake_contacts = []

    for _ in range(num):
        contact = { "first_name":   fake.first_name(),
                    "last_name":    fake.last_name(),
                    "email":        fake.email(),
                    "phone":        fake.msisdn(),
                    "birthday":     fake.date(),
                    "notes":        fake.sentence()
                  }
        fake_contacts.append(contact)
    return fake_contacts

def put_date_to_DB(contacts):
    base_url = "http://192.168.0.222:8000"
    headers = {'Content-type': 'application/json'}
    for contact in contacts:
        response = requests.post(f'{base_url}/api/contacts/', 
                                data=json.dumps(contact), 
                                headers=headers
                                )


if __name__ == "__main__":
    fake_contacts = generate_fake_data(100)
    put_date_to_DB(fake_contacts)
