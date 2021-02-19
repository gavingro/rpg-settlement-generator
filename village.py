from random import choice
from settlement import Settlement


class Village(Settlement):
    """
    Derived class for generating villages and hamlets of small sizes.

    In general a Village:
        - is less than 500 people, farmland, governing ruler with representative,
            usually from a noble family
        - often a branch off commission of a nearby city or town
        - often provided for from bigger settlement so they can
            focus on resource gathering
        - guards are volunteers and mostly untrained (1guard x 50pax)
        - law is undefined
        - there is some sort of religion or culture setting ideology
        - there is some sort of place for travellers to stay,
            and a small shop for general goods,
            and maybe traveling merchant in town
        - Owned by a guy, but the guy has hired  a Reeve to live there
        - no real long term rarities - that would cause a town to form
    """

    def __init__(self):
        self.name = self.get_name()
        self.water = self.get_water()
        self.resource = self.get_resource()
        self.culture = self.get_culture()
        self.noble_house = self.get_noble_house()

    # The Template

    # The attribute getter's.

    def get_name(self):
        with open("attributes/village_names.txt") as village_name_list:
            village_names = village_name_list.readlines()
            return choice(village_names)

    def get_water(self):
        with open("attributes/water_source.txt") as water_source_list:
            water_sources = water_source_list.readlines()
            return choice(water_sources)

    def get_resource(self):
        with open("attributes/resources.txt") as resource_list:
            resources = resource_list.readlines()
            return choice(resources)

    def get_culture(self):
        with open("attributes/cultures.txt") as culture_list:
            cultures = culture_list.readlines()
            return choice(cultures)

    def get_noble_house(self):
        with open("attributes/noble_house_names.txt") as noble_list:
            nobles = noble_list.readlines()
            return choice(nobles)


# Manual Testing

if __name__ == "__main__":
    test_village = Village()
    print(test_village.name)
