import random
choices = ["rock" , "paper" , "scissors"]
user_score = 0
pc_score = 0
while True :
    user = input("Rock/Paper/Scissores? (or type 'exit' to quit):")
    if user == "exit" :
        break
    pc = random.choice(choices)
    print(f"computer chose :{pc}")
    if user == pc :
        print("It's a tie!")
Elif (user == "rock" and pc == "scissors") or\
             (user == "paper" and pc == "rock") or \
             (user == "scissors" and pc == "paper");
print( "you win!")
user_score += 1
Else : print( "computer wins!") == pc_score = +1
print( f"your score :{user_score} | computer: {pc_score}\n")
    
