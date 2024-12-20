import random

art = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

choices = ["rock", "paper", "scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.\n")

    user_score = 0
    computer_score = 0
    ties = 0

    while True:
        user_choice = input("Your choice (rock/paper/scissors/quit): ").lower()
        if user_choice == "quit":
            print("Thanks for playing! Final scores:")
            print(f"You: {user_score} | Computer: {computer_score} | Ties: {ties}")
            break
        if user_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"\nYou chose:\n{art[user_choice]}")
        print(f"Computer chose:\n{art[computer_choice]}")

        result = determine_winner(user_choice, computer_choice)
        print(result + "\n")

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        else:
            ties += 1

# Run the game
if __name__ == "__main__":
    play_game()