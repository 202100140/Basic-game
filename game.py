import random
user_action=input("Enter choice (rock,paper,scissors):")
possible_actions = ["rock","paper","scissors"]
computer_action = random.choice(possible_actions)
print("you choose",user_action,"\computer choose:",computer_action)
if user_action == computer_action:
    print("Both player selected:",user_action,"Tie")
elif user_action == "rock":
    if computer_action == "scissors":
            print("Rock smashes scissors:!! You win")
    else:
            print("paper covers rock:!! you loose")

elif user_action == "paper":
    if computer_action == "rock":
            print("paper covers rock:!! You win")
    else:
            print("scissors cuts paper :!! you loose")
elif user_action == "scissors":
    if computer_action == "paper":
            print("scissors cuts paper:!! You win")
    else:
            print("rock smashes scissors:!! you loose")
    