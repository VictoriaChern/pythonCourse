import os
import random

# очищаем консоль
os.system('clear')

def ask_name(n):
    return input(f'Введите имя игрока {n}: ')

def define_player_list(p1, p2):
    rand = random.randint(0,1)
    return [p1, p2] if rand == 0 else [p2, p1] 

def ask_number(player, total_number):
    number = input(f'Игрок {player}, сколько конфет вы хотите взять? ')
    if(not number.isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return ask_number(player, total_number)
    number = int(number)
    if(number > 28):
        print(f'Ошибка: за один ход можно забрать не более чем 28 конфет')
        return ask_number(player, total_number)
    if (number > total_number):
        print(f'Ошибка: вы не можете взять больше чем {total_number} конфет')
        return ask_number(player, total_number)
    return number

def turn(player, total):
    print(f'Ходит игрок {player}')
    number = ask_number(player,total)
    return total - number

def game():
    candies = 100
    print(f'На столе лежит {candies} конфета')
    player_1 = ask_name(1)
    player_2 = ask_name(2)
    print('Бросаем жребий...')
    player_list = define_player_list(player_1,player_2)
    cursor = 0
    current_player = player_list[cursor]
    winner = None
    print(f'Первым будет ходить игрок {current_player}!')
    while(winner == None):
        current_player = player_list[cursor]
        candies = turn(current_player, candies)
        print(f'На столе осталось {candies} конфет')
        cursor += 1
        if(cursor > 1):
            cursor = 0
        if (candies == 0):
            winner = player_list[cursor]
    print(f'Игрок {current_player} проиграл')
    print('=======================================')
    print(f'======= Игрок {winner} победил !!! =========')
    print('=======================================')

game()