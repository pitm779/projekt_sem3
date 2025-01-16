from functools import partial
from geopy.geocoders import Nominatim
import random

geolocator = Nominatim(user_agent="projekt")
reverse = partial(geolocator.reverse, language="pl")

vertical_boundaries = [51.05052, 51.128762]
horizontal_boundaries = [16.968597, 17.053558]

decimals = 14

def losowy_adres(vertical_boundaries, horizontal_boundaries, decimals):
    # vertical
    random_lat = random.uniform(vertical_boundaries[0], vertical_boundaries[1]) 
    random_lat = round(random_lat, decimals)

    # horizontal
    random_long = random.uniform(horizontal_boundaries[0], horizontal_boundaries[1])
    random_long = round(random_long, decimals)

    result = reverse(f"{random_lat}, {random_long}")
    return [x.strip() for x in result.address.split(",")]

def generowanie_adresow(liczba_pracownikow, liczba_klientow):
    result = []
    for _ in range(liczba_klientow+liczba_pracownikow):
        adres = losowy_adres(vertical_boundaries, horizontal_boundaries, decimals)
        while(len(adres) != 7):
            adres = losowy_adres(vertical_boundaries, horizontal_boundaries, decimals)
        
        ulica = adres[1]
        numer = str(round(random.uniform(1, 50), 0))
        kod_pocztowy = adres[-2]
        miasto = adres[3]

        result.append([ulica + " " + numer, kod_pocztowy, miasto])

    return result