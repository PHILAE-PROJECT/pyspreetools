import json
import sys
import unittest
# #Here spree_simulator_local_path= ~/spree_simulator/api
# with open('../config/spreeprocessing.json') as json_file:
#     spree_simulator_local_path = json.load(json_file)['spree_simulator_local_path']
#
# sys.path.insert(0, spree_simulator_local_path)
from pyspree.SpreeAPIManager import SpreeAPIManager
from pyspree.Products import Products
from pyspree.Filters import Filters

class OneTraceExecutor(unittest.TestCase):

    def setUp(self,sam :SpreeAPIManager):
        self.sessions=dict()
        self.SEQ=None
        self.sam=sam
        self.products=None
        self.basket=[]
        self.current_product=None
        self.taxon=None
        self.id_to_modify = None

    def process(self,action,res):
        action=action.strip()
        if action=='createACart':
            self._exec_createACart(res)
        elif action=='retrieveAProduct':
            self._exec_retrieveAProduct(res)

        elif action =='addAnItemToCart':
            self._exec_addAnItemToCart(res)
        elif action=='associateACartWithAUser':
            self._exec_associateACartWithAUser(res)

        elif action =='advanceCheckout':
            self._exec_advanceCheckout(res)
        elif action =='updateCheckout_ChooseAShippingRate':
            self._exec_updateCheckout_ChooseAShippingRate(res)
        elif action =='completeCheckout':
            self._exec_completeCheckout(res)
        elif action =='listShippingRates':
            self._exec_listShippingRates(res)
    
        elif action =='updateCheckout_UpdateBillingInformation':
            self._exec_updateCheckout_UpdateBillingInformation(res)
        elif action =='updateCheckout_UpdateEmailInformation':
            self._exec_updateCheckout_UpdateEmailInformation(res)
        elif action =='updateCheckout_UpdatePaymentMethod':
            self._exec_updateCheckout_UpdatePaymentMethod(res)
        elif action =='updateCheckout_UpdateShippingInformation':
            self._exec_updateCheckout_UpdateShippingInformationres(res)
        elif action =='nextCheckoutStep':
            self._exec_nextCheckoutStep(res)
        elif action =='createAnAccount':
            self._exec_createAnAccount(res)
        elif action =='createAnAddress':
            self._exec_createAnAddress(res)
        elif action =='createOrRefreshAToken':
            self._exec_createOrRefreshAToken(res)
        elif action =='removeALineItem':
            self._exec_removeALineItem(res)
        elif action =='listAllTaxons':
            self._exec_listAllTaxons(res)
        elif action =='listAllProducts_SpecificTaxonFilter':
            self._exec_listAllProducts_SpecificTaxonFilter(res)
        elif action =='listAllProducts_SpecificTaxonFilter_SortByPrice':
            self._exec_listAllProducts_SpecificTaxonFilter_SortByPrice(res)
        elif action =='retrieveAnAccount':
            self._exec_retrieveAnAccount(res)
        elif action =='retrieveACart':
            self._exec_retrieveACart(res)
        elif action =='setLineItemQuantity':
            self._exec_setLineItemQuantity(res)
        else:
            print("Unknown operation:"+str(action))
            sys.exit(-1)
    def _exec_createACart(self,res):
        r=self.sam.create_a_cart()
        self.assertEqual(int(res), r.status_code)

    def _exec_retrieveAProduct(self,res):
        self.assertNotEqual(len(self.products.products),0)

        random_product = self.products.pick_a_random_product()
        r=self.sam.retrieve_a_product(random_product.slug)

        self.current_product=random_product

        self.assertEqual(int(res), r.status_code)
        #garbageCollector
        # self.products.products=[]

    def _exec_addAnItemToCart(self,res):

        r=self.sam.add_an_item_to_cart(variant_id=self.current_product.id_default_variant,quantity=1)
        self.basket.append(self.current_product.id)
        self.assertEqual(int(res), r.status_code)

    def _exec_associateACartWithAUser(self,res):
        r=self.sam.associate_a_cart_with_a_user(res)
        self.assertEqual(int(res), r.status_code)

    def _exec_advanceCheckout(self,res):
        r=self.sam.advance_checkout()
        self.assertEqual(int(res), r.status_code)

    def _exec_updateCheckout_ChooseAShippingRate(self,res):
        r=self.sam.update_checkout(information_to_update="selected_shipping_rate")
        self.assertEqual(int(res), r.status_code)

    def _exec_completeCheckout(self,res):
        r=self.sam.complete_checkout()
        self.assertEqual(int(res), r.status_code)


    def _exec_updateCheckout_UpdateBillingInformation(self,res):
        r=self.sam.update_checkout(information_to_update="bill_address_attributes")
        self.assertEqual(int(res), r.status_code)

    def _exec_nextCheckoutStep(self,res):
        r=self.sam.next_checkout_step()
        self.assertEqual(int(res), r.status_code)

    def _exec_createAnAccount(self,res):
        r=self.sam.createAnAccount()
        self.assertEqual(int(res), r.status_code)

    def _exec_createAnAddress(self,res):
        r=self.sam.create_an_address()
        self.assertEqual(int(res), r.status_code)


    def _exec_createOrRefreshAToken(self,res):
        r=self.sam.create_or_refresh_a_token()
        self.assertEqual(int(res), r.status_code)

    def _exec_removeALineItem(self,res):
        self.assertNotEqual(len(self.basket),0)
        id = self.sam.retrieve_a_cart().json()['data']['relationships']['line_items']['data'][0]['id']
        r=self.sam.remove_a_line_item(id)
        self.assertEqual(int(res), r.status_code)

    def _exec_listAllTaxons(self,res):

        r=self.sam.list_all_taxons()
        self.assertEqual(int(res), r.status_code)

    def _exec_listAllProducts_SpecificTaxonFilter(self,res):
        level_1_taxon = self.taxon

        if self.taxon is None:
            taxons = self.sam.taxons.pick_taxons_from_depth(1)
            level_1_taxon = taxons.pick_a_random_taxon()
        f = Filters(taxon=level_1_taxon.id)
        r = self.sam.list_all_products(filters=f.to_filter_dict())
        self.assertEqual(int(res), r.status_code)
        self.products = Products(response=r)

    def _exec_listAllProducts_SpecificTaxonFilter_SortByPrice(self,res):
        level_1_taxon = self.taxon

        if self.taxon is None:
            taxons = self.sam.taxons.pick_taxons_from_depth(1)
            level_1_taxon = taxons.pick_a_random_taxon()
        f = Filters(taxon=level_1_taxon.id, sort="price")
        r = self.sam.list_all_products(filters=f.to_filter_dict())
        self.assertEqual(int(res), r.status_code)
        self.products = Products(response=r)

    def _exec_retrieveAnAccount(self,res):

        order_number = self.sam.list_all_orders().json()['data'][0]['attributes']['number']
        r=self.sam.retrieve_an_order(order_number)
        self.assertEqual(int(res), r.status_code)

    def _exec_retrieveACart(self,res):
        r=self.sam.retrieve_a_cart()
        self.assertEqual(int(res), r.status_code)
        self.id_to_modify=r.json()['data']['relationships']['line_items']['data'][0]['id']


    def _exec_setLineItemQuantity(self,res):
        r=self.sam.set_line_item_quantity(self.id_to_modify, quantity=2)
        self.assertEqual(int(res), r.status_code)
        self.id_to_modify=None

    def _exec_listShippingRates(self, res):
        r=self.list_shipping_rates()
        self.assertEqual(int(res), r.status_code)

    def _exec_updateCheckout_UpdateEmailInformation(self, res):
        r=self.update_checkout(information_to_update="email")
        self.assertEqual(int(res), r.status_code)

    def _exec_updateCheckout_UpdatePaymentMethod(self, res):
        r=self.update_checkout(information_to_update='payments_attributes')
        self.assertEqual(int(res), r.status_code)
    def _exec_updateCheckout_UpdateShippingInformation(self, res):
        r=self.update_checkout(information_to_update="ship_address_attributes")
        self.assertEqual(int(res), r.status_code)

    def test_one_trace_as_test(self):

        for i_row,row in enumerate(self.SEQ):

            op=row[0].strip()
            res=row[1].strip()

            try:
                self.process(op,res)
            except:
                print(str(row)+" (line "+str(i_row)+")")
                sys.exit(-1)







