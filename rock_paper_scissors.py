import random

choices = [
    'rock',
    'paper',
    'scissors',
    ]
userChoice = input("Enter your choice  rock or paper or scissors:  \n")
pcChoice   = random.choice(choices)

print(f"You choose: {userChoice}")
print(f"Computer choose: {pcChoice}")

if userChoice == pcChoice:
    print("Tie")
elif (userChoice == 'rock' and pcChoice == 'scissors') or (userChoice == 'paper' and pcChoice == 'rock') or (userChoice == 'scissors' and pcChoice == 'paper'):
    print("You Win and computer lost")

else:
    print("computer win and you lost")
