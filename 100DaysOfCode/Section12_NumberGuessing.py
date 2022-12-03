import random
import Data.game_data
print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100")
dificulty_level = input("Choose the type of difficulty: Type 'easy' or 'hard:")

rand_number = random.randint(0, 101)

level_times = 0

if dificulty_level == 'easy':
    level_times = 10
else:
    level_times = 4


while level_times > 0:
    number = int(input("Make a guess?"))
    if number > rand_number:
        print("Too high")
    elif number < rand_number:
        print("Too low")
    elif number == rand_number:
        print("You got it!")
    level_times = level_times - 1
    print("Guess again!")
    print(f"You have {level_times} attempts to guess the number")




