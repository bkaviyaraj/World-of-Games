from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5


def initialize_score():
    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write('0')
        # print("Score initialized to 0.")
    except Exception as e:
        print(f"Error initializing score: {e}")


def add_score(difficulty):
    try:
        try:
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read().strip())
        except FileNotFoundError:
            # Initialize the score file with a default value of 0
            with open(SCORES_FILE_NAME, 'w') as file:
                file.write('0')
            current_score = 0
        except Exception as e:
            return BAD_RETURN_CODE

        points_won = POINTS_OF_WINNING(difficulty)
        new_score = current_score + points_won

        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))

        return new_score
    except Exception as e:
        return BAD_RETURN_CODE
