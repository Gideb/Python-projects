import random

print('Hello, what is your name?')
name = input()

print('Well, '+ name + '. I am thinking of a number between 1 and 20.')
print('Take a guess.')
secretNumber = random.randint(1,20)
try:
    for guessesTaken in range(1, 6):
        guess = int(input()) 
        
        if guess < secretNumber:
            print('Guess a little higher.')
        elif guess > secretNumber:
            print ('Guess a little lower ')
        else:
            break
    
    if guess == secretNumber:
        print('Good Job, '+ name + '. You guessed my secretNumber in ' + str(guessesTaken) + ' guesses')
    else:
        print('Sorry '+ name + ', my secret number was ' + str(secretNumber))
except:
    print('Come on ' +name+ ', I said a number. Restart game again')