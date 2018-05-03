import pygal.maps
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    for code, name in COUNTRIES.items():  # COUNTRIES.items() returns the full list of country names and their corresponding country codes.
        if name == country_name:
            return code
        # Some country names in the pygal world map module do not match those in the JSON file and we need to include these country codes.
        elif name == "Russian Federation" and country_name == "Russia":
            return code
        elif name == "Taiwan (Republic of China)" and country_name == "Taiwan":
            return code
        elif name == "Korea, Republic of" and country_name == "Korea (South)":
            return code
        elif name == "Korea, Democratic People\'s Republic of" and country_name == "Korea (North)":  # Need to escape special characters.
            return code
        elif name == "Iran, Islamic Republic of" and country_name == "Iran":
            return code
        elif name == "Lao People\'s Democratic Republic" and country_name == "Laos":
            return code
        elif name == "Bolivia, Plurinational State of" and country_name == "Bolivia":
            return code
        elif name == "Congo, the Democratic Republic of the" and country_name == "Congo Republic":
            return code
        elif name == "Congo, the Democratic Republic of the" and country_name == "Congo Republic":
            return code
        elif name == "Libyan Arab Jamahiriya" and country_name == "Libya":
            return code
        elif name == "Macedonia, the former Yugoslav Republic of" and country_name == "The FYR of Macedonia":
            return code
        elif name == "Syrian Arab Republic" and country_name == "Syria":
            return code
        elif name == "Tanzania, United Republic of" and country_name == "Tanzania":
            return code
        elif name == "Venezuela, Bolivarian Republic of" and country_name == "Venezuela":
            return code
        elif name == "United States" and country_name == "USA":
            return code
    return None



