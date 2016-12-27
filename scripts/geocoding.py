from geopy.geocoders import Nominatim
from geopy.distance import vincenty

# >>> from geopy.geocoders import Nominatim
# >>> geolocator = Nominatim()
# >>> location = geolocator.geocode("175 5th Avenue NYC")
# >>> print(location.address)
# Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
# >>> print((location.latitude, location.longitude))
# (40.7410861, -73.9896297241625)
# >>> print(location.raw)
# {'place_id': '9167009604', 'type': 'attraction', ...}

def geo(loc):
    """ Input a string of loc"""
    geolocator = Nominatim()
    location = geolocator.geocode(loc)
    return location.longitude, location.latitude

def rev_geo(lon, lat):
    """Use geopy to do reverse geocoding
    
    Becarefule of the output format as geopy has multiple sources and can have many format.
    """
    geolocator = Nominatim()
    location = geolocator.reverse(str(lat) + ", " + str(lon))
    return location.raw

def distance(lon1, lat1, lon2, lat2):    
    newport_ri = (lon1, lat1)
    cleveland_oh = (lon1, lat2)
    return vincenty(newport_ri, cleveland_oh).kilometers