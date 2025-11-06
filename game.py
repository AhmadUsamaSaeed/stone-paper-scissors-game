import random

def gamefun():
# List of choices
 choices = ["stone", "paper", "scissors"]
# Computer makes a random choice
 computer_choice = random.choice(choices)
 user_input = input("Enter b/w (stone, paper and scissors): ").lower()
 print (computer_choice)
 print(user_input)

 if user_input not in choices:
    print("Invalid choice! Please try again.")
    return None


 print(f"Computer chose: {computer_choice}")
 print(f"You chose: {user_input}")

 if computer_choice == user_input:
    print("Game  is tie")
 elif(computer_choice == "stone" and user_input == "scissors") or (computer_choice == "paper" and user_input == "stone" ) or(computer_choice == "scissors" and user_input == "paper"):
    print(f"computer win {computer_choice}")
 else:
    print("You win")

gamefun()    