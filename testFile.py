from random import randint

randNum = randint(1, 10)
print("+=== Guess a number from 1 to 10 ===+\n")

num = None

print(randNum)    #testNumber

while num != randNum:
    userInput = int(input("Your guess: "))

    if userInput > randNum:
        print("\nToo high.")
        
    elif userInput < randNum:
        print("\nToo low.")

    else:
        print("\nGood guess!")
        break

