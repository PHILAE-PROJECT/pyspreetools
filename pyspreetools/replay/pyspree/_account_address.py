import json


def list_all_addresses(self, fields_address="firstname,lastname,country_name"):
    endpoint = '/api/v2/storefront/account/addresses'
    # headers = self.get_bearer_token_header(content_type_basic=True)
    headers = self.get_headers(content_type_basic=True)
    params = {"fields[address]": fields_address}
    r = self.session.get(self.base_url + endpoint, headers=headers, params=params)

    self.log(r)
    return r


def create_an_address(self, fields_address='firstname,lastname,country_name'):
    endpoint = '/api/v2/storefront/account/addresses'
    headers = self.get_bearer_token_header(content_type_basic=False)
    params = {"fields[address]": fields_address}
    data = {"address":
        {
            "firstname": self.api_data.first_name,
            "lastname": self.api_data.last_name,
            "address1": self.api_data.address1,
            "address2": self.api_data.address2,
            "city": self.api_data.city,
            "phone": self.api_data.phone,
            "zipcode": self.api_data.zipcode,
            "state_name": self.api_data.state_name,
            "country_iso": self.api_data.country_iso,
            "label": self.api_data.label
        }
    }
    r = self.session.post(self.base_url + endpoint, headers=headers, data=json.dumps(data), params=params)
    self.log(r)
    return r


def remove_an_address(self, id):
    endpoint = '/api/v2/storefront/account/addresses'
    headers = self.get_bearer_token_header(content_type_basic=False)
    r = self.session.delete(self.base_url + endpoint + str(id), headers=headers)
    self.log(r)
    return r


def update_an_address(self, id):
    endpoint = '/api/v2/storefront/account/addresses/'
    headers = self.get_bearer_token_header(content_type_basic=False)
    r = self.session.patch(self.base_url + endpoint + str(id), headers=headers)
    self.log(r)
    return r
