import numpy as np #pobrać
import pandas as pd #pobrać
from unidecode import unidecode #pobrać

imiona = pd.read_csv('lista_imion.csv')
nazwiska = pd.read_csv('lista_nazwisk.csv')

def generowanie_imie_nazwisko_mail(liczba_wierszy):

    lista_imiona_nazwiska = []
    gen_imiona_płeć = imiona.sample(n = liczba_wierszy, replace=True, weights=imiona['CZĘSTOŚĆ'])[['IMIĘ_PIERWSZE', 'PŁEĆ']]
    gen_numery_email = np.random.choice(999, liczba_wierszy, replace=False)
    nazwiska_męskie = nazwiska.query("PŁEĆ == 'MĘŻCZYZNA'")
    nazwiska_żeńskie = nazwiska.query("PŁEĆ == 'KOBIETA'")

    for i in range(liczba_wierszy):
        imie_płeć = gen_imiona_płeć.iloc[i]
        if imie_płeć['PŁEĆ'] == 'MĘŻCZYZNA':
            nazwisko = nazwiska_męskie.sample(n = 1, weights = nazwiska_męskie['CZĘSTOŚĆ']).iloc[0]
        else:
            nazwisko = nazwiska_żeńskie.sample(n = 1, weights = nazwiska_żeńskie['CZĘSTOŚĆ']).iloc[0]
        email = f"{unidecode(imie_płeć['IMIĘ_PIERWSZE'][0]).lower()}{unidecode(nazwisko['Nazwisko aktualne']).lower()}{gen_numery_email[i]}@gmail.com"
        lista_imiona_nazwiska.append((imie_płeć['IMIĘ_PIERWSZE'], nazwisko['Nazwisko aktualne'], email))
    return lista_imiona_nazwiska

print(generowanie_imie_nazwisko_mail(10))

