from Utils import screen_cleaner
from Score import add_score, initialize_score


def welcome():
    username = input("Please Enter Your Name: ")
    initialize_score()
    return f"Hello {username} and Welcome to the World of Games (WoG). Here you can find many cool games to play."


def load_game():
    NewScore = 0
    while True:
        print("Please choose a game to play:")
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        print("2. Guess Game - guess a number and see if you chose like the computer")
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

        GameNumber = input("Enter the number of the game you want to play (1-3), or 'q' to quit: ")

        if GameNumber == 'q':
            break

        if GameNumber not in ['1', '2', '3']:
            print("Invalid Game Number. Please enter a number between 1 and 3")
            continue

        DifficultyNumber = input("Please choose game difficulty from 1 to 5: ")

        if DifficultyNumber not in ['1', '2', '3', '4', '5']:
            print("Invalid Difficulty Number Entered. Please enter a number between 1 and 5")
            continue

        Game = int(GameNumber)
        Difficulty = int(DifficultyNumber)

        if Game == 1:
            print(f"You have chosen the Game Number: {Game} and difficulty level is {Difficulty}. Let's play!")
            from MemoryGame import play_memory_game
            result = play_memory_game(Difficulty)
        elif Game == 2:
            print(f"You have chosen the Game Number: {Game} and difficulty level is {Difficulty}. Let's play!")
            from GuessGame import play_guess_game
            result = play_guess_game(Difficulty)
        elif Game == 3:
            print(f"You have chosen the Game Number: {Game} and difficulty level is {Difficulty}. Let's play!")
            from CurrencyRouletteGame import play_roulette_game
            result = play_roulette_game(Difficulty)
        else:
            print("You have entered incorrect Game number.")
            continue

        if result['success']:

            NewScore = add_score(Difficulty)
            if NewScore != -1:
                print(f"Congratulations! Your new score is: {NewScore}")
            else:
                print("Failed to update the score.")

        while True:
            play_again = input("Do you want to play another game? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == 'no':

            print(f"Your final score: {NewScore}")
            break
        else:

            screen_cleaner()

    print("Thank you for playing!")


