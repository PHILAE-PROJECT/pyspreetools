from pyspree.Product import Product
import random


class Products:
    def __init__(self, products=None, response=None):

        self.products = []
        if response is None and products is not None:
            self.products = products
        elif response is not None and products is None:
            self.products = self.parse_list_all_products_response(response)
        else:
            raise ValueError('provide a products input or a response input')
        self.available_properties = self.get_available_properties(response)

    def parse_list_all_products_response(self, response):

        products = response.json()
        # print("hello",products)
        products = products['data']
        list_of_products = []
        for product in products:
            t = Product(product)

            list_of_products.append(t)
        return list_of_products

    def pick_a_random_product(self):
        product = random.choice(self.products)
        return product

    def most_frequent_terms(self):
        self.most_frequent_terms = []
        for p in self.products:
            self.most_frequent_terms += p.name.split(' ')

    def get_available_properties(self, response):
        properties = {}

        products = response.json()
        products = products['meta']
        for filter in products['filters']['option_types']:
            properties[filter['name']] = []
            for option_values in filter['option_values']:
                properties[filter['name']].append(option_values['name'])
        for filter in products['filters']['product_properties']:
            properties[filter['name']] = []
            for option_values in filter['values']:
                properties[filter['name']].append(option_values['filter_param'])
        return properties

    def __len__(self):
        return len(self.products)

    def __repr__(self):
        return '\n'.join([elt.__repr__() for elt in self.products])
