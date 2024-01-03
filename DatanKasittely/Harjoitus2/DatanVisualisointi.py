# 1. Luetaan JSON-tiedosto ######
import json
import matplotlib.pyplot as plt

# Avataan JSON-tiedosto
with open('todos.json', 'r') as tiedosto:
    tiedot = json.load(tiedosto)

# Ensimmäinen tehtävä ja sen tiedot:
ensimmainen_tehtava = tiedot[0]

# Tulostetaan ensimmäinen tehtävä:
print (ensimmainen_tehtava)


# 2. Analysoi Dataa ######

# Tehtävät yhteensä:
tehtavat = len(tiedot)

# Lasketaan valmiit tehtävät:
valmiit_tehtavat = sum(1 for tehtava in tiedot if tehtava["completed"])

#Tulostetaan tulokset
print("Tehtävien määrä: ", tehtavat)
print("Valmiiden tehtävien määrä: ", valmiit_tehtavat)


# 3. Visualisoi Dataa ###### Pylväsdiagrammi

# Etsitään käyttäjien tehtävien määrä:
tehtavien_maara_per_kayttaja = {}
for tehtava in tiedot:
    kayttaja_id = tehtava["userId"]
    if kayttaja_id in tehtavien_maara_per_kayttaja:
        tehtavien_maara_per_kayttaja[kayttaja_id] +=1
    else:
        tehtavien_maara_per_kayttaja[kayttaja_id] = 1

# Erotetaan ID:t ja tehtävien määrät:
kayttajan_idt = list(tehtavien_maara_per_kayttaja.keys())
tehtavien_maarat = list(tehtavien_maara_per_kayttaja.values())

# Piirretän pylväsdiagrammi:
plt.bar(kayttajan_idt, tehtavien_maarat)
plt.xlabel("Käyttäjän ID")
plt.ylabel("Tehtävien määrä")
plt.title("Tehtävien päärä per käyttäjä")
plt.show()

# 3. Visualisoi Dataa ###### Piirakkadiagrammi

# Lasketaan keskeneräiset tehtävät:

valmiit_tehtavat = 0
tehtavat_kesken = 0

for tehtava in tiedot:
    if tehtava["completed"]:
        valmiit_tehtavat += 1
    else:
        tehtavat_kesken += 1

# Tiedot piirakkadiagrammiin:

tehtavien_maarat = [valmiit_tehtavat, tehtavat_kesken]
tehtavien_kuvaus = ["Valmiit tehtävät", "Keskeneräiset tehtävät"]
varjostus = (0.1, 0)

# Piirretään piirakkadiagrammi:

plt.pie(tehtavien_maarat, labels=tehtavien_kuvaus, autopct='%1.1f%%', shadow=True, explode=varjostus)
plt.axis('equal')  # Tämä pitää ympyrän muotoisena
plt.title("Tehtävien tila")
plt.show()


# 4. Analysoi ja visualisoi tehtävien valmistumista käyttäjäkohtaisesti ######

valmiit_tehtavat_kayttaja = {}

# Tehtävät käydään läpi for-loopilla
for tehtava in tiedot:
    kayttaja_id = tehtava["userId"]
    if tehtava["completed"]:
        if kayttaja_id in valmiit_tehtavat_kayttaja:
            valmiit_tehtavat_kayttaja[kayttaja_id] +=1
        else:
            valmiit_tehtavat_kayttaja[kayttaja_id] = 1

kayttajan_idt = list(valmiit_tehtavat_kayttaja.keys())
valmiiden_tehtavien_maarat = list(valmiit_tehtavat_kayttaja.values())

# Piirretään pylväsdiagrammi
plt.bar(kayttajan_idt, valmiiden_tehtavien_maarat)
plt.xlabel("Käyttäjän ID")
plt.ylabel("Valmiiksi saadut tehtävät")
plt.title("Valmiiksi saadut tehtävät käyttäjittäin")
plt.show()