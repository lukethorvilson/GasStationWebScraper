from geopy.geocoders import Nominatim
from citipy import citipy
import time
import re
import numbers

app = Nominatim(user_agent="GetLoc")

# https://thepythoncode.com/article/get-geolocation-in-python
def get_location_coords(lat, long, language="en"):
    if isinstance(lat, numbers.Real) and isinstance(long, numbers.Real):
        coordinates = f"{lat}, {long}"
        time.sleep(1)
        try:
            return app.reverse(coordinates, language=language).raw
        except:
            return get_location_coords(lat, long)

def get_location_city(city):
    data =  app.geocode(city).raw
    return re.split(", ", data["display_name"])

def get_nearest_city(lat, long):
    nearest_city = citipy.nearest_city(lat, long)
    return nearest_city.city_name.replace(" ", "-")

