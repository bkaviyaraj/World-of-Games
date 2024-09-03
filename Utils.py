import os

SCORES_FILE_NAME = r"D:\WorldOfGames\WorldOfGames\Scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')





