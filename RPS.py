import random

choice_list={"r": "Rock",
            "s": "Scissors",
            "p": "Paper"}

#A function to get user input
def user_input():
  print("Welcome to Rock, Paper, Scissors Game")
  
  while True:
    print("R represnets Rock \nP represents paper \nS represents scissors" )
    print("------------------------------------------------------")
    user_move = str(input("Enter a choice between (R , P, S): ").lower())
    if user_move in ['r','s','p']:
      print(f"User chose {choice_list[user_move]}")
      return user_move  
    else:
      print("Invalid response, Try again")
      print('---------------------------------------------')
      

#A function to get computer input
def computer_input():
  possible_actions = ["r", "p", "s"]
  computer_move = random.choice(possible_actions)
  print(f"Computer chose {choice_list[computer_move]}")
  return computer_move

#A function to determine Winner
def determine_winner(user_action, computer_action):
  print("------------------------------------------")
  if user_action == computer_action:
    print(f"Both players selected {choice_list[user_action]}. It's a tie!")
    
  elif user_action == "r":
    if computer_action == "s":
      print("Rock smashes scissors! You win!")
    else:
      print("Paper covers rock! You lose.")
  elif user_action == "p":
    if computer_action == "r":
      print("Paper covers rock! You win!")
    else:
      print("Scissors cuts paper! You lose.")
  elif user_action == "s":
    if computer_action == "p":
      print("Scissors cuts paper! You win!")
    else:
      print("Rock smashes scissors! You lose.")

  

def play_again():
  play_again_answer = str(input("Play again? (y/n): ")).lower()
  state=True
  while state == True:
    if play_again_answer =="n":
      break;
    elif play_again_answer =="y":
      state=False
      init()
    else:
      print('Invalid Input')
      state=False
      play_again()

        
def init():
  user_choice=user_input()
  
  comp_choice=computer_input()
  
  determine_winner(user_choice,comp_choice)
  
  play_again()

init()