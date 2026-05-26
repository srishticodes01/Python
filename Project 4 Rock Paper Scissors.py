import random
print("Welcome to Rock Paper Scissors!" 
"\nPlease enter your choice:For rock choose 1,for paper choose 2, or scissors choose 3: ")
choices= ["rock","paper","scissors"]
user_input=int(input())
if user_input==1:
    user_input="rock"
elif user_input==2:
    user_input="paper"
elif user_input==3:
    user_input="scissors"
else:
    print("The input is invalid . Try Again")
input_from_computer= random.choice(choices) 
print("The computer chose: ",input_from_computer)
if user_input==input_from_computer:
    print("It's a tie!")
elif (user_input=="rock" and input_from_computer=="scissors") or (user_input=="scissors" and input_from_computer=="paper") or (user_input=="paper" and input_from_computer=="rock"):
    print("U wonn!!!!")
else:
    print("U Lost, Better Luck Next Time")