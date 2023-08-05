import random
guessNumber=random.randrange(1,101)
chance = 0

while chance < 3:
    guess=int(input("Guess the number:- "))

    if guess < guessNumber:
        print("Random number is ", guessNumber)
        print("Your Guess number is low comparision to random number.")
    
    if guess > guessNumber:
        print("Random number is ", guessNumber)
        print("Your Guess number is high comparision to random number.")
    
    if guess == guessNumber:
        print("Random number is ", guessNumber)
        print("You won")
    
    chance += 1
    if chance == 3:
        print("Game over ! you loss")