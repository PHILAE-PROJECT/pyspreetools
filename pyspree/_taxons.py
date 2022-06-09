def list_all_taxons(self):
    endpoint = '/api/v2/storefront/taxons/'
    querystring = {"per_page": "100"}
    r = self.session.get(self.base_url + endpoint, params=querystring)

    self.log(r)
    return r


def retrieve_a_taxon(self, taxon_permalink):
    endpoint = '/api/v2/storefront/taxons'
    r = self.session.get(self.base_url + endpoint + '/' + taxon_permalink)
    self.log(r)
    return r
