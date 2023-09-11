notes = {
    'Meddelande från skolan': "Friluftsdag på tisdag.",
    "Kom ihåg": "Ta bilen till verkstad.",
    "Inför tentan": "Gör alla instuderingsuppgifter."

}
while True:

    for key in notes:
        print("Titel:",key)
        print("Text:",notes[key])
        print('---------')

    print("Lägg till artikel > ")
    cmd = input("Titel: ")
    cmd2 = input("Text: ")
    notes[cmd] = cmd2
    del notes[cmd]

