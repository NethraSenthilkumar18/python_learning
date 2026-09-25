import random

print(" Rock Paper Scissors ")
print("Choose one:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

user_choice = input("Enter your choice: ")

if user_choice == "1":
    user_choice = "Rock"
elif user_choice == "2":
    user_choice = "Paper"
elif user_choice == "3":
    user_choice = "Scissors"
else:
    print("Invalid choice!")

choices = ["Rock", "Paper", "Scissors"]

computer_choice = random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a draw!")

elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You win!")

elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win!")

elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You win!")

else:
    print("Computer wins!")
