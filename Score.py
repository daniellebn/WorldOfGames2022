def add_score(difficulty):
    try:
        file = open("Scores.txt", "r")
    except FileNotFoundError:
        file = open("Scores.txt", "w")

    current_score = int(file.read())
    points_of_winning = (difficulty*3) + 5
    new_score = current_score + points_of_winning
    file = open("Scores.txt", "w")
    file.write(str(new_score))
    print(f"your new score is {new_score}")
    file.close()
