#Övningsuppgift 12.1

"""notes = {
    'Meddelande från skolan': "Friluftsdag på tisdag.",
    "Kom ihåg": "Ta bilen till verkstad.",
    "Inför tentan": "Gör alla instuderingsuppgifter."

}


print("Kom igång!")
for i in notes:
    print(i)
titel = input("Anteckningar > ")
try:
    print(notes[titel])
except KeyError:
    print("FEL! Du har ingen sådan anteckning.")
"""
notes = {
    'Meddelande från skolan': "Friluftsdag på tisdag.",
    "Kom ihåg": "Ta bilen till verkstad.",
    "Inför tentan": "Gör alla instuderingsuppgifter."

}
for key in notes:
    print("Titel:",key)
    print("Text:",notes[key])
    
