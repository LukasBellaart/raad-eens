import random

i = 1
x = 1
punten = 0
while i <= 20:
    doorgaan = input("Nog een getal raden? -> ")
    if doorgaan.lower() == 'ja':
        print('dit is ronde '+str(i))
        randomnumber = random.randint(0,1000)
        margindown = randomnumber - 50
        marginup = randomnumber + 50
        print(randomnumber)
        while x <= 10:
            guess = input("Nummer? -> ")
            if guess.lower() == 'stop' or guess.lower() == 'quit':
                break
            guess = int(guess)
            if guess >= margindown and guess <= marginup:
                if guess == randomnumber:
                    print("Je heb het geraden!")
                    punten += 1
                    break
                elif guess >= margindown + 30:
                    print('Je bent heel warm (lager)')
                elif guess <= marginup - 30:
                    print("Je bent heel warm (hoger)")
                else:
                    if guess <= randomnumber:
                        print('Je bent warm (hoger)')
                    elif guess >= randomnumber:
                        print('Je bent warm (hoger)')
            elif guess <= randomnumber:
                print("helaas dat is fout, het antwoord is hoger")
            elif guess >= randomnumber:
                print("helaas dat is fout, het antwoord is lager")
        print("Je heb nu "+ str(punten)+ " punten!")
        i += 1
    else:
        break

print("De eindscore is "+ str(punten)+" punten!")
