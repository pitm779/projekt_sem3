import numpy as np #pobrać
import pandas as pd #pobrać
from unidecode import unidecode #pobrać
from faker import Faker  #pobrać
import random
import datetime
from functools import partial
from geopy.geocoders import Nominatim #pobrać
import random

fake = Faker()

imiona = pd.read_csv('lista_imion.csv')
nazwiska = pd.read_csv('lista_nazwisk.csv')

def generowanie_imiona_nazwiska_email_addressid(liczba_klientów, liczba_pracowników):
    lista = []
    gen_imiona_płeć = imiona.sample(n = liczba_klientów+liczba_pracowników, replace=True, weights=imiona['CZĘSTOŚĆ'])[['IMIĘ_PIERWSZE', 'PŁEĆ']]
    gen_numery_email = np.random.choice(999, liczba_klientów+liczba_pracowników, replace=False)
    nazwiska_męskie = nazwiska.query("PŁEĆ == 'MĘŻCZYZNA'")
    nazwiska_żeńskie = nazwiska.query("PŁEĆ == 'KOBIETA'")
    gen_address_id = np.random.choice(range(1,liczba_klientów+liczba_pracowników+1), liczba_klientów+liczba_pracowników, replace=False)

    for i in range(liczba_klientów + liczba_pracowników):
        imie_płeć = gen_imiona_płeć.iloc[i]
        if imie_płeć['PŁEĆ'] == 'MĘŻCZYZNA':
            nazwisko = nazwiska_męskie.sample(n = 1, weights = nazwiska_męskie['CZĘSTOŚĆ']).iloc[0]
        else:
            nazwisko = nazwiska_żeńskie.sample(n = 1, weights = nazwiska_żeńskie['CZĘSTOŚĆ']).iloc[0]
        first_name = imie_płeć['IMIĘ_PIERWSZE']
        last_name = nazwisko['Nazwisko aktualne']
        address_id = gen_address_id[i]
        email = f"{unidecode(first_name[0]).lower()}{unidecode(last_name).lower()}{gen_numery_email[i]}@gmail.com"
        lista.append((first_name, last_name, address_id, email))
    return lista


def generowanie_customers(liczba_klientów, gen_imiona_nazwiska_email_addressid):

    lista_customers = []
    gen_numery_telefonu = random.sample(range(500000000,899999999), liczba_klientów*2)

    for i in range(liczba_klientów):
        birth_date = fake.date(end_datetime = '-15y')
        phone_number = gen_numery_telefonu[2*i]
        ICE_number = gen_numery_telefonu[2*i+1] #na pewno będą różne numery u wszystkich

        lista_customers.append((i+1,  gen_imiona_nazwiska_email_addressid[i][2],gen_imiona_nazwiska_email_addressid[i][0], gen_imiona_nazwiska_email_addressid[i][1], gen_imiona_nazwiska_email_addressid[i][3], phone_number, birth_date, ICE_number)) #i+1 to id klienta
    return lista_customers

def generowanie_costs():
    lista_kosztów = []

    indeksy_wycieczek = range(1, 19)

    koszty = {'id_wycieczek': indeksy_wycieczek, 
              'Transport': [np.random.randint(4400, 4700), np.random.randint(7700, 8000), np.random.randint(7000, 7300), np.random.randint(4300, 4600), np.random.randint(380, 480), np.random.randint(70, 100), np.random.randint(3300, 3700), np.random.randint(80, 100), np.random.randint(1000, 1300), np.random.randint(3300, 3700), np.random.randint(40, 50), np.random.randint(4300, 4600), np.random.randint(12200, 12500), np.random.randint(1100, 1400), np.random.randint(560, 660), np.random.randint(160, 200), np.random.randint(3400, 3700), np.random.randint(1050, 1350)], 
              'Zakwaterowanie': [], 
              'Opłata instruktora/przewodnika': []}
    
    for i in range(0, 18): #tworzenie cen zakwaterowania
        if koszty['Transport'][i] <= 100:
            koszty['Zakwaterowanie'].append(koszty['Transport'][i]*3)
        elif 100 < koszty['Transport'][i] <= 500:
            koszty['Zakwaterowanie'].append(koszty['Transport'][i]*2)
        elif 500 < koszty['Transport'][i] <= 1000: 
            koszty['Zakwaterowanie'].append(koszty['Transport'][i])
        else:
            koszty['Zakwaterowanie'].append(round(koszty['Transport'][i]*0.5))
    
    for i in range(0, 18): #tworzenie opłaty dla przewodnika
        if koszty['Transport'][i] <= 100:
            koszty['Opłata instruktora/przewodnika'].append(koszty['Transport'][i]*6)
        elif 100 < koszty['Transport'][i] <= 500:
            koszty['Opłata instruktora/przewodnika'].append(koszty['Transport'][i]*3)
        elif 500 < koszty['Transport'][i] <= 1000: 
            koszty['Opłata instruktora/przewodnika'].append(koszty['Transport'][i]*2)
        else:
            koszty['Opłata instruktora/przewodnika'].append(round(koszty['Transport'][i]*1.2))

    for i in range(0, 18):
        j = 0
        names = ['Transport', 'Zakwaterowanie', 'Opłata instruktora/przewodnika']
        while j <= 2:
            lista_kosztów.append((koszty['id_wycieczek'][i], list(koszty.keys())[j+1], koszty[names[j]][i]))
            j += 1

    return lista_kosztów


