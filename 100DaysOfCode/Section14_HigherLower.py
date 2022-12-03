import random
from Data import game_data


def choice(var_a, var_b):
    if var_a > var_b:
        return "a"
    else:
        return "b"


def game():

    game_continue = True
    score = 0

    rand_A = random.choice(game_data.data)
    print(rand_A)
    rand_B = random.choice(game_data.data)

    while game_continue is True:
        if rand_B == rand_A:
            rand_B = random.choice(game_data.data)
        print(rand_B)
        user_choice = input("Who has more followers? A or B").lower().strip(" ")
        actual_choice = choice(rand_A["follower_count"], rand_B["follower_count"])

        #print(f"User choice = {user_choice} and Actual choice = {actual_choice}")

        if user_choice == actual_choice:
            score += 1
            print(f"You are correct!Your score {score}")
        else:
            print(f"You are wrong! Your final score is {score}")
            game_continue = False

        rand_A = rand_B
        rand_B = random.choice(game_data.data)


game()

