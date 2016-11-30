import requests
from bs4 import BeautifulSoup

def reverse_geocoding(lat, lng):
    reverse_geocoding_url = 'http://nominatim.openstreetmap.org/search.php'
    payload = {'q':lat+', '+lng}
    get_url = requests.get(reverse_geocoding_url, params=payload, timeout=30)
    soup = BeautifulSoup(get_url.text,"lxml")
    return (soup.select('div[id=content] span[class=name]')[0].string)

def parse_country(string):
    return string.split(', ')[-1]