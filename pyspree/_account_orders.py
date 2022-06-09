def list_all_orders(self, fields_cart="token,currency,number", page=1, per_page=25,
                    include="line_items,variants,variants.images,billing_address,shipping_address,user,payments,shipments,promotions"):
    endpoint = "/api/v2/storefront/account/orders"

    headers = self.get_bearer_token_header(content_type_basic=True)
    params = {"fields[cart]": fields_cart,
              "page": str(page), "per_page": per_page,
              "include": include}
    r = self.session.get(self.base_url + endpoint, headers=headers, params=params)
    self.log(r)
    return r


def retrieve_an_order(self, order_number, fields_cart="cc_type,last_digits,month,year,name",
                      include="payment_method"):
    endpoint = '/api/v2/storefront/account/orders/'

    headers = self.get_bearer_token_header(content_type_basic=True)

    params = {"fields[cart]": fields_cart,
              "include": include}

    r = self.session.get(self.base_url + endpoint + str(order_number), headers=headers)
    self.log(r)
    return r
