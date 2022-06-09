def list_all_credit_cards(self, fields_credit_card="cc_type,last_digits,month,year,name", filter_payment_method_id=1,
                          include="payment_method"):
    endpoint = "/api/v2/storefront/account/credit_cards"

    headers = self.get_headers()

    # params = {"fields[credit_card]": fields_credit_card,
    #           "filter[payment_method_id]": filter_payment_method_id,
    #           "include": include}
    # params = {"fields[credit_card]": fields_credit_card,
    #
    #           "include": include}
    r = self.session.get(self.base_url + endpoint, headers=headers)
    self.log(r)
    return r


def remove_a_credit_card(self, id):
    endpoint = "/api/v2/storefront/account/credit_cards/"

    headers = self.get_bearer_token_header(content_type_basic=True)

    r = self.session.delete(self.base_url + endpoint + str(id), headers=headers)
    self.log(r)
    return r


def retrieve_the_default_credit_card(self, fields_credit_card="cc_type,last_digits,month,year,name",
                                     include="payment_method"):
    endpoint = '/api/v2/storefront/account/credit_cards/default'

    headers = self.get_bearer_token_header(content_type_basic=True)

    params = {"fields[credit_card]": fields_credit_card,
              "include": include}

    r = self.session.get(self.base_url + endpoint, headers=headers, params=params)
    self.log(r)
    return r
