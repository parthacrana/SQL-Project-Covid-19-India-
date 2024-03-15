#ROCK PAPER SCISSORS PROJECT 
import random

# to print the rules of the game
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

user_action = input("Enter a choice (rock, paper, scissors): " )

# 2 parameters...user's choice and computer's choice 
possible_action = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_action)

# message to user
print(f"\nYou chose {user_action}, computer chose {computer_action} \n")
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")

# if user chooses rock 
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock beats scissors! You win!")

    else:
        print("Paper beats scissors! You lose.")

# if user chooses paper 
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper beats rock! You win!")

    else:
        print("Scissors beats paper! You lose!")

# if user chooses scissors
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors beats paper! You win!")

    else:
        print("Rock beats scissors! You lose.")

# at the end of the game 
while True:
     ans = input("Would you like to play again? (yes/no) " )
     if ans == "yes":
         print("\nContinuing to next game...")
         break
     if ans == "no":
         print("\nWe don't stop playing because we grow old, we grow old because we stop playing, Come again!")
         break
         
