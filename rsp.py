import random
import colorama
from colorama import init, Fore, Back, Style
init()

elements = ['rock', 'paper', 'scissors']

bot_wins_count = 0
user_wins_count = 0

gameRunning = True

while gameRunning:
    symbol = random.choice(elements)
    userElement = input('Enter element: ')

    if symbol == 'rock' and userElement == 'paper' or symbol == 'scissors' and userElement == 'rock' or symbol == 'paper' and userElement == 'scissors':
        print('\tBot:', symbol)
        print('\n\tUser won')
        user_wins_count += 1
    elif symbol == 'rock' and userElement == 'scissors' or symbol == 'paper' and userElement == 'rock' or symbol == 'scissors' and userElement == 'paper':
        print('\tBot:', symbol)
        print('\n\tBot won')
        bot_wins_count += 1
    elif userElement == 'q':
        gameRunning = False
    else:
        print('\n\tTie')

if user_wins_count > bot_wins_count:
    print(f'\n\tUser wins:', Fore.BLACK + Back.GREEN + f'{user_wins_count}' + Style.RESET_ALL, f'\n\tBot wins:', Fore.BLACK + Back.RED + f'{bot_wins_count}' + Style.RESET_ALL)
elif user_wins_count < bot_wins_count:
    print(f'\n\tUser wins:', Fore.BLACK + Back.RED + f'{user_wins_count}' + Style.RESET_ALL, f'\n\tBot wins:', Fore.BLACK + Back.GREEN + f'{bot_wins_count}' + Style.RESET_ALL)
else:
    print(f'\n\tUser wins: {user_wins_count}\n\tBot wins: {bot_wins_count}')
