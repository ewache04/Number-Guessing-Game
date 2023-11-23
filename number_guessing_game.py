'''
Author name: Jeremiah E. Ochepo
Code description: Number Guessing Game
Last Updated Date: 6/28/19
'''

import random


def guessing_game():
    options_list = ['yes', 'no']
    active = True
    range_min = 0
    range_max = 4

    while active:
        computer_pick = random.randint(range_min, range_max)
        repeat_input = input("Do you wish to play this game? (Yes or No): ").lower()

        try:
            if repeat_input in options_list and repeat_input == 'yes':
                user_pick = input(f"Pick a number from ({range_min} to {range_max}): ")

                try:
                    user_pick = int(user_pick)

                    if range_min <= user_pick <= range_max:
                        print(f"You entered the number: {user_pick}")
                        print(f"I picked the number: {computer_pick}")

                        if user_pick == computer_pick:
                            print("Your number is the same as mine, so you win... hurray!!")
                            print("Thanks for playing with me! Enter 'yes' to play again.\n")
                            continue
                        else:
                            print("Your number is different from mine, so you lose.")
                            print("Thanks for playing with me! Enter 'yes' to play again.\n")
                            continue
                    else:
                        print(f"Entry has to be a number from ({range_min} to {range_max})\n")
                        continue

                except ValueError:
                    print(f"Please enter a valid number from ({range_min} to {range_max})\n")
                    continue

            elif repeat_input in options_list and repeat_input == 'no':
                print('Bye! Till next time.')
                active = False
        except:
            print('Your entry has to be (Yes or No)\n')
            continue


guessing_game()
