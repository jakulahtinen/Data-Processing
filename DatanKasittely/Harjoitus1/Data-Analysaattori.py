# 1. CSV-tiedoston lukeminen ja tulostaminen. 

import csv
import matplotlib.pyplot as plt

with open('exampleData.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

# 2. Lasketaan tiedostosta löytyvien henkilöiden keski-ikä.

average = []
with open ("exampleData.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

#Keski-iän laskeminen: 
    for row in reader:
        average.append(float(row["ika"]))

print("Keski-ikä on: ", sum(average) / len(average))


# 3. Lasketaan kuinka monta kertaa kukin ammatti esiintyy ja
# tulostetaan analyysin tulos muodossa "[ammatti]: x kertaa"

tiedosto_nimi = "exampleData.csv"

# Tyhjä tila laskurille:
ammattien_laskuri = {}

# Käydään tiedosto läpi for-loopilla ja lasketaan esiintymiskerrat:
with open(tiedosto_nimi, newline='', encoding='utf-8') as csv_tiedosto:
    lukija = csv.DictReader(csv_tiedosto)
    for rivi in lukija:
        ammatti = rivi["ammatti"]
        if ammatti in ammattien_laskuri:
            ammattien_laskuri[ammatti] += 1
        else:
            ammattien_laskuri[ammatti] = 1


for ammatti, lkm in ammattien_laskuri.items():
    print(f"{ammatti}: {lkm} kertaa")

# 4. Visualisoidaan data.


# Luetaan CSV-tiedosto
tiedosto_nimi = "exampleData.csv"

# Luodaan tyhjä sanakirja ammattien laskemista varten
ammattien_laskuri = {}

# Avataan CSV-tiedosto ja luetaan sen sisältö
with open(tiedosto_nimi, newline='', encoding='utf-8') as csv_tiedosto:
    lukija = csv.DictReader(csv_tiedosto)
    for rivi in lukija:
        ammatti = rivi["ammatti"]
        if ammatti in ammattien_laskuri:
            ammattien_laskuri[ammatti] += 1
        else:
            ammattien_laskuri[ammatti] = 1

# Erotellaan ammattien nimet ja esiintymiskerrat
ammattien_nimet = list(ammattien_laskuri.keys())
esiintymiskerrat = list(ammattien_laskuri.values())

# Luodaan pylväsgrafiikka
plt.figure(figsize=(10, 6))
plt.bar(ammattien_nimet, esiintymiskerrat, color='skyblue')
plt.xlabel('Ammatti')
plt.ylabel('Esiintymiskerrat')
plt.title('Ammattien esiintymiskerrat')
plt.xticks(rotation=45, ha="right")

# Näytetään grafiikka
plt.tight_layout()
plt.show()
