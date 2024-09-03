import random
import time


def play_memory_game(difficulty):
    generate_sequence = []
    for i in range(0, difficulty):
        generate_sequence.append(random.randint(1, 101))

    print(generate_sequence, end='', flush=True)
    time.sleep(0.7)

    print('\r' + ' ' * len(str(generate_sequence)), end='', flush=True)
    time.sleep(0.7)

    get_list_from_user = []
    for i in range(0, difficulty):
        get_list_from_user.append(int(input("\nPlease add a number you think was on this list: ")))

    print(f"\nThe generated list: {generate_sequence}")
    print(f"User guess: {get_list_from_user}")

    def is_list_equal(generate_sequence, get_list_from_user):
        return sorted(generate_sequence) == sorted(get_list_from_user)

    if is_list_equal(generate_sequence, get_list_from_user):
        print("Bingo!!! You won!!!")
        return {'success': True, 'difficulty': difficulty}
    else:
        print("You Lost!!! Better Luck Next Time")
        return {'success': False, 'difficulty': difficulty}

