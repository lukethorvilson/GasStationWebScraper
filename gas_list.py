from bs4 import BeautifulSoup
from lxml import etree
import requests

# get the page we are scraping the gas station data from
webpage = requests.get("https://en.wikipedia.org/wiki/List_of_gas_station_chains_in_North_America")

soup = BeautifulSoup(webpage.content, "html.parser")

dom = etree.HTML(str(soup))

station_list_el = dom.xpath("/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[2]/ul")[0]

stations_el_text = [child.text for child in station_list_el.iter()]

gas_list = []
for station in stations_el_text:
    if station != None:
        gas_list.append(station)
