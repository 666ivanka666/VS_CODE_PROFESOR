""" counter = 1

while True:
    ime = input("Unesite ime kontakta: \t")
    prezime = input("Unesite prezime kontakta: \t")
    telefon = input("Unesite broj telefona kontakta: \t")

    # 1. otvaranje konekcije
    try:
        file_writer = open("adresar.txt", "a")

        # 2. pisanje u datoteku
        file_writer.write(f"{counter};{ime};{prezime};{telefon}\n")
        counter += 1
    except:
        print("Dogodila se greška")

    finally:
        # 3. zatvaranje konekcije
        file_writer.close()

    ponovi_unos = input("Želite li unijeti novi kontakt? (y/n)")
    if ponovi_unos.lower() != 'y':
        break """

""" counter = 1
while True:
    ime = input("Unesite ime kontakta: \t")
    prezime = input("Unesite prezime kontakta: \t")
    telefon = input("Unesite broj telefona kontakta: \t")

    try:
        with open("adresar.txt", "a") as file_writer:
            # file_writer = open("adresar.txt", "a")

            # na isti način zapišemo u datoteku
            file_writer.write(f"{counter};{ime};{prezime};{telefon}\n")
            counter += 1

            # file_writer.close() nam ne treba jer Python to napravi automatski
            # nakon što izvrši sve unutar with bloka
    
    except Exception as e:
        print(f"Dogodila se greška: {e}")
    
    ponovi_unos = input("Želite li unijeti novi kontakt? (y/n)")
    if ponovi_unos.lower() != 'y':
        break  """


class Kontakt:
    def __init__(self, id_kontakta, ime, prezime, broj):
        self.id_kontakta = id_kontakta
        self.ime = ime
        self.prezime = prezime
        self.broj = broj
    
    def ispisi_kontakt(self):
        print(f"ID: {self.id_kontakta}\t Ime: {self.ime}\t Prezime: {self.prezime}\t Broj: {self.broj}")

lista_kontakata = []

try:
    with open("adresar.txt", "r") as file_reader:
        for red in file_reader:
            red = red.rstrip()
            dijelovi = red.split(";")
            kontakt = Kontakt(dijelovi[0], dijelovi[1], dijelovi[2], dijelovi[3])
            lista_kontakata.append(kontakt)
except Exception as e:
    print(f"Dogodila se greška: {e}") 

for kontakt in lista_kontakata:
    kontakt.ispisi_kontakt()
