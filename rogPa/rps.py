import random

variant = ['rog', 'paper', 'scissors', 'sponge', 'air', 'water', 'fire']

global rat_I, rat_An, rat_A, i


def choose_rat(inp):
    with open("rating.txt", "r") as file:
        names = file.readlines()
        str1 = names[0]
        str2 = names[1]
        str3 = names[2]
        str1_1 = str1.split(" ")
        rat_I = int(str1_1[1])
        str2_2 = str2.split(" ")
        rat_An = int(str2_2[1])
        str3_3 = str3.split(" ")
        rat_A = int(str3_3[1])
    if inp == "Ivan":
        print(f"Hello,{inp}")
        print("Your rating:" + str(rat_I))

    if inp == "Anna":
        print(f"Hello,{inp}")
        print("Your rating:" + str(rat_An))

    if inp == "Alexey":
        print(f"Hello,{inp}")
        print("Your rating:" + str(rat_A))

    rpg(inp)




def rat(inp,i):
    with open("rating.txt", "r") as file:
        names = file.readlines()
        str1 = names[0]
        str2 = names[1]
        str3 = names[2]
        str1_1 = str1.split(" ")
        rat_I = int(str1_1[1])
        str2_2 = str2.split(" ")
        rat_An = int(str2_2[1])
        str3_3 = str3.split(" ")
        rat_A = int(str3_3[1])
    if inp == "Ivan":
        rat_I_tot = rat_I + i
        print("Your rating:" + str(rat_I_tot))

    if inp == "Anna":
        rat_An_tot = rat_An + i
        print("Your rating:" + str(rat_I_tot))

    if inp == "Alexey":
        rat_A_tot = rat_A + i
        print("Your rating:" + str(rat_I_tot))

    game_s()


def rpg(inp):
    while True:

        comp = str(random.choice(variant))
        print(comp)
        player = str(input())
        i = 0
        if player != variant:
            print("Invalid key")
        if player == "rog" and (comp == "fire" or comp == "scissors" or comp == "sponge"):
            print("Well Done.The computer chose " + comp + " and failed\n")
            i += 100

        elif player == "paper" and (comp == "rog" or comp == "air" or comp == "water"):
            print("Well Done.The computer chose " + comp + " and failed\n")
            i += 100

        elif player == "scissors" and (comp == "air" or comp == "paper" or comp == "sponge"):
            print("Well Done.The computer chose " + comp + " and failed\n")
            i += 100

        elif player == "sponge" and (comp == "paper" or comp == "air" or comp == "water"):
            print("Well Done.The computer chose " + comp + " and failed\n")
            i += 100

        elif player == "air" and (comp == "rog" or comp == "fire" or comp == "water"):
            print("Well Done.The computer chose " + comp + " and failed\n")
            i += 100

        elif player == "water" and (comp == "rog" or comp == "fire" or comp == "scissors"):
            print("Well Done.The computer chose " + comp + " and failed\n")
            i += 100

        elif player == "fire" and (comp == "paper" or comp == "sponge" or comp == "scissors"):
            print("Well Done.The computer chose " + comp + " and failed\n")
            i += 100

        elif player == comp:
            print("There is draw " + comp + "\n")
            i += 50

        else:
            print("Sorry, but the computer chose " + comp + "\n")

        rat(inp,i)
        break


def game_s():
    while True:
        print("""Что ты хочешь сделать 
        "play" 
        "exit" """)
        choice = input()
        if choice == 'play':
            inp = input()
            choose_rat(inp)

        elif choice == 'exit':

            print("Bye\n")
            break
        elif choice.isnumeric():
            print("Введите буквы")
            game_s()
        elif choice != 'play' or choice != 'exit':
            print("Invalid input")
            game_s()


game_s()