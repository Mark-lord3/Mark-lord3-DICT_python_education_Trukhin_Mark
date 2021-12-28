game = list(['_', '_', '_', '_', '_', '_', '_', '_', '_'])
choose = list()
print(f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| {"".join(map(str, game))[6:9]} |')
print('__________')
x = 'X'
o = '0'
x_Win = 0
o_Win = 0
b = x
p = 0
coordinates = 0


def Restart():
    global choose
    restart = input('''Хочешь еще раз?
    1 - сначала
    2 - выйти''')

    if restart.isnumeric():
        restart = int(restart)
        if restart == 1:
            choose.clear()
            play_cor()
        elif restart == 2:
            print('Пока')
        else:
            print('Попробуй еще раз')
            Restart()
    else:
        print('Попробуй еще раз')
        Restart()


def play_str():
    global game
    game = list(['_', '_', '_', '_', '_', '_', '_', '_', '_'])
    global x, o, x_Win, o_Win, p, b, str


def play_cor():
    global game
    game = list(['_', '_', '_', '_', '_', '_', '_', '_', '_'])
    global x, o, x_Win, o_Win, p, b, coordinates
    while True:
        p = 0
        coordinates = 0
        word = "".join(map(str, game))
        if game[0] == 'X' and game[1] == 'X' and game[2] == 'X':
            print('X WON')
            x_Win = 1
            break
        elif game[0] == 'X' and game[3] == 'X' and game[6] == 'X':
            print('X WON')
            x_Win = 1
            break
        elif game[0] == 'X' and game[4] == 'X' and game[8] == 'X':
            print('X WON')
            x_Win = 1
            break
        elif game[2] == 'X' and game[5] == 'X' and game[8] == 'X':
            print('X WON')
            x_Win = 1
            break
        elif game[2] == 'X' and game[4] == 'X' and game[6] == 'X':
            print('X WON')
            x_Win = 1
            break
        elif game[6] == 'X' and game[7] == 'X' and game[8] == 'X':
            print('X WON')
            x_Win = 1
            break
        elif game[1] == 'X' and game[4] == 'X' and game[7] == 'X':
            print('X WON')
            x_Win = 1
            break
        elif game[3] == 'X' and game[4] == 'X' and game[5] == 'X':
            print('X WON')
            x_Win = 1
            break
        elif game[0] == '0' and game[1] == '0' and game[2] == '0':
            print('O WON')
            o_Win = 1
            break
        elif game[0] == '0' and game[3] == '0' and game[6] == '0':
            print('O WON')
            o_Win = 1
            break
        elif game[0] == '0' and game[4] == '0' and game[8] == '0':
            print('O WON')
            o_Win = 1
        elif game[2] == '0' and game[5] == '0' and game[8] == '0':
            print('O WON')
            o_Win = 1
            break
        elif game[2] == '0' and game[4] == '0' and game[6] == '0':
            print('O WON')
            o_Win = 1
            break
        elif game[6] == '0' and game[7] == '0' and game[8] == '0':
            print('O WON')
            o_Win = 1
            break
        elif game[1] == '0' and game[4] == '0' and game[7] == '0':
            print('O WON')
            o_Win = 1
            break
        elif game[3] == '0' and game[4] == '0' and game[5] == '0':
            print('O WON')
            o_Win = 1
            break
        elif '_' not in game and x_Win == 0 and o_Win == 0:
            print('tie')
            break
        print(f'Выберите место: {word}')
        player = str(input(f'введите {b}\nКоординаты :>>> '))
        split_player = ''.join(player.split())
        coordinates = {'1 1': 0, '1 2': 1, '1 3': 2, '2 1': 3, '2 2': 4, '2 3': 5, '3 1': 6, '3 2': 7, '3 3': 8}
        numbers = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']
        if player.isnumeric():
            print('введите правильные координаты ')
            print('__________')
            print(
                f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| \
{"".join(map(str, game))[6:9]} |')
            print('__________')
            continue
        elif str(player) not in str(numbers) and player != player.isnumeric():
            print('координаты долны быть от 1 to 3!')
            print('__________')
            print(
                f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| \
{"".join(map(str, game))[6:9]} |')
            print('__________')
            continue
        elif split_player.isnumeric():
            p = coordinates[player]
        else:
            print('вы должны ввести цифры!')
            print('__________')
            print(
                f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| \
{"".join(map(str, game))[6:9]} |')
            print('__________')
            continue

        if p < 0 or p > 8:
            print('Неизвестно')
            continue
        elif p in choose:
            print('Уже используется')
            print('__________')
            print(
                f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| \
{"".join(map(str, game))[6:9]} |')
            print('__________')
            continue
        else:
            choose.append(p)
            game.pop(p)
            game.insert(p, b)
            print('__________')
            print(
                f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| \
{"".join(map(str, game))[6:9]} |')
            print('__________')
            if b == x:
                b = o
            elif b == o:
                b = x
    x_Win = 0
    o_Win = 0
    b = x
    Restart()


play_cor()
#я кинул два файла (там можно реально играть учтите пж :)))))) )