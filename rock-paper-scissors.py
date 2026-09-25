import random

print(" Rock Paper Scissors ")
print("Choose one:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

user_choice = input("Enter your choice: ")

choices = ["Rock", "Paper", "Scissors"]

computer_choice = random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)
