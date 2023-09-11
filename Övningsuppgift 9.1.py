#Visa hur man med en for loop kan beräkna
#1. Summan av alla heltal mellan 0 och 1000000
"""siffror = list(range(1,1000000))
for siffra in siffror:
    total = sum(siffror)
    print("Din summa är",total)
    odd_numbers = [x for x in range(1, 1001) if x % 2 != 0]#2. Summan av alla udda tal.
    # if x % 2 != 0 - Vi har ett villkor som kontrollerar om det aktuella talet x är ojämnt.
    # x % 2 är en modulo-operation som ger resten när x delas med 2. Om resten inte är lika med 0 (vilket betyder att talet är udda),
    #kommer x att inkluderas i listan.
    totala = sum(odd_numbers)
    print("Summan av alla udda tal: ", totala)
    break
"""
#Modifiera scriptet så att listan registrerade töms på alla namn som specificerats i listan avanmälningar.
#Uppgiften måaste lösas med en for-loop.

"""registrerade =[" Anna ", "Eva ", " Erik ", " Lars ", " Karl "]
avanmalningar =[" Anna ", " Erik ", " Karl "]
ny_registrerade = []
for namn in registrerade:
    if namn not in avanmalningar:
        ny_registrerade.append(namn)

print(ny_registrerade)
"""
#Visa hur man med nästlade for-loopar kan skriva ut samtliga kombinationer avde för och efternamn
# som specificerats i listorna ovan.

"""förnamn =[" Maria ", " Erik ", " Karl "]
efternamn =[" Svensson ", " Karlsson ", " Andersson "]
kombinerade_namn = [f"{namn1} {namn2}" for namn1, namn2 in zip(förnamn, efternamn)]#zip() att kombinera namnen i förnamn och efternamn parvis,
print (kombinerade_namn)
"""

"""todos = [ 'Städa', 'Handla', 'Plugga' , 'Ge blod']
text = ".: TODOIFY :.\n*************"
centered_text = text.center(20)
print(centered_text)
print ('-',todos[0])
print ('-',todos[1])
print ('-',todos[2])
print ('-',todos[3])
"""
width_ui = 20
bilar = ['Mercedes', 'Volvo', 'Toyota']
print (bilar) # [ ’ Mercedes ’, ’Volvo ’, ’Toyota ’, ’Kia ’]
while True:
    try:
        num = 1
        print("'.: STACKMASTER v1 .33.7 :.'".center(width_ui))
        print("-" * width_ui)
        for i in bilar:
            print(num, "-" + i)
            num += 1
        print("Push > Push element to stack.")
        print("Pull > Pull element from stack.")
        print("Exit > Exits program.")
        Menu = input("Menu >").lower()

        if Menu == ("Push").lower():
            val = input("Vilken bil vill du lägga till?: ")
            bilar.append(val)
        elif Menu == ("Pull").lower():
            val2 = int(input("Vilken bil vill du ta bort? Välj siffra."))
            bilar.pop(val2 - 1)

        elif Menu == ("exit").lower():
            break
        else:
            print("Ogiltigt val!")
            input("Tryck på ENTER för att försöka igen.")
    except ValueError:
            print(i,"är inte ett giltigt heltal!")
    except IndexError:
        print(val2,"Siffran är ogiltig.")


# Öppna en befintlig fil (w betyder write, x betyder create, r betyder read,
"""
if os.path.exists('sign.txt'):
# Öppna en befintlig fil
    f = open('sign.txt', 'a')
else:
# Skapa en ny fil
    f = open('sign.txt', 'x')
message = ll
print('| - - - - - - - - - - - - - - - - - - - - - - - - |')
print('|   # --------------------------------------- #   |')
print(f'| ### | Welcome to {message.center(18)} | # ###  |')
print ('| ### ---------------------------------- ### ### |')
print ('|  |                                      |   | #|')
print('|- - - - - - - - - - - - - - - - - - - - - - - - -|')
print('| C | Change sign message')
print('| E | Exit program')
print('| - - - - - - - - - - - - - - - - - - - - - - - -')
print('| >')
"""


