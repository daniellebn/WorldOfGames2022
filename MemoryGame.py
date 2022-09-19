import os
import random
import time


def generate_sequence(difficulty):
    random_list = random.sample(range(1, 101), difficulty)
    return random_list


def get_list_from_user(difficulty):
    user_list = []
    for i in range(difficulty):
        user_list.append(int(input("please enter a number: ")))
    return user_list


def is_list_equal(user_list, random_list):
    user_list.sort()
    random_list.sort()
    if user_list == random_list:
        return True
    else:
        return False


def play(difficulty):
    random_list = generate_sequence(difficulty)
    print(random_list)
    time.sleep(1)
    os.system('cls')
    user_list = get_list_from_user(difficulty)
    return is_list_equal(random_list, user_list)

