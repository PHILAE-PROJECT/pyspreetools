from pyspree.Filters import Filters
from pyspree.Products import Products
import random
import sys


class UserSimulator:

    def __init__(self, spreeApiManager):
        self.sam = spreeApiManager
        self.basket = []
        self.abstract_trace = []
        self.logged = False

    def start_navigation(self):
        self.abstract_trace.append('start navigation')
        self.sam.new_session()
        self.sam.create_a_cart()
        # Next step
        self.enter_home()

    def enter_home(self):
        self.abstract_trace.append('enter home')

        self.sam.list_all_taxons()
        if len(self.abstract_trace) > 7 and random.random() > 0.7:
            self.end_navigation()
            return

        # Next step
        self.browse()

    def browse(self, taxon=None):
        self.abstract_trace.append('browse')

        level_1_taxon = taxon

        if taxon is None:
            taxons = self.sam.taxons.pick_taxons_from_depth(1)
            level_1_taxon = taxons.pick_a_random_taxon()

        f = Filters(taxon=level_1_taxon.id)
        products_response = self.sam.list_all_products(filters=f.to_filter_dict())

        if random.random() > 0.3:
            self.abstract_trace.append('sort by price')
            f = Filters(taxon=level_1_taxon.id, sort="price")
            products_response = self.sam.list_all_products(filters=f.to_filter_dict())

        products = Products(response=products_response)

        # Next step
        if random.random() > 0.3:
            self.look_for_a_product(products, level_1_taxon)
        else:
            self.enter_home()

    def look_for_a_product(self, products, previous_taxon):
        self.abstract_trace.append('look for a product')

        random_product = products.pick_a_random_product()
        self.sam.retrieve_a_product(random_product.slug)
        if random.random() > 0.7:
            self.add_product_to_basket(random_product)
        elif random.random() > 0.3:
            self.enter_home()
        else:
            self.browse(taxon=previous_taxon)

    def add_product_to_basket(self, random_product):
        self.abstract_trace.append('add_product_to_basket')
        self.sam.add_an_item_to_cart(variant_id=random_product.id_default_variant, quantity=1)
        self.basket.append(random_product.id)

        random_number = random.random()
        if len(self.abstract_trace) > 15 or len(self.basket) > 3:
            self.checkout()
        elif random_number > 0.7:
            self.checkout()
        elif random_number > 0.5:

            try:
                self.abstract_trace.append('modify quantity')
                id = self.sam.retrieve_a_cart().json()['data']['relationships']['line_items']['data'][0]['id']

                self.sam.set_line_item_quantity(id, quantity=2)
                self.enter_home()

            except:
                self.sam.session_with_bug = True

                self.enter_home()

        else:
            self.enter_home()

    def checkout(self):
        if len(self.basket) > 1 and random.random() > 0.3:
            try:
                self.abstract_trace.append('remove a line item')
                # print(self.sam.retrieve_a_cart().json())
                id = self.sam.retrieve_a_cart().json()['data']['relationships']['line_items']['data'][0]['id']
                self.sam.remove_a_line_item(id)
            except:
                self.sam.session_with_bug = True

        if random.random() > 0.5:
            self.abstract_trace.append('create an account')

            self.sam.create_an_account()
            self.sam.create_or_refresh_a_token()
            self.sam.associate_a_cart_with_a_user()

            self.abstract_trace.append('registered_user_checkout')
            self.abstract_trace.append('create an address')
            self.sam.create_an_address()
            self.sam.registered_user_checkout()

            if random.random() > 0.3:
                self.abstract_trace.append('Browse all orders')
                try:
                    order_number = self.sam.list_all_orders().json()['data'][0]['attributes']['number']
                    self.abstract_trace.append('View last order status')
                    self.sam.retrieve_an_order(order_number)
                except:
                    self.sam.session_with_bug = True

            self.end_navigation()
        else:
            self.abstract_trace.append('guest_checkout')
            self.sam.guest_checkout()
            self.end_navigation()

    def end_navigation(self):
        self.abstract_trace.append('end navigation')
