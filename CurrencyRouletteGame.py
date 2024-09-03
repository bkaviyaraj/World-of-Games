import requests
import random


def play_roulette_game(difficulty):
    api_key = '376ae59457c273c469abccdd'
    base_currency = 'USD'
    target_currency = 'ILS'

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data['rates'][target_currency]
        print(f"The exchange rate from {base_currency} to {target_currency} is: {exchange_rate}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

    if difficulty < 1 or difficulty > 5:
        print("Invalid difficulty level. Please choose a level between 1 and 5.")
        exit()

    get_money_interval = (max(0, exchange_rate - (5 - difficulty)), exchange_rate + (5 - difficulty))
    random_amount = random.randint(1, 100)
    print(f"How much is {random_amount} dollars in ILS? (Guess within the interval)")

    try:
        get_guess_from_user = float(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit()

    if get_money_interval[0] * random_amount <= get_guess_from_user <= get_money_interval[1] * random_amount:
        print(f"Congratulations! Your guess is correct.")
        return {'success': True, 'difficulty': difficulty}
    else:
        print(
            f"Sorry, your guess is incorrect. The correct range was between {get_money_interval[0] * random_amount} and {get_money_interval[1] * random_amount}.")
        return {'success': False, 'difficulty': difficulty}
