from random import randint
import requests
import random
import string


class APIData:
    def __init__(self):
        random_number = randint(0, 9999)
        letters = string.ascii_lowercase
        random_letters = ''.join(random.choice(letters) for i in range(10))
        self.first_name = "fred" + random_letters
        self.last_name = "tam" + random_letters
        self.password = "philae123" + str(random_number)
        self.email = self.first_name + self.last_name + "@philae.com"
        self.username = self.email
        self.address1 = str(random_number) + "chemin du bois fleuri"
        self.address2 = "bat" + str(random_number)
        self.city = "Portland"
        self.phone = "0606060606"
        self.zipcode = "97035"
        self.state_name = 'Nebraska'
        self.country_iso = "US"
        self.label = "work"
        self.credit_card = {
            "number": "4242424242424242",
            "exp_month": "3",
            "exp_year": "2023",
            "cvc": "314"
        }
        self.complete_address = {
            "firstname": self.first_name,
            "lastname": self.last_name,
            "address1": self.address1,
            "city": self.city,
            "phone": self.phone,
            "zipcode": self.zipcode,
            "state_name": self.state_name,
            "country_iso": self.country_iso
        }
        self.shipment_id = str(0)
        self.shipping_rate = str(0)

    def create_a_card_token(self, experimental=False):

        if experimental:
            endpoint = "https://api.stripe.com/v1/tokens"
            test_token = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
            data = 'card[number]=' + self.credit_card['number'] + '&card[exp_month]=' + self.credit_card[
                'exp_month'] + '&card[exp_year]=' + self.credit_card['exp_year'] + '&card[cvc]=' + self.credit_card[
                       'cvc']
            r = requests.post(endpoint, data=data, auth=(test_token, ''))
            self.gateway_payment_profile_id = r.json()["card"]['id']
            return r
        else:
            self.gateway_payment_profile_id = 'card_1Kj4VQ2eZvKYlo2C09pqWoYC'
            return {'id': 'tok_1Kj4VR2eZvKYlo2C60pdOx1D', 'object': 'token',
                    'card': {'id': 'card_1Kj4VQ2eZvKYlo2C09pqWoYC', 'object': 'card', 'address_city': None,
                             'address_country': None, 'address_line1': None, 'address_line1_check': None,
                             'address_line2': None, 'address_state': None, 'address_zip': None,
                             'address_zip_check': None, 'brand': 'Visa', 'country': 'US', 'cvc_check': 'unchecked',
                             'dynamic_last4': None, 'exp_month': 3, 'exp_year': 2023, 'fingerprint': 'Xt5EWLLDS7FJjR1c',
                             'funding': 'credit', 'last4': '4242', 'metadata': {}, 'name': None,
                             'tokenization_method': None}, 'client_ip': '193.253.78.1', 'created': 1648658185,
                    'livemode': False, 'type': 'card', 'used': False}


if __name__ == '__main__':
    api_data = APIData()
    r = api_data.create_a_card_token(experimental=False)

    print(r)
