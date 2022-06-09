import json


def create_or_refresh_a_token(self):
    endpoint = 'spree_oauth/token'
    data = \
        {"grant_type": "password",
         "username": self.api_data.username,
         "password": self.api_data.password
         }
    headers = {'Content-Type': 'application/json'}

    r = self.session.post(self.base_url + endpoint, headers=headers, data=json.dumps(data))
    response = r.json()
    self.set_bearer_token(response['access_token'])
    self.auth_mode = 'Bearer Auth'
    self.log(r)
    return r
