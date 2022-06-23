from random import choice
first_choice = 0
second_choice = 0
result = 0
c = 0
arguments = 0
level = 0
second = 0
mark = 0


def simple():
    global first_choice, second_choice, arguments
    first_choice = choice(range(2, 10))
    second_choice = choice(range(2, 10))
    arguments = choice(['+', '-', '*'])


def integral():
    global second, result
    second = choice(range(11, 30))
    result = second ** 2
    print(second)


def res_Print():
    global result, first_choice, second_choice, arguments
    simple()
    if arguments == '+':
        print(str(first_choice) + ' + ' + str(second_choice))
        result = first_choice + second_choice
    elif arguments == '-':
        print(str(first_choice) + ' - ' + str(second_choice))
        result = first_choice - second_choice
    elif arguments == '*':
        print(str(first_choice) + ' * ' + str(second_choice))
        result = first_choice * second_choice


def results(an):
    global mark, c
    if result == an:
        print('Right!')
        mark += 1
        c += 1
    else:
        print('Wrong!')
        c += 1


def Start(lev):
    while c != 5:
        try:
            if lev == 1:
                res_Print()
                answer = int(input())
                results(answer)
            elif lev == 2:
                integral()
                answer = int(input())
                results(answer)
        except ValueError:
            print('Incorrect format')
    print('Your mark is ' + str(mark) + '/5')
    print("Would you like to save the result? Enter yes or no.")
    answer_file = input()
    Save_ToFile(answer_file)


def Save_ToFile(answer_file):
    if answer_file == 'YES' or 'Yes' or 'y' or 'yes':
        name = input('What is your name? \n')
        file = open('results.txt', 'a')
        file.write(f'{name}: {mark}/5 in level {level}\n')
        file.close()
        print('The results are saved in "results.txt".')
    # print("Would u like to start game again?")
    # an=input()
    # if an == 'YES' or 'Yes' or 'y' or 'yes':
    #     print("Which level do you want? Enter a number:")
    #     lev = int(input())
    #     Start(lev)


def begin():
    global level
    while level not in [1, 2]:
        try:
            print("Which level do you want? Enter a number:")
            level = int(input())
            Start(level)
        except ValueError:
            print("Incorrect format.")


begin()
