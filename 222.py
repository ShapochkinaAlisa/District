from Samples.mapapi_PG import show_map
from Samples.geocoder import get_coordinates, get_ll_span, get_nearest_object
import sys

adress = ' '.join(sys.argv[1:])
lon, lat = get_coordinates(adress)
res = get_ll_span(adress)
param1 = f'{lon},{lat}'
param2 = "&spn=3,3"
result = get_nearest_object(param1.split(','), 'district')
print(result)
show_map(ll_spn=f"ll={res[0]}&spn=0.005,0.005", add_params=f"pt={lon},{lat},pm2rdm")