import random


def main():
    guessing_game()
    play_again()


def guessing_game():
    number = random.randint(1, 10)

    player_name = input("Hello there! What is your name?")

    print("Nice to meet you, " + player_name)

    print(player_name + ", I am thinking of a number between 1 and 10")

    print("Could you guess what it is?")

    number_of_guesses = 0

    while number_of_guesses < 5:
        try:
            guess = int(input("Enter a number: "))
            number_of_guesses += 1
            if guess < number:
                print('Your guess is too low')
            if guess > number:
                print('Your guess is too high')
            if guess == number:
                print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
                break
        except ValueError:
            print("Please enter a number.")
    else:
        print('You did not guess the number, The number was ' + str(number))

    print("Thanks for playing!")


def play_again():
    while True:
        next_game = input("Would you like to play again?(Y or N) > ")
        if next_game == "Y":
            main()
        if next_game == "N":
            print("Thanks for playing. Goodbye!")
            exit()
        else:
            print("I'm sorry I could not recognize what you entered")

main()

