# The Cow and Bull Game
"""
Cows and Bulls: A Classic Logic Code-Breaking Game

Rules:
- The computer generates a secret 4-digit number with unique digits.
- The player guesses a 4-digit number to crack the secret code.
- Feedback is provided after each guess:
  * Bulls: Correct digits in the correct position.
  * Cows: Correct digits in the wrong position.
- The game ends when the player scores 4 Bulls.
"""

import random

def getDigit(num):
    return [int(i) for i in str(num)]

def isNotDuplicate(num):
    num_list = getDigit(num)
    if(len(num_list) == len(set(num_list))):
        return True
    else:
        return False
    
def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if isNotDuplicate(num):
            return num

def BullAndCowGame(num, guess):
    numOfBullAndCow = [0, 0]
    num_list = getDigit(num)
    guess_list = getDigit(guess)
    
    for i, j in zip(num_list, guess_list):
        if j in num_list:
            if i == j:
                numOfBullAndCow[0] += 1
            else:
                numOfBullAndCow[1] += 1
    return numOfBullAndCow


num = generateNum()
tries = int(input("Enter the Number of Tries that you need to guess the Number: "))

while tries > 0:
    guess = int(input("Guess the Number: "))
    NumOfBullAndCow = BullAndCowGame(num, guess)
    print(f"The Number of Bulls are: {NumOfBullAndCow[0]} and The Number of Cow are: {NumOfBullAndCow[1]}")
    tries -= 1
    
    if NumOfBullAndCow[0] == 4:
        print("You Have Guessed The Code Correctly!!")
else:
    print(f"You ran out of Tries, Beeter Luck next Time!! \nThe Number was {num}")  