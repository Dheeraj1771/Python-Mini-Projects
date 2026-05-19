import random

print("Welcome to Rock, Paper, Scissor Game!")
print("Winning Rules of the Rock, Paper, Scissor Game is as follows: ")
print("Rock vs Paper -> Paper Wins \n" + 
    "Rock vs Scissor -> Rock Wins \n" + 
    "Paper vs Scissor -> Scissor Wins \n")

user_points = 0
comp_points = 0

while True:
    print("1. Play Game")
    print("2. View Scores")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    
    
    if choice == 1:
        print("Let's Start the Game!")
        ch = int(input("Enter your choice of Rock as (1), Paper as (2), Scissor as (3): "))
        
        while ch > 3 or ch < 1:
            ch = int(input("Enter valid choice from 1 to 3: "))
        
        if ch == 1:
            ch_name = "Rock"
        elif ch == 2:
            ch_name = "Paper"
        else:
            ch_name = "Scissor"
        
        print("User's Choice is: ", ch_name)
        print("It's Computer's Turn: ")
        
        comp_ch = random.randint(1, 3)
        if comp_ch == 1:
            comp_ch_name = "Rock"
        elif comp_ch == 2:
            comp_ch_name = "Paper"
        else:
            comp_ch_name = "Scissor"
        
        print("Computer's Choice is: ", comp_ch_name)
        print(ch_name, "vs", comp_ch_name)
        
        if ch == comp_ch:
            result = "DRAW"
        elif(ch == 1 and comp_ch == 2) or (ch == 2 and comp_ch == 1):
            result = "Paper"
        elif(ch == 2 and comp_ch == 3) or (ch == 3 and comp_ch == 3):
            result = "Scissor"
        elif(ch == 1 and comp_ch == 3) or (ch == 3 and comp_ch == 1):
            result = "Rock"
            
        if(result == "DRAW"):
            print("It's a Tie!")
        elif(result == ch_name):
            print("User Wins!")
            user_points += 1
        else:
            print("Computer Wins!")
            comp_points += 1
        
        print("The Scores are: ")
        print("User: ", user_points, "Computer: ", comp_points)
    
    elif choice == 2:
        print("The Scores are: ")
        print("User: ", user_points, "Computer: ", comp_points)
    
    elif choice == 3:
        print("The Final Scores are: ")
        print("User: ", user_points, "Computer: ", comp_points)
        if(user_points > comp_points):
            print("User Won the Game!")
        elif(user_points < comp_points):
            print("Computer Won the Game!")
        else:
            print("It's a Tie!")
        print("Exiting the Game...")
        break
        
        
    
    