import json
import pygal
from country_code import get_country_code

filename = 'cpi.json'

with open(filename) as f:
    jurisdiction_cpi = {}
    cpi_data = json.load(f) # Store the file in the cpi_data object.
    for cpi_dict in cpi_data:   # Iterate each dictionary set in the JSON file.
        jurisdiction_name = cpi_dict['Jurisdiction']  # Assign the country name (jurisdiction) to jurisdiction_name
        cpi = cpi_dict['2015']  # Query the info in 2015.
        if cpi != '-':  # Some data is unavailable and marked as "-" in the JSON file. We will ignore these cases.
            cpi = int(cpi)  # Convert the CPI string to integers.
        code = get_country_code(jurisdiction_name)  # Get the country code of the jurisdiction.
        if code and cpi!='-':
            jurisdiction_cpi[code] = cpi    # Store the CPI for a jurisdiction.
    # The output is dict_items([('dk', 91), ('nz', 91), ('fi', 90), ('se', 89),...)
    print(jurisdiction_cpi.items())

jurisdiction_cpi_1, jurisdiction_cpi_2,jurisdiction_cpi_3 = {}, {}, {} # Define three new dictionaries to group the countries.

for cc, cpi_value in jurisdiction_cpi.items():  # cc is the key and cpi_value is the value
    if cpi_value < 40:
        jurisdiction_cpi_1[cc] = cpi_value
    elif cpi_value < 60:
        jurisdiction_cpi_2[cc] = cpi_value
    else:
        jurisdiction_cpi_3[cc] = cpi_value

print(len(jurisdiction_cpi_1), len(jurisdiction_cpi_2), len(jurisdiction_cpi_3))  # Get a summary of the number of countries in each group

wm = pygal.maps.world.World()   # Import the world map module from the pygal package.
wm.title = 'World CPI in 2015, by Country'
wm.add('0-40', jurisdiction_cpi_1)
wm.add('40-60', jurisdiction_cpi_2)
wm.add('60-99', jurisdiction_cpi_3)
wm.render_to_file('world_cpi.svg')

