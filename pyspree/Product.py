class Product:
    def __init__(self, dict_product):
        self.slug = dict_product['attributes']['slug']
        self.name = dict_product['attributes']['name']
        self.id = dict_product['id']
        self.id_default_variant = dict_product['relationships']['default_variant']['data']['id']

    def __repr__(self):
        return ' | '.join(str(elt) for elt in [self.id, self.name])