tabela_cost = generowanie_costs()


def generowanie_trips(tabela_cost):
    lista_trips = []

    nazwy = [
                ['Trekking na Kilimandżaro', 1, 'Wyrusz na przygodę życia i zdobądź najwyższy szczyt Afryki! ', True],
                ['Polowanie na Zorzę Polarną w Arktyce', 1, 'Wyrusz na niezapomnianą wyprawę za koło podbiegunowe i stań twarzą w twarz z jednym z najpiękniejszych zjawisk natury!', True],
                ['Podwodne Odkrycia w Rafie Koralowej', 1, 'Zanurz się w krystalicznych wodach Australii i odkryj cuda Wielkiej Rafy Koralowej.', True],
                ['Tajemnicze Zakątki Machu Picchu', 2, 'Odkryj magiczne Machu Picchu – zaginione miasto Inków skryte w chmurach peruwiańskich Andów.', True],
                ['Podróż w Czasie - Odkrywanie Pompejów', 2, 'Przenieś się do czasów starożytnego Rzymu i odkryj Pompeje – miasto zatrzymane w czasie przez erupcję Wezuwiusza.', True],
                ['Gotyckie Zamki Dolnego Śląska', 2, 'Odkryj majestatyczne gotyckie zamki Dolnego Śląska – pełne tajemnic, legend i średniowiecznego uroku.', False],
                ['Kosmiczna Przygoda w Centrum NASA', 3, 'Wyrusz w fascynującą podróż w kosmos, nie opuszczając Ziemi!', True],
                ['Raj w Parku Rozrywki Energylandia', 3, 'Przygotuj się na dzień pełen emocji i radości w największym parku rozrywki w Polsce!', False],
                ['Jurassic Park Live', 3, 'Przenieś się miliony lat wstecz i spotkaj gigantyczne dinozaury w pełnej skali!', True],
                ['Warsztaty Jogi w Himalajach', 4, 'Zanurz się w duchowej harmonii i odkryj wewnętrzny spokój w sercu najwyższych gór świata.', True],
                ['Sanktuarium na Jasnej Górze', 4, 'Pielgrzymka na Jasną Górę to wyjątkowa okazja do wzmocnienia wiary i odnalezienia duchowego spokoju.', False],
                ['Rytuał w szamańskiej wiosce w Peru', 4, 'Wyrusz w duchową podróż do serca peruwiańskiej Amazonii, gdzie czeka na Ciebie niezwykły rytuał ayahuaski prowadzony przez lokalnych szamanów.', True],
                ['Surfing na Plażach Australii', 5, 'Poczuj adrenalinę i złap idealną falę na rajskich plażach Byron Bay!', True],
                ['Wspinaczka na Ścianę Trolla w Norwegii', 5, 'Zmierz się z jedną z najbardziej spektakularnych formacji skalnych w Europie – legendarną Ścianą Trolla!', True],
                ['Rowerem przez Holandię', 5, 'Przemierzaj malownicze holenderskie krajobrazy na rowerze, mijając pola tulipanów w pełnym rozkwicie, urokliwe wiatraki i kanały.', True],
                ['Koncerty w Operze Wiedeńskiej', 6, 'Wejdź do jednej z najpiękniejszych sal koncertowych świata i zanurz się w dźwiękach muzyki klasycznej na żywo.', True],
                ['Karnawał w Rio de Janeiro', 6, 'Poczuj niesamowitą atmosferę najsłynniejszego karnawału na świecie!', True],
                ['Karnawał w Wenecji', 6, 'Weź udział w najpiękniejszym i najbardziej eleganckim karnawale Europy!', True]
        ]

    pierwsza_data = fake.date_between(start_date=datetime.date.today() - datetime.timedelta(days = 365+14), end_date = '-1y') #powstanie pierwszej wycieczki w ofercie

    koszty = pd.DataFrame(tabela_cost, columns=['trip_id', 'name', 'amount'])
    suma_kosztów = koszty[['trip_id', 'amount']].groupby('trip_id').sum()


    for i in range(0, 18):
        creation_date = pierwsza_data + datetime.timedelta(days = i*21) #co 3 tygodnie publikujemy nową wycieczkę, dzięki temu daty nie będą się nakładać
        begin_date = creation_date + datetime.timedelta(days = 67) 
        end_date = begin_date + datetime.timedelta(days = 7) #wycieczka trwa tydzień
        margin = suma_kosztów.iloc[i]['amount']*1.2
        trip_name = nazwy[i][0]
        category_id = nazwy[i][1]
        description = nazwy[i][2]
        abroad = nazwy[i][3]
        lista_trips.append((i+1, category_id, trip_name, margin, begin_date, end_date, abroad, creation_date, description)) # i to trip_id, może max_spots do usunięcia (albo zamiast tego min_spots)??
    return lista_trips

