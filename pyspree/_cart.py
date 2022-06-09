import warnings


def create_a_cart(self):
    endpoint = "/api/v2/storefront/cart"
    # payload = {
    #     "public_metadata": {
    #         "total_weight": 3250
    #     },
    #     "private_metadata": {
    #         "had_same_cart_items": True
    #     }
    # }
    r = self.session.post(self.base_url + endpoint)
    response = r.json()
    try:
        self.set_order_token(response['data']['attributes']['token'])
    except KeyError:
        self.session_with_bug = True

        warnings.warn('Can t extract token from response')
    self.log(r)

    return r


def retrieve_a_cart(self):
    endpoint = '/api/v2/storefront/cart'
    headers = self.get_headers()
    r = self.session.get(self.base_url + endpoint, headers=headers)

    self.log(r)

    return r


def delete_a_cart(self, ):
    endpoint = '/api/v2/storefront/cart'
    headers = self.get_headers()
    r = self.session.delete(self.base_url + endpoint, headers=headers)

    self.log(r)

    return r
