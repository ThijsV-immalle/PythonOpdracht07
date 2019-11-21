import sqlite3, os
 
file_name = 'leerlingen.sqlite3'
if(os.path.exists(file_name)):
        os.remove(file_name)
 
conn = sqlite3.connect(f"{file_name}")
c = conn.cursor()
 
c.execute("""CREATE TABLE leerlingen
(Id integer primary key, voornaam text, achternaam text)""")
 
c.execute("INSERT INTO leerlingen(Voornaam, Achternaam) VALUES ('Thijs','Verbelen')")
c.execute("INSERT INTO leerlingen(Voornaam, Achternaam) VALUES ('Brent', 'Verlinden')")
c.execute("INSERT INTO leerlingen(Voornaam, Achternaam) VALUES ('Arne', 'Meylemans')")
c.execute("INSERT INTO leerlingen(Voornaam, Achternaam) VALUES ('Senne', 'Weygers')")
c.execute("INSERT INTO leerlingen(Voornaam, Achternaam) VALUES ('Jarnick', 'Sas')")
c.execute("INSERT INTO leerlingen(Voornaam, Achternaam) VALUES ('Michiel', 'Dries')")
c.execute("INSERT INTO leerlingen(Voornaam, Achternaam) VALUES ('Nick', 'Van Looveren')")
c.execute("INSERT INTO leerlingen(Voornaam, Achternaam) VALUES ('Joren', 'De Rijk')")
c.execute("INSERT INTO leerlingen(Voornaam, Achternaam) VALUES ('Brent', 'Meylemans')")
c.execute("INSERT INTO leerlingen(Voornaam, Achternaam) VALUES ('Arne', 'Verlinden')")
 
print("""
*****************************************
        Dit is mijn programma!
***************************************** 
 
- Voeg een nieuwe leerling toe: N
- Lijst van leerlingen, gesorteerd op voornaam: V
- Lijst van leerlingen, gesorteerd op achteraam: A
- Verwijder leerling: X
- Verwijder leerling op basis van voornaam als deze meerdere keren voorkomt: D
""")
 
letter = input("Geef één van de bovenstaande letters:  ")