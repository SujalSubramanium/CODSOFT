import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    user_score = 0
    comp_score = 0

    while True:
        user = input("rock, paper or scissors? (or quit): ").lower()
        if user == 'quit':
            break
        if user not in options:
            print("Invalid input.")
            continue

        comp = random.choice(options)
        print("Computer chose:", comp)

        if user == comp:
            print("It's a tie.")
        elif (user == 'rock' and comp == 'scissors') or \
             (user == 'paper' and comp == 'rock') or \
             (user == 'scissors' and comp == 'paper'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins.")
            comp_score += 1

        print(f"Score: You {user_score} - {comp_score} Computer")
        print("-" * 25)

if __name__ == "__main__":
    play_game()