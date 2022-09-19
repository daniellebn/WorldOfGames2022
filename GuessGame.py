import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    user_guess = int(input(f"Please enter a number between 1 to {difficulty}: "))
    return user_guess


def compare_results(user_guess, secret_number):
    if user_guess == secret_number:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(user_guess, secret_number)

