import hashlib
import random

# Luottokorttinumerot
luottokortit = ["1234-5678-9012-3456", "2345-6789-0123-4567"]

def tokenisoi_kortti(numero):
    # Luo satunnainen suola (salt)
    suola = str(random.randint(0, 99999999)).zfill(8)
    # Yhdistä korttinumero ja suola
    tieto = numero + suola
    # Luo SHA-256-tiiviste (hash) yhdistetystä tiedosta
    tiiviste = hashlib.sha256(tieto.encode()).hexdigest()[:8]
    return tiiviste

for kortti in luottokortit:
    token = tokenisoi_kortti(kortti)
    print(f"{kortti} -> {token}")
