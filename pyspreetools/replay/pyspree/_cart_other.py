def associate_a_cart_with_a_user(self):
    endpoint = '/api/v2/storefront/cart/associate'
    headers = self.get_headers(content_type_basic=False)
    params = {"guest_order_token": self.get_order_token()}

    r = self.session.patch(self.base_url + endpoint, headers=headers, params=params)
    self.log(r)
    return r


def empty_the_cart(self, auth_mode='API Key'):
    endpoint = 'api/v2/storefront/cart/empty'
    headers = self.get_headers(auth_mode)

    r = self.session.patch(self.base_url + endpoint, headers=headers)
    self.log(r)
    return r
