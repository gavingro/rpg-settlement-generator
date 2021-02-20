from random import choice
from settlement import Settlement
from tavern import Tavern


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

    def generate_attributes(self):
        self.name = self.get_name()
        self.water = self.get_water()
        self.resource = self.get_resource()
        self.culture = self.get_culture()
        self.noble_house = self.get_noble_house()
        self.power_player = self.get_power_player()
        self.ideology = self.get_ideology()
        self.profession = self.get_profession()
        self.landmark1 = self.get_landmark()
        self.landmark2 = self.get_landmark()
        self.nearby_town = self.get_nearby_town()
        self.oddity = self.get_oddity()

    # The Template
    # TODO: Add template
    def generate_template(self):
        pass

    # The attribute getter's.

    def get_name(self):
        with open("attributes/village_names.txt") as village_names:
            return choice(village_names.readlines())

    def get_water(self):
        with open("attributes/water_source.txt") as water_sources:
            return choice(water_sources.readlines())

    def get_resource(self):
        with open("attributes/resources.txt") as resources:
            return choice(resources.readlines())

    def get_culture(self):
        with open("attributes/cultures.txt") as cultures:
            return choice(cultures.readlines())

    def get_noble_house(self):
        with open("attributes/noble_house_names.txt") as nobles:
            return choice(nobles.readlines())

    def get_power_player(self):
        with open("attributes/power_players.txt") as power_players:
            return choice(power_players.readlines())

    # TODO: replace with proper ideology generator and class.
    def get_ideology(self):
        with open("attributes/ideologies.txt") as ideologies:
            return choice(ideologies.readlines())

    def get_profession(self):
        with open("attributes/professions.txt") as professions:
            return choice(professions.readlines())

    def get_landmark(self):
        with open("attributes/landmarks.txt") as landmarks:
            return choice(landmarks.readlines())

    def get_nearby_town(self):
        with open("attributes/town_names.txt") as nearby_towns:
            return choice(nearby_towns.readlines())

    def get_oddity(self):
        with open("attributes/oddities.txt") as oddities:
            return choice(oddities.readlines())

    def get_tavern(self):
        pass


# Manual Testing

if __name__ == "__main__":
    test_village = Village()
    print(test_village.name)
