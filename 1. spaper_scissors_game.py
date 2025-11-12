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