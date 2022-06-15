import json


def list_payment_methods(self):
    endpoint = "/api/v2/storefront/checkout/payment_methods"

    headers = self.get_headers()

    r = self.session.get(self.base_url + endpoint, headers=headers)
    self.log(r)
    return r


def create_new_payment(self, fields_cart="token,currency,number",
                       include="line_items,variants,variants.images,billing_address,shipping_address,user,payments,shipments,promotions"):
    endpoint = "/api/v2/storefront/checkout/create_payment"
    headers = self.get_headers(content_type_basic=False)
    # params={"fields[cart]":fields_cart,"include":include}

    data = {
        "payment_method_id": "2",

    }
    r = self.session.post(self.base_url + endpoint, headers=headers, data=json.dumps(data))
    self.log(r)
    return r
