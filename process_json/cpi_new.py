import json
import pygal
from country_code import get_country_code

filename = 'cpi_data.json'
with open(filename) as f:
    country_cpi = {}
    cpi_data = json.load(f) # Store the file in an object.
    for cpi_dict in cpi_data:   # Iterate each dictionary set in the JSON file.
        country_name = cpi_dict['Country']
        cpi = int(cpi_dict['2015_score'])
        code = get_country_code(country_name)
        if code:
            country_cpi[code] = cpi
    print(country_cpi.items())


country_cpi_1, country_cpi_2,country_cpi_3 = {}, {}, {}
for cc, cpi_value in country_cpi.items():
    if cpi_value <= 40:
        country_cpi_1[cc] = cpi_value
    elif cpi_value <= 60:
        country_cpi_2[cc] = cpi_value
    else:
        country_cpi_3[cc] = cpi_value

print(len(country_cpi_1), len(country_cpi_2), len(country_cpi_3))
wm = pygal.maps.world.World()
wm.title = 'World CPI in 2015, by Country'
wm.add('0-40', country_cpi_1)
wm.add('40-60', country_cpi_2)
wm.add('60-99', country_cpi_3)
wm.render_to_file('world_cpi_new.svg')


