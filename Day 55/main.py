import random

options = ["snake", "gun", "water"]
computer = random.choice(options)
user = input("Enter your Option: ").lower()
if user == computer:
    print("Draw!")
elif (user == "snake" and computer == "water") or \
    (user == "gun" and computer == "snake") or \
    (user == "water" and computer == "gun"):
    print("User Wins!")
else :
    print("Computer Wins!")

print(f"User choice: {user} ")
print(f"Computer choice: {computer}")