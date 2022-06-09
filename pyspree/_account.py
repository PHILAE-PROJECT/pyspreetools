import json


# def associate_a_cart_with_a_user(self):
#     endpoint = '/api/v2/storefront/cart/associate/'
#     headers = self.get_bearer_token_header(content_type_basic=False)
#     params = {"guest_order_token": self.get_order_token()}
#
#     r = self.session.patch(self.base_url + endpoint, headers=headers, params=params)
#
#     self.log(r)
#     return r

def retrieve_an_account(self):
    endpoint = '/api/v2/storefront/cart/account/'
    headers = self.get_headers(content_type_basic=True)

    r = self.session.get(self.base_url + endpoint, headers=headers)

    self.log(r)
    return r


def create_an_account(self, guest_mode=False):
    endpoint = '/api/v2/storefront/account/'
    headers = {'Content-Type': 'application/vnd.api+json'}
    if guest_mode:
        data = {
            "user": {
                "email": self.api_data.email,

                "public_metadata": {
                    "user_segment": "customer"
                },
                "private_metadata": {
                    "has_abandoned_cart": False
                }
            }
        }
    else:
        data = {
            "user": {
                "email": self.api_data.email,
                "first_name": self.api_data.first_name,
                "last_name": self.api_data.last_name,
                "password": self.api_data.password,
                "password_confirmation": self.api_data.password,
                "public_metadata": {
                    "user_segment": "customer"
                },
                "private_metadata": {
                    "has_abandoned_cart": False
                }
            }
        }

    r = self.session.post(self.base_url + endpoint, headers=headers, data=json.dumps(data))
    self.log(r)
    return r
