def guest_checkout(self):
    self.update_checkout(information_to_update="email")
    self.update_checkout(information_to_update="ship_address_attributes")
    self.update_checkout(information_to_update="bill_address_attributes")
    self.list_shipping_rates()
    self.update_checkout(information_to_update="selected_shipping_rate")
    self.advance_checkout()
    self.update_checkout(information_to_update='payments_attributes')
    self.complete_checkout()


def registered_user_checkout(self):
    # self.create_an_address()
    self.next_checkout_step()
    self.update_checkout(information_to_update="email")
    self.update_checkout(information_to_update="ship_address_attributes")
    self.update_checkout(information_to_update="bill_address_attributes")
    self.next_checkout_step()
    self.list_shipping_rates()
    self.advance_checkout()
    self.update_checkout(information_to_update='payments_attributes')
    self.complete_checkout()
