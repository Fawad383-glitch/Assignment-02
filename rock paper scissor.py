import random
item_list =["ROCK", "PAPER", "SCISSOR"]

user_choice = input("Enter your move = Rock, Paper, Scissor")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers the Rock = Computer")
    else:
        print("Both chooses same: = Match Tie ")

elif user_choice == "Rock":
    if comp_choice ==  "Paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper = Computer win")
    else:
        print("Paper covers rock = You win")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper = You win")
    else:
        print("Rock smashes scissor = Computer win")
         
       

