def mask_persons(persons):

    masked_persons = []

    for person in persons:

        name = person["nimi"]
        email = person["email"]
        phone = person["puhelin"]

        email_osat = email.split('@')
        email_masked = email_osat[0][0] + "x" * (len(email_osat[0]) - 1) + "@" + email_osat[1]

        # Maskeeraa puhelinnumero korvaamalla kaikki numerot "x"-merkeillä

        phone_masked = phone[:3] + "x" * (len(phone) -3)
        masked_person = {"nimi": name, "email": email_masked, "puhelin": phone_masked}
        masked_persons.append(masked_person)

    return masked_persons

persons = [
    
    {"nimi": "Matti Meikäläinen", "email": "matti.meikalainen@example.com", "puhelin": "0501234567"},
    {"nimi": "Liisa Laulaja", "email": "liisa.laulaja@example.com", "puhelin": "0407654321"}
]

masked_persons = mask_persons(persons)
for henkilo in masked_persons:

    print(henkilo)