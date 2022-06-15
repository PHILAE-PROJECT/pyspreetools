import random
from .Taxon import Taxon


class Taxons:

    def __init__(self, taxons=None, response=None):
        self.max_depth = 0
        self.taxons = []
        if response is None and taxons is not None:
            self.taxons = taxons
        elif response is not None and taxons is None:
            self.taxons = self.parse_list_all_taxons_response(response)
        else:
            raise ValueError('provide a taxons input or a response input')
        self.children = self.get_all_children()

    def parse_list_all_taxons_response(self, response):

        taxons = response.json()
        taxons = taxons['data']
        list_of_taxons = []
        for taxon in taxons:
            t = Taxon(taxon)
            if t.depth > self.max_depth:
                self.max_depth = t.depth
            list_of_taxons.append(t)
        return list_of_taxons

    def pick_taxons_from_depth(self, depth):
        list_taxons = []
        for t in self.taxons:
            if t.depth == depth:
                list_taxons.append(t)
        return Taxons(taxons=list_taxons)

    def pick_a_random_taxon(self):
        return random.choice(self.taxons)

    def pick_a_random_children(self):
        return random.choice(self.children)

    def get_all_children(self):
        children = []
        for t in self.taxons:
            children += t.children
        return list(set(children))

    def __repr__(self):
        return '\n'.join([elt.__repr__() for elt in self.taxons])
