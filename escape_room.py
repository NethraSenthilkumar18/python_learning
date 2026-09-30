import random

print("ESCAPE ROOM")
print("You are trapped inside a mysterious room!")
print("Solve the clues and escape before your attempts run out.")
print()

print("ROOM 1: THE SECRET CODE")
print("A locked door stands in front of you...")
print("You need to find the secret code to open it.")

secret_code = random.randint(100, 999)

print("Find the 3-digit secret code!")
print("You have 3 attempts.")

for attempt in range(3):
    guess = int(input("Enter the secret code: "))

    if guess == secret_code:
        print("Correct! The door is unlocked!")
        break
    else:
        print(" Wrong code! Try again.")

else:
    print("You used all your attempts!")
    print("GAME OVER!")

print()
print("ROOM 2 UNLOCKED!")
print("You enter a dark room...")
print("There is a mysterious riddle on the wall.")
