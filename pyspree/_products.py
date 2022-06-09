import json


# def _arch_list_all_products(self, name=None, in_stock=None, description=None):
#     endpoint = "/api/v2/storefront/products?"
#     sufix = ""
#     if name is not None:
#         sufix += "filter%5Bname%5D=" + name + "&"
#     else:
#         sufix += ""
#
#     if in_stock is not None:
#         sufix += "filter%5Bin_stock%5D=" + str(in_stock) + "&"
#     else:
#         sufix += ""
#
#     if description is not None:
#         sufix += "filter%5Bdescription%5D=" + description + "&"
#     headers = {'content-type': 'application/json'}
#
#     r = self.session.get(self.base_url + endpoint + sufix, headers=headers)
#     self.log(r)
#     return r

def list_all_products(self, filters={"filter[in_stock]": "true"}, per_page=300):
    """

    :param self:
    :param filters:
    example of filters :
    filters = {
                "filter[in_stock]":True,
                "filter[options][tshirt-color]":"red",
                "filter[price]":"10,100"
                }
    :return:
    """
    endpoint = "/api/v2/storefront/products"
    filters['per_page'] = per_page
    filters['filter[in_stock]'] = True

    # filters={"filter[in_stock]":"true","per_page":"300"}

    headers = {'content-type': 'application/json'}
    # filters={"filter":{"taxons":"3","option_value_ids":"","properties":{"brand":"alpha"},"name":""}}
    r = self.session.get(self.base_url + endpoint, headers=headers, data=json.dumps(filters))

    self.log(r)
    return r


def retrieve_a_product(self, id=None):
    endpoint = "/api/v2/storefront/products/"

    headers = {'content-type': 'application/json'}

    r = self.session.get(self.base_url + endpoint + str(id), headers=headers)
    self.log(r)
    return r


if __name__ == '__main__':
    from SpreeAPIManager import SpreeAPIManager
    from pprint import pprint

    sam = SpreeAPIManager(test_mode=True)
    r = sam.retrieve_a_product(id=16)
    pprint(r)
