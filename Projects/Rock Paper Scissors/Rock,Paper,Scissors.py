import random

print()
print("______Welcome_to_Rock,Paper,Scissors!______\n")

while True:
    user_move = input("Insert a choice (rock, paper, scissors): ").lower()
    possible_move = ["rock", "paper", "scissors"]
    computer_move = random.choice(possible_move)
    print(f"\nYou Chose {user_move}, computer chose {computer_move}")


    if user_move == computer_move:
        print(f"Both players chose {computer_move}. It's a draw!")
    elif user_move == "rock":
        if computer_move == "scissors":
            print("Rock breaks scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif user_move == "paper":
        if computer_move == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif user_move == "scissors":
        if computer_move == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock breaks scissors! You lose!")
    else:
        print("Invalid move, please select  a valid move from the possible moves which are rock, paper or scissors.")
        continue
        
    play_again = input("Play Again? (y/n): ")
    if play_again.lower() != "y":
        break

