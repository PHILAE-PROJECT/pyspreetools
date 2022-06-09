def list_all_countries(self, fields_cart="token,currency,number",
                       include="line_items,variants,variants.images,billing_address,shipping_address,user,payments,shipments,promotions"):
    endpoint = '/api/v2/storefront/countries'
    headers = {'Content-Type': 'application/json'}

    r = self.session.get(self.base_url + endpoint, headers=headers)
    self.log(r)
    return r


def retrieve_a_country(self, country_iso='US'):
    endpoint = '/api/v2/storefront/countries'
    headers = {'Content-Type': 'application/json'}

    r = self.session.get(self.base_url + endpoint + country_iso, headers=headers)
    self.log(r)
    return r
