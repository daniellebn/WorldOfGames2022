import GuessGame
import MemoryGame
import Score
import Utils
import time


def welcome(name):
    return "HellO " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"


def is_valid(min_range, max_range, user_choice):
    if int(user_choice) < min_range or int(user_choice) > max_range:
        return False
    else:
        return True


def load_game():
    type_of_games = open("choose_game.txt", "r")
    print(type_of_games.read())
    type_of_games.close()

    game_selection = int(input("Please enter your game selection: "))
    while not is_valid(1, 3, game_selection):
        game_selection = int(input("Must be a number between 1 to 3 - please try again: "))

    difficulty = int(input("Please enter level of difficulty: "))
    while not is_valid(1, 5, difficulty):
        difficulty = int(input("Must be a number between 1 to 5 - please try again: "))

    if game_selection == 1:
        if MemoryGame.play(difficulty) is True:
            Score.add_score(difficulty)
        else:
            print("SORRY, you lost!")
            time.sleep(5)
            Utils.screen_cleaner()
            load_game()

    if game_selection == 2:
        if GuessGame.play(difficulty) is True:
            Score.add_score(difficulty)
        else:
            print("SORRY, you lost!")
            time.sleep(5)
            Utils.screen_cleaner()
            load_game()
