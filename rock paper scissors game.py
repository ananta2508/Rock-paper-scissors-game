import random
def computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

def check_winner(user, computer):
    if user == computer:
        return "Tie"

    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "User"

    else:
        return "Computer"



user_score = 0
computer_score = 0

print("=" * 45)
print("       ROCK PAPER SCISSORS GAME")
print("=" * 45)

while True:

    print("\nChoose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Please try again.")
        continue

    if choice == "1":
        user = "Rock"
    elif choice == "2":
        user = "Paper"
    else:
        user = "Scissors"

    computer = computer_choice()

    print("\nYour Choice     :", user)
    print("Computer Choice :", computer)

    result = check_winner(user, computer)

    if result == "Tie":
        print("Result : It's a Tie!")

    elif result == "User":
        print("Result : You Win!")
        user_score += 1

    else:
        print("Result : Computer Wins!")
        computer_score += 1

    print("\n------ Score Board ------")
    print("You      :", user_score)
    print("Computer :", computer_score)

print("\n========== FINAL RESULT ==========")
print("Your Score      :", user_score)
print("Computer Score  :", computer_score)

if user_score > computer_score:
    print("Congratulations! You are the Winner.")
elif computer_score > user_score:
    print("Computer Wins the Game.")
else:
    print("The Match is a Draw.")

print("\nThank you for playing!")