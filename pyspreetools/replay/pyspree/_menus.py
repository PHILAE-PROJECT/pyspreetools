def list_all_menus(self):
    endpoint = '/api/v2/storefront/menus/'
    r = self.session.get(self.base_url + endpoint)

    self.log(r)
    return r


def retrieve_a_menu(self, menu_id):
    assert type(menu_id) == int
    endpoint = '/api/v2/storefront/menus/'
    r = self.session.get(self.base_url + endpoint + str(menu_id))
    self.log(r)
    return r
