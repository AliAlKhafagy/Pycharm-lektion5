notes = {
    'Meddelande från skolan': "Friluftsdag på tisdag.",
    "Kom ihåg": "Ta bilen till verkstad.",
    "Inför tentan": "Gör alla instuderingsuppgifter."

}
while True:

    print(".: ALWAYSNOTE :.\n-- gold edition --\n******************")
    for key in notes:


        print("Titel:",key)
        print('---------')
    print("""
view | view note
add | add note
rm | remove note
exit | exit program
------------------""")

    cmd = input("menue >")
    if cmd == "view":
        print(notes)
    elif cmd == "add":
        print("Lägg till en artikel: ")
        cmd = input("Titel: ")
        cmd2 = input("Text: ")
        notes[cmd] = cmd2
    elif cmd == "rm":
        tabort = input("Ta bort artikel: ")
        del notes[tabort]
    elif cmd == "exit":
        break






