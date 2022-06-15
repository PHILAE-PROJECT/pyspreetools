import random


class Filters:
    def __init__(self, name=None, price=None, taxon=None, per_page=None, sort=None):
        """

        :param name: str example : "skirt"
        :param price: list example: [10,100]
        :param taxons: list example: [1]
        :param per_page: int example 400
        :param sort: example 'price' (sorting by ascending price), '-price' (sorting by descending price
        """
        self.name = name
        self.price = price
        self.taxon = taxon
        self.per_page = per_page
        self.sort = sort
        self.properties = None

    def to_filter_dict(self):
        querystring = {}
        if self.name is not None:
            querystring['filter[name]'] = self.name
        if self.price is not None:
            querystring['filter[price]'] = str(self.price[0]) + ',' + str(self.price[1])
        if self.taxon is not None:
            querystring['filter[taxons]'] = str(self.taxon)

        if self.sort is not None:
            querystring['sort'] = self.sort

        if self.properties is not None:
            querystring['properties'] = self.properties
        return {"filter": querystring}

    def random_properties(self, available_options=None):
        if available_options is None:
            self.left_properties = ['color', 'brand', 'manufacturer', 'size']
            self.number_of_properties = random.randint(1, 1)
            self.selected_properties = random.sample(self.left_properties, k=self.number_of_properties)
            self.left_properties = list(set(self.left_properties) - set(self.selected_properties))

            available_options = {
                "color": [2, 4, 6, 9, 12, 16, 17],
                "brand": ['beta', 'zeta', 'theta', 'gamma', 'epsilon', 'delta', 'alpha'],
                "manufacturer": ['conditioned', 'jerseys', 'resiliance', 'wilson', 'wannabe'],
                "size": ['xs', 's', 'm', 'l']
            }
            self.properties = {}
            for prop in self.selected_properties:
                self.properties[prop] = random.choice(available_options[prop])
        else:
            a_o = available_options.copy()
            available_options = {}
            available_options['brand'] = a_o['brand']
            available_options['manufacturer'] = a_o['manufacturer']
            self.left_properties = available_options.keys()
            self.number_of_properties = random.randint(1, 1)
            self.selected_properties = random.sample(self.left_properties, k=self.number_of_properties)
            self.left_properties = list(set(self.left_properties) - set(self.selected_properties))
            self.properties = {}
            for prop in self.selected_properties:
                self.properties[prop] = random.choice(available_options[prop])

    def random_price(self):
        b = random.choice([True, False])
        if b:
            self.price = random.choice([[10, 100], [0, 50], [20, 30], [80, 100]])


if __name__ == '__main__':
    f = Filters('skirt', [0, 100], [1], 400, '-price')
    f.random_properties()
    print(f.properties)
