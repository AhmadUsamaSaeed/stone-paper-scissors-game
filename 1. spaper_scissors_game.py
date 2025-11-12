# requirment

### 🧠 **Game Logic & Structure**
# Loop the game** — let players play multiple rounds until they choose to quit. done
# Add score tracking** — keep count of wins, losses, and ties for both player and computer. done
# Best of N** — let the user decide how many rounds to play (e.g., best of 3, 5, etc.).
# Replay option** — ask if the user wants to play again after each game.done

### 💻 **Interface Improvements**
# Use colors or emojis** — to make it more visually fun (`stone 🪨`, `paper 📄`, `scissors ✂️`).
# Clear output** — use line breaks or separators for readability.


### ⚙️ **Code & Design**
# Use functions for modularity** — e.g., separate input, logic, and display parts.
#Error handling** — handle invalid inputs gracefully (like typos).

### 🧩 **Extra Fun Features**
# 13. **Leaderboard / score file** — store scores in a file (`scores.txt` or JSON).

import random
def gameRandom():
 
 computer_score = 0
 user_score = 0   
 while True:
      
      print("press 1 for play")
      print("press 2 for Exit")
      userpress = int(input("enter your number"))
      if userpress ==1:
         choices = ["stone", "paper", "scissors"]
         user_input = input("choise b/w `stone 🪨`, `paper 📄`, `scissors ✂️`: ").lower()
         computer_choice =  random.choice(choices)
         print(f"computer choice is {computer_choice}")
         print(f"your choice is {user_input}")
         if user_input == computer_choice:
          print("game tie")
         elif user_input not in choices:
           print("You enter wrong words try again") 
         elif(computer_choice == "stone" and user_input == "scissors") or (computer_choice == "paper" and user_input == "stone" ) or(computer_choice == "scissors" and user_input == "paper"):
          print(f"computer win {computer_choice}")
          computer_score+=1
          print(f"computer win and now computer score is {computer_score}")
          print(f"your score is {user_score}")
         else:
          print("You win")
          user_score+=1
          print(f"You win and now your score is {user_score}")
          print(f"computer score is {computer_score}")
      elif userpress==2:
        print("thanks for comings ")
        break
      else:
        print("you enter wrong number try Again")



gameRandom()         