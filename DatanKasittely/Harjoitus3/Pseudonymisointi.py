#Pseudonymisointi

import hashlib

def pseudonymize_names(names):

    pseudonyms = []

    for name in names:

        sha256 = hashlib.sha256()
        sha256.update(name.encode('utf-8'))
        pseudonym = sha256.hexdigest()
        pseudonyms.append(f"{name} -> {pseudonym}...")

    return pseudonyms

 
nimet = ["Matti Meikäläinen", "Liisa Laulaja", "Juha Jokunen"]
pseudonyms = pseudonymize_names(nimet)

for pseudonym in pseudonyms:

    print(pseudonym)