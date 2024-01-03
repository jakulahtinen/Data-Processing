import hashlib

def anonymize_data(people):

    anonymized_data = []

    for person in people:

        birth_year = int(person["syntymaaika"].split('-')[0])
        city_initial = person["kaupunki"][0]
        anonymized_person = {"syntymavuosi": birth_year, "kaupunki_kirjain": city_initial}
        anonymized_data.append(anonymized_person)

    return anonymized_data

henkilot = [

    {"nimi": "Matti Meikäläinen", "syntymaaika": "1990-05-15", "kaupunki": "Helsinki"},

    {"nimi": "Liisa Laulaja", "syntymaaika": "1985-12-12", "kaupunki": "Tampere"}

]

anonymized_people = anonymize_data(henkilot)
for person in anonymized_people:

    print(person)
