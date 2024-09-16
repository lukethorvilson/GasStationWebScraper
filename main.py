import requests
from bs4 import BeautifulSoup
from lxml import etree 
from location import get_location_coords, get_location_city, get_nearest_city


# retrieves the response of the page in gas buddy so we can retrieve the data applicable to location
def get_content_coords(lat, long):
    # (may need this at some point in the future) location_data = get_location_coords(lat, long)
    url = f'https://www.bing.com/maps?q=gas+stations+near+me&FORM=HDRSC6&cp={lat}%7E{long}&lvl=13.0'
    try:
        response = requests.get(url)
        
        return response
    except:
        print("Error")


response = get_content_coords(47.4817446, -122.7215600)
print(response.content)
