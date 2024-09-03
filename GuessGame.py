import random


def play_guess_game(difficulty):
    secret_number = random.randint(1, difficulty + 1)
    get_guess_from_user = int(input(f"\nGuess a number between 1 and {difficulty}:"))
    compare_results = secret_number == get_guess_from_user
    print(f"\nNumber generated: {secret_number}")
    print(f"User guess: {get_guess_from_user}")

    def play(compare_results):
        if compare_results:
            print("Bingo!!! You won!!!")
            return {'success': True, 'difficulty': difficulty}
        else:
            print("You Lost!!! Better Luck Next Time")
            return {'success': False, 'difficulty': difficulty}

    result = play(compare_results)
    return result