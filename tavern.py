from random import choice


class Tavern:
    def __init__(self):
        self.generate_attributes()
        self.generate_template()

    def generate_attributes(self):
        self.colour = self.get_colour()
        self.symbol = self.get_symbol()
        self.structure = self.get_structure()
        self.name = self.get_name()

    def generate_template(self):
        pass

    def get_symbol(self):
        with open("attributes/symbols.txt") as symbols:
            return choice(symbols.getlines())

    def get_colour(self):
        with open("attributes/colours.txt") as colours:
            return choice(colours.getlines())

    def get_structure(self):
        with open("attributes/tavern_structures.txt") as structures:
            return choice(structures.getlines())


color = Tavern()
