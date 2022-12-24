#importare pymongo
import pymongo
from pymongo import MongoClient
import uuid

#loggare come admin nel cluster
client = MongoClient('mongodb+srv://admin:uniteca123@cluster0.znfxrbr.mongodb.net/test')

#entra nel database uniteca e assegno ad una variabile
uniteca = client["uniteca"]

#entra nella collection "Libri"
mycol = uniteca["libri"]


#aggiunge o sovrascrive elementi nella collection
mylist = [
  { "_id": uuid.uuid4().hex, "name": "Il signore degli anelli", "n.writer": "J. R. R. Tolkien", "tag": "+adventure +cult", "ann.d.p": "1954", "editore": "Caio", "disponibile": "1"},
  { "_id": uuid.uuid4().hex, "name": "Il mio bambino difficile", "n.writer": "Hoffman", "tag": "+int +study", "ann.d.p": "1982", "editore": "Mondadori", "disponibile": "1"},
  { "_id": uuid.uuid4().hex, "name": "harry potter", "n.writer": "J. K. Rowling", "tag": "+fantasy +mag", "ann.d.p": "2002", "editore": "Feltrinelli", "disponibile": "1"},
  { "_id": uuid.uuid4().hex, "name": "Fisica avanzata II", "n.writer": "Albert", "tag": "+study +science", "ann.d.p": "2021", "editore": "Caio", "disponibile": "1"},
  { "_id": uuid.uuid4().hex, "name": "C for dummys", "n.writer": "K. T. Mellown", "tag": "+comedy +science", "ann.d.p": "2014", "editore": "Feltrinelli", "disponibile": "1"}
]

x = mycol.insert_many(mylist)

#stampa tutti gli elementi della collection
print ("elementi presenti in Libri")
for x in mycol.find():
  print(x)



#Parte utenti_______

#entra nella collection "utenti"
utenti = uniteca["utenti"]

#aggiunge o sovrascrive elementi nella collection
user = [
    {"_id": uuid.uuid4().hex, "Name": "Nicola", "Surname": "Cirillo", "Email": "nicolacirillo@studenti.universita.it", "Password": "nicola", "Type": "admin"},
    {"_id": uuid.uuid4().hex, "Name": "Filippo", "Surname": "Spitaletta", "Email": "filippospitaletta@studenti.universita.it", "Password": "campania", "Type": "admin"},
    {"_id": uuid.uuid4().hex, "Name": "Pasquale", "Surname": "Ferrandino", "Email": "pasqualeferrandino@studenti.universita.it", "Password": "pasquale", "Type": "admin"},
    {"_id": uuid.uuid4().hex, "Name": "Mario", "Surname": "Esposito", "Email": "mariorossi@studenti.universita.it", "Password": "mario", "Type": "user"},
    {"_id": uuid.uuid4().hex, "Name": "Marcello", "Surname": "Bianchi", "Email": "angelobianchi@studenti.universita.it", "Password": "marcello", "Type": "user"}
       ]

x = utenti.insert_many(user)

#stampa tutti gli elementi della collection
print ("elementi presenti in Libri")
for x in mycol.find():
  print(x)




#Parte reservation_____

reservation = uniteca["posti"]

#aggiunge o sovrascrive elementi nella collection

posti = [
            {"disponibilità_tot": "100", "prenotati": "1", "data": "2022, 6, 1"}
            
        ]

x = reservation.insert_many(posti)



#stampa tutti i database connessi al cluster
print(client.list_database_names())

#stampa tutte le collection del database
print(uniteca.list_collection_names())
