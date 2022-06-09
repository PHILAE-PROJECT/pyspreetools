import random
import uuid
from pyspree.APIData import APIData
from pyspree.Products import Products
from pyspree.Taxons import Taxons
import requests
from pprint import pprint
from datetime import datetime
import time
import json


class SpreeAPIManager:
    def __init__(self, config_file_path=None,config_dict=None):
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y__%H_%M_%S")

        if config_file_path is None and config_dict is None:
            self.base_url = "https://demo.spreecommerce.org/"
            self.logging = True
            self.log_file = './logs/log'
            self.test_mode = True
            self.verbose = False
            self.sleep_time = 0.1

        elif config_file_path is not None:
            with open(config_file_path) as json_file:
                self.config = json.load(json_file)

            self.base_url = self.config['base_url']
            self.logging = self.config['logging']
            self.log_file = self.config['log_file'].replace('.json', '_' + dt_string + '.json')
            self.test_mode = self.config['test_mode']
            self.verbose = self.config['verbose']
            self.sleep_time = self.config['sleep_time']
        else:
            self.base_url = config_dict['base_url']
            self.logging = config_dict['logging']
            self.log_file = config_dict['log_file'].replace('.json', '_' + dt_string + '.json')
            self.test_mode = config_dict['test_mode']
            self.verbose = config_dict['verbose']
            self.sleep_time = config_dict['sleep_time']

        self.session = requests.Session()

        # Manage controlled Randomness
        seed = 0
        self.rd = random.Random()
        self.rd.seed(seed)

        # Manage some statistics of the execution
        self.session_counter = 1
        self.init_time = time.time()
        self.session_with_bug = False
        self.session_with_bug_counter = 0
        # if self.test_mode and self.logging:
        #     self.log_file= '../logs/log0.json'

        # Initialize Log file
        if self.logging:
            with open(self.log_file, 'w') as f:
                f.write('{}' + '\n')

        # Initialization of Session
        self.new_session()
        # Get all the products and taxons
        self.products = self.get_all_products()
        self.taxons = self.get_all_taxons()

    from pyspree._account import create_an_account, retrieve_an_account
    from pyspree._account_address import create_an_address, remove_an_address, update_an_address, list_all_addresses
    from pyspree._account_orders import list_all_orders, retrieve_an_order
    from pyspree._account_credit_cards import list_all_credit_cards
    from pyspree._auth_token import create_or_refresh_a_token
    from pyspree._cart import create_a_cart, retrieve_a_cart, delete_a_cart
    from pyspree._cart_line_items import add_an_item_to_cart, remove_a_line_item, set_line_item_quantity
    from pyspree._cart_other import associate_a_cart_with_a_user, empty_the_cart
    from pyspree._checkout_shipments import select_shipping_method_for_shipment, list_shipping_rates
    from pyspree._checkout_payments import create_new_payment, list_payment_methods
    from pyspree._checkout_state import next_checkout_step, advance_checkout, complete_checkout
    from pyspree._countries import retrieve_a_country
    from pyspree._checkout import update_checkout
    from pyspree._menus import list_all_menus, retrieve_a_menu
    from pyspree._products import retrieve_a_product, list_all_products
    from pyspree._taxons import list_all_taxons, retrieve_a_taxon
    from pyspree._wishlists import list_all_wishlists, create_a_wish_list, retrieve_a_wishlist, update_a_wishlist, \
        delete_a_wishlist, retrieve_the_default_wishlist
    from pyspree._wishlists_wished_items import add_item_to_wishlist, set_wished_item_quantity, \
        delete_item_from_wishlist
    from pyspree._utils_checkout import guest_checkout, registered_user_checkout

    def new_session(self):
        if self.session_with_bug == True:
            self.session_with_bug += 1
        print("%session ok :", str((self.session_counter - self.session_with_bug_counter) / self.session_counter))
        self.api_data = APIData()
        self.auth_mode = 'API Key'
        self.session_with_bug = False
        self.session_id = uuid.UUID(int=self.rd.getrandbits(128)).int
        self.order_token = None
        self.bearer_token = True
        self.session_counter += 1
        print('session #' + str(self.session_counter))
        print('time elapsed :', time.time() - self.init_time)

    def get_bearer_token_header(self, content_type_basic=True):

        if content_type_basic:
            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer " + self.get_bearer_token(),
                # 'User-Agent': 'Chrome'
            }
            return headers
        else:
            headers = {
                'Content-Type': "application/vnd.api+json",
                'Authorization': "Bearer " + self.get_bearer_token(),
                # 'User-Agent': 'Chrome'
            }
            return headers

    def get_order_token_headers(self, content_type_basic=True):

        if content_type_basic:
            headers = {'Content-Type': 'application/vnd.api+json', 'X-Spree-Order-Token': self.get_order_token()}
            return headers
        else:
            headers = {'Content-Type': 'application/json', 'X-Spree-Order-Token': self.get_order_token()}
            return headers

    def get_headers(self, auth_mode=None, content_type_basic=True):

        if auth_mode is None:
            auth_mode = self.auth_mode
        if auth_mode == 'API Key':
            headers = self.get_order_token_headers(content_type_basic)
        elif auth_mode == 'Bearer Auth':
            headers = self.get_bearer_token_header(content_type_basic)
        else:
            raise ValueError('wrong input for mode parameters, it should be either API key or Bearer Auth')
        return headers

    def set_order_token(self, order_token):
        self.order_token = order_token

    def set_bearer_token(self, bearer_token):
        self.bearer_token = bearer_token

    def get_order_token(self):
        if self.order_token is None:
            raise AttributeError(" Spree API Manager does not have a order token yet")
        return self.order_token

    def get_bearer_token(self):
        if self.bearer_token is None:
            raise AttributeError(" Spree API Manager does not have a order token yet")
        return self.bearer_token

    def get_all_products(self):
        products = self.list_all_products(per_page=400)
        return Products(response=products)

    def get_all_taxons(self):
        taxons = self.list_all_taxons()
        return Taxons(response=taxons)

    def log(self, r):
        time.sleep(self.sleep_time)
        log = {}
        q = r.request
        if self.logging:
            try:
                log['session_id'] = self.session_id
            except:
                pass
            log['url'] = q.url
            log['method'] = q.method
            if hasattr(q, 'body') and q.body is not None:
                try:
                    log['body'] = json.loads(q.body)
                except:
                    log['body'] = None
            log['headers'] = (dict(q.headers))
            try:
                log['responses'] = r.json()
            except:
                log['responses'] = None
            log['status_code'] = r.status_code

            with open(self.log_file, "a") as file_object:
                file_object.write(json.dumps(log) + '\n')
        if self.test_mode:
            print(q.url, q.method, r.status_code)
            if self.verbose:
                try:
                    pprint(r.json())
                except:
                    pass
            if hasattr(q, 'body') and q.body is not None:
                try:
                    print(json.loads(q.body))
                except:
                    pass
