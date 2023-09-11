# Dictionary Demo

# Skapa en ny dictionary

person = {
    "name": "Ali Al Khafagy",
    "age": 28,
}
print(person)

# Hämta ett element från dictionary
print("Hej " + person['name'])
print("Du är " + str(person['age']) + '  år gammal.')#lägger man till str så konverterar man siffor.
print(f"Du är  { person['age'] }  år gammal.") #lägger man till str så konverterar man siffor.

#Referera till en nyckel dynamiskt
"""attr = input("Ange en attribut (nyckel) > ")

try:
    print(person[attr])
except KeyError: #except för felmeddelande(KeyError) när du skriver något annat än "name".
    print("Fel! Attributet existerar inte!")
"""

# Ändra värdet
person['age'] = 29
print(person)

#Lägg till ny data (Key-value-pair)/ element.
person['address'] = "Baldersväg 16"
print(person)

# Ta bort element, del står för delete.
del person['age']
print(person)

# Kopiera dict
temp = person # FEL, du skapar en ny referens.
print(temp)
print(person)
# temp och person pekar på samma object

person_copy = person.copy()
person_copy['temp2'] = "temp2"
print(person_copy)

"""del person_copy
print(person_copy) # Visar bara ibland ett felmeddelande (WIRED)

#Iteration av dict
for key in person:
    print("Key: " + key) #print key skriver ut alla värden.
    print("Value:", person[key])

#Nästlande dict
person["address"] = {
    "gatuadress":"Baldersväg 16",
    "ort":"Norsborg",
    "postnum": "145 71"
}
print(person)
#Skriv ut adressen enligt svensk standard
print(person['address']['gatuadress'])
print(person['address']['postnum'], (person['address']['ort']).upper())
"""

#Övning på tolkning av dictionary objekt

person = {
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
        {"name": "Morris","age": 3,"typ": "hund"},
        {"name": "Lisa","age": 2,"typ": "katt"},
        {"name": "Lassi","age": 5,"typ": "katt"}
    ]
}
pets = person['pets']
count_pets = len(person['pets'])
print('Namn är',person['firstname'],(person['lastname']))
print('Är',person['age'],'år gammal.')
print('Han har',count_pets,'husdjur.')

for pet in pets: #Man kan göra: for pets in person['pets'].
    print(f"* En är {pet['age']} och är en {pet['typ']} som heter {pet['name']}")


