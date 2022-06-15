class Taxon:

    def __init__(self, dict_taxon):
        self.id = dict_taxon['id']
        self.pretty_name = dict_taxon['attributes']['pretty_name']
        self.permalink = dict_taxon['attributes']['permalink']
        self.depth = dict_taxon['attributes']['depth']
        self.parent = []
        self.children = []
        children_raw = dict_taxon['relationships']['children']['data']
        parents_raw = dict_taxon['relationships']['parent']['data']
        if parents_raw is not None:
            self.parent.append(parents_raw['id'])

        if len(children_raw) > 0:
            for c in children_raw:
                self.children.append(c['id'])

    def __repr__(self):
        return ' | '.join(
            str(elt) for elt in [self.id, self.pretty_name, self.permalink, self.depth, self.parent, self.children])
