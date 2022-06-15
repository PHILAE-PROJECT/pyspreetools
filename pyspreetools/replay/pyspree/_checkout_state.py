import requests


def next_checkout_step(self, fields_cart="token,currency,number",
                       include="line_items,variants,variants.images,billing_address,shipping_address,user,payments,shipments,promotions"):
    endpoint = '/api/v2/storefront/checkout/next'
    headers = self.get_headers()
    # params = {"fields[cart]": fields_cart,
    #           "include": include}

    r = self.session.patch(self.base_url + endpoint, headers=headers)
    self.log(r)
    return r


def advance_checkout(self, fields_cart="token,currency,number",
                     include="line_items,variants,variants.images,billing_address,shipping_address,user,payments,shipments,promotions"):
    endpoint = '/api/v2/storefront/checkout/advance'
    headers = self.get_headers()
    params = {"fields[cart]": fields_cart,
              "include": include}

    r = self.session.patch(self.base_url + endpoint, headers=headers, params=params)
    self.log(r)
    return r


def complete_checkout(self,
                      include="line_items,variants,variants.images,billing_address,shipping_address,user,payments,shipments,promotions"):
    endpoint = '/api/v2/storefront/checkout/complete'
    headers = self.get_headers()
    params = {
        "include": include}

    r = self.session.patch(self.base_url + endpoint, headers=headers, params=params)
    self.log(r)
    return r
