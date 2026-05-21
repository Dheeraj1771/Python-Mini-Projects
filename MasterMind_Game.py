import random

num = random.randint(1000, 9999)

print("Let the Computer Choose the Number...")
print("Now you can start guessing the Number...")

chances = int(input("Enter in how many chances can you guess the Number: "))
play_cnt = 0

while(True):
    play_cnt += 1
    chances -= 1
    n = int(input("Guess the Four Digit Number:  "))
    
    if(chances == 0):
        print("You were not able to Guess the Number, your Turn is Over!")
        print("You are not a Mastermind!!")
        break
    
    if(num == n):
        print("You Guessed the Number in,", play_cnt, "Guesses")
        print("The Number of chances left were: ", chances)
        print("You are a Mastermind!!")    
        break
    else:
        str_n = str(n)
        str_num = str(num)
        
        num_cnt = 0
        list = ['X', 'X', 'X', 'X']
        for i in range(0, 4):
            if(str_n[i] == str_num[i]):
                num_cnt += 1
                list[i] = str_n[i]
            else:
                continue
        
        if num_cnt == 0:
            print("You didn't guess any of the Number Correctly!")
            print("Please try Again!!")
        else:
            print("You didn't Guess the Number correctly!")
            print("You are close to the Number, You have Guessed", num_cnt, "digits correctly!")
            print("Here is/are the digits that you guessed correctly: ")
            for i in range(0, 4):
                print(list[i], end = ' ')
            print()
            print("Please Try Again!!")
        print("The Number of chances left are: ", chances)
                
                
                
            