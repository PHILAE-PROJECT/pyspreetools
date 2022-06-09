import json


def select_shipping_method_for_shipment(self, fields_cart="token,currency,number",
                                        include="line_items,variants,variants.images,billing_address,shipping_address,user,payments,shipments,promotions"):
    endpoint = '/api/v2/storefront/checkout/select_shipping_method'
    headers = self.get_headers(content_type_basic=False)
    params = {"fields[cart]": fields_cart, "include": include}
    data = {'shipment_id': str(self.api_data.shipment_id),
            "shipping_method_id": str(self.api_data.shipping_rate)}
    # payload = "{\n  \"shipping_method_id\": \"1\"\n}"
    r = self.session.patch(self.base_url + endpoint, headers=headers, data=data)
    self.log(r)

    return r


def list_shipping_rates(self):
    endpoint = '/api/v2/storefront/checkout/shipping_rates'
    headers = self.get_headers(content_type_basic=True)
    r = self.session.get(self.base_url + endpoint, headers=headers)
    self.log(r)
    try:
        self.api_data.shipment_id = r.json()['data'][0]['id']
        self.api_data.shipping_rate = r.json()['data'][0]['relationships']['shipping_rates']['data'][0]['id']
    except:
        self.session_with_bug = True

    return r
