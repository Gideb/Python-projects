import random

print('Hi, what is your name?')
name = input()

print('Welcome '+ name + ', I have a secret number from 1 to 20.')
print('Take a guess...')
secretNumber = random.randint(1, 20)

try:
    for guesscount in range(1, 6):
        guessNumber = int(input())
    
        if guessNumber < secretNumber:
            print('Guess a little higher')
        elif guessNumber > secretNumber:
            print('Guess a little lower')
        else:
            break
    
    if guessNumber == secretNumber:
        print('Bravo ' +name+', you guessed right after '+ str(guesscount)+ ' guesse(s).')
    else:
        print("You're out of guesses " + name + ", the secret number is "+str(secretNumber))
except:
    print('Come on ' +name + ', I said a number. Restart game again')