tabela_trips = generowanie_trips(tabela_cost)


def generowanie_payment(liczba_pracowników, liczba_klientów, liczba_wierszy, tabela_trips): #liczba wierszy to będzie liczba klientów, którzy kupili 2 lub więcej wycieczek
    lista_payment = []

    trips = tabela_trips 
    
    customers_id = np.concatenate((random.sample(range(1, liczba_klientów+1), liczba_klientów), np.random.choice(range(1, 101), liczba_wierszy, replace=True))) #liczba rekordów, 
    #100 to liczba klientów ze zmiennej tabela_customers, można zautowatyzować, ale nie trzeba; w pierwszym losowaniu mamy zapewnione, że każdy klient wystąpi w tabeli
    trips_id = np.random.choice(range(1,trips[-1][0]+1), liczba_klientów + liczba_wierszy, replace=True) #losowanie id kupionych wycieczek, 100 + liczba_wierszy to liczba wierszy

    for i in range(liczba_klientów+liczba_wierszy):
        customer_id = customers_id[i] 
        trip_id = trips_id[i]
        payment_date = fake.date_between(start_date = trips[trip_id - 1][7], end_date = trips[trip_id - 1][4] - datetime.timedelta(days=7)) #end_date to deadline, 4 i 7 to indeksy begin_date i creation_date
        amount = np.random.choice(range(1, 5), 1)[0]
        staff_id = np.random.randint(1, liczba_pracowników+1)
        lista_payment.append([i+1, customer_id, staff_id, trip_id, payment_date, amount]) #i+1 to indeks zapłaty
    return lista_payment


def generowanie_staff(liczba_klientów, liczba_pracowników, gen_imiona_nazwiska_email_addressid):
    lista_staff = []

    for i in range(liczba_pracowników):
        salary = np.random.randint(4666, 7500)
        hire_date = fake.date_between(start_date=datetime.date.today() - datetime.timedelta(days = 365+21), end_date = datetime.date.today() - datetime.timedelta(days = 365+21))
        birth_date = fake.date(end_datetime='-18y')
        lista_staff.append((gen_imiona_nazwiska_email_addressid[liczba_klientów + i][2], 
                            gen_imiona_nazwiska_email_addressid[liczba_klientów + i][0], 
                            gen_imiona_nazwiska_email_addressid[liczba_klientów + i][1], salary,
                            gen_imiona_nazwiska_email_addressid[liczba_klientów + i][3], 
                            hire_date, birth_date))
    return lista_staff
    

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

def generowanie_adresow(liczba_pracowników, liczba_klientów):
    result = []
    for _ in range(liczba_klientów+liczba_pracowników):
        adres = losowy_adres(vertical_boundaries, horizontal_boundaries, decimals)
        while(len(adres) != 7):
            adres = losowy_adres(vertical_boundaries, horizontal_boundaries, decimals)
        
        ulica = adres[1]
        numer = str(int(round(random.uniform(1, 50), 0)))
        kod_pocztowy = adres[-2]
        miasto = adres[3]

        result.append([ulica + " " + numer, kod_pocztowy, miasto])

    return result

