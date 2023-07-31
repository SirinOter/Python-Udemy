# import imports.grade_average_service as grade_service

homework_assignment_grades = {
    'homework_1': 85,
    'homework_2': 100,
    'homework_3': 81,
}

# grade_service.calculate_homework(homework_assignment_grades)

import random

types_of_drinks = ['Soda', 'Coffee', 'Water', 'Tea']  # Water
print(random.choice(types_of_drinks))

print(random.randint(1, 10))  # 2

import math

square_root = math.sqrt(64)
print(square_root)  # 8

import random


def rock_paper_scissors():
    player_one = random.randint(1, 3)
    player_two = random.randint(1, 3)

    print('ROCK PAPER SCISSORS SHOOT!')

    if player_one == 1:
        if player_two == 1:
            print('rock DRAWS rock')

        elif player_two == 2:
            print('rock Loses paper')
        else:
            print('rock BEATS scissors')
    elif player_one == 2:
        if player_two == 1:
            print('paper BEATS rock')
        elif player_two == 2:
            print('paper DRAWS paper')
        else:
            print('paper LOSES scissors')
    else:
        if player_two == 1:
            print('scissors LOSES rock')
        elif player_two == 2:
            print('scissors BEATS paper')
        else:
            print('scissors DRAWS scissors')

    rock_paper_scissors()


