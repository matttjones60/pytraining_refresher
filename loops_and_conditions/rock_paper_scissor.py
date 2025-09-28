import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
print("Computer chooses:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("You lose!")
print("Game over. Thanks for playing!")