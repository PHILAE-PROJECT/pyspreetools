import json


def add_an_item_to_cart(self, variant_id, quantity):
    endpoint = '/api/v2/storefront/cart/add_item'

    headers = self.get_headers()

    data = {
        "variant_id": variant_id,
        "quantity": quantity,
        # "public_metadata": {"first_item_order": True},
        # "private_metadata": {"recommended_by_us": False}
    }
    r = self.session.post(self.base_url + endpoint, headers=headers, data=json.dumps(data))

    self.log(r)

    return r


def set_line_item_quantity(self, line_item_id, quantity):
    endpoint = '/api/v2/storefront/cart/set_quantity'

    headers = self.get_headers(content_type_basic=True)
    data = {
        "line_item_id": str(line_item_id),
        'quantity': str(quantity)
    }

    r = self.session.patch(self.base_url + endpoint, headers=headers, data=json.dumps(data))
    self.log(r)
    return r


def remove_a_line_item(self, line_item_id):
    endpoint = '/api/v2/storefront/cart/remove_line_item/'

    headers = self.get_headers(content_type_basic=True)

    r = self.session.delete(self.base_url + endpoint + str(line_item_id), headers=headers)
    self.log(r)
    return r
