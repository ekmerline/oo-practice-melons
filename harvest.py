############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

# musk1 = MelonType(
#     "musk",
#     "Muskmelon",
#     1998,
#     "green",
#     True,
#     True
# )

# musk1.code

# musk1.update_code("muskier")
#musk1.new_code is now "muskier"
#musk1.code is still "musk"
    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)
        
    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    casaba.add_pairing("mint")
    casaba.add_pairing("strawberries ")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    crenshaw.add_pairing("proscuitto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # Fill in the rest
    for melon_type in melon_types:
        if len(melon_type.pairings) > 0:
            print(f"{melon_type.name} pairs with")
            for pairing in melon_type.pairings:
                print(f"- {pairing}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_dict = {}
    # Fill in the rest
    for melon_type in melon_types:
        melon_type_dict[melon_type.code] = melon_type
        
    return melon_type_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by
        
    def is_sellable(self):
        if self.color_rating > 4 and self.shape_rating > 5 and  self.harvested_from != 3:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons_by_id = make_melon_type_lookup(melon_types)
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    return [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        sellable_status = "(CAN BE SOLD)" if melon.is_sellable() else "(NOT SELLABLE)"

        print(f"Harvest by {melon.harvested_by} from Field {melon.harvested_from} {sellable_status}")


melon_types = make_melon_types()
print_pairing_info(melon_types)
melons = make_melons(melon_types)
get_sellability_report(melons)
