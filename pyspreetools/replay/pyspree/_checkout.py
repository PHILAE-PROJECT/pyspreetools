import json


def update_checkout(self, information_to_update="email"):
    endpoint = '/api/v2/storefront/checkout'
    headers = self.get_headers(content_type_basic=False)

    if information_to_update == "email":
        data = {
            "order": {
                "email": self.api_data.email,

            }}
    elif information_to_update == "bill_address_attributes":
        data = {
            "order": {
                "bill_address_attributes": self.api_data.complete_address

            }
        }
        # data = {"order": {
        # "ship_address_attributes": {"firstname": "fred", "lastname": "tam", "address1": "2 rue charlie",
        #                             "address2": "45", "zipcode": "33000", "city": "portland",
        #                             "state_name": "Nebraska", "country_iso": "US", "phone": "000000000"}}}


    elif information_to_update == "ship_address_attributes":
        data = {
            "order": {
                "ship_address_attributes": self.api_data.complete_address,
            }
        }
        # data = {"order": {
        #     "bill_address_attributes": {"firstname": "fred", "lastname": "tam", "address1": "2 rue charlie",
        #                                 "address2": "45", "zipcode": "33000", "city": "portland",
        #                                 "state_name": "Nebraska", "country_iso": "US", "phone": "000000000"}}}

    elif information_to_update == 'selected_shipping_rate':

        data = {
            "order": {
                "shipments_attributes": [
                    {"id": self.api_data.shipment_id,
                     "selected_shipping_rate_id": self.api_data.shipping_rate}]}
        }

    elif information_to_update == 'payments_attributes':
        data = {"order": {"payments_attributes": [{"payment_method_id": "2"}]}}
    else:
        raise ValueError('Wrong value for information to update')

    r = self.session.patch(self.base_url + endpoint, data=json.dumps(data), headers=headers)

    self.log(r)
    return r
