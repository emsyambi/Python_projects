from random import randint


def main():
    player_name = input("Hello there! What is your name?  ")
    print("Nice to meet you, " + player_name)
    print("Let's play a game of Rock, Papers and Scissors.")

    play_game()
    play_again()


def play_game():
    num_games = int(input("Enter how many games you would like to play:  "))
    print("You are going to play " + str(num_games) + " games! Here we go!")

    # create a list of play options
    t = ["Rock", "Paper", "Scissors"]

    # assign a random play to the computer
    computer = t[randint(0, 2)]

    player_wins = 0
    computer_wins = 0
    games_played = 0

    # set player to False
    # player = False

    while games_played < num_games:
        # set player to True
        player = input("Choose either Rock, Paper or Scissors and enter it: ")
        games_played += 1
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                computer_wins += 1
            else:
                print("You win!", player, "smashes", computer)
                player_wins += 1
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                computer_wins += 1
            else:
                print("You win!", player, "covers", computer)
                player_wins += 1
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                computer_wins += 1
            else:
                print("You win!", player, "cut", computer)
                player_wins += 1
        else:
            print("That's not a valid play. Please make sure you enter either Rock, Paper or Scissors!")
        # player was set to True, but we want it to be False so the loop continues
        # player = False
        computer = t[randint(0, 2)]

    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(computer_wins))
    print("Games played: " + str(games_played))

    if player_wins >= (num_games / 2):
        print("Congratulations, you won!")
    elif player_wins == computer_wins:
        print("Oh! It's a tie!")
    else:
        print("Oops! You lost.")


def play_again():
    while True:
        next_game = input("Would you like to play again?(y or n) > ")
        if next_game.lower() == "y":
            main()
        if next_game.lower() == "n":
            print("Thanks for playing. Byeeee!")
            exit()
        else:
            print("I'm sorry, I could not recognize what you entered. Please type y or n")


main()
