form_com = 'Available formatters: plain, bold, italic, header, link, inline-code, ordered-list, unordered-list, ' \
           'new-line \nSpecial commands: !help !done '
t = 0
t2 = ''


def func(input_str):
    global t, t2
    if input_str == '':
        t2 += ' '
    elif input_str == 'plain':
        t2 += input('Text: > ')
    elif input_str == 'bold':
        t = input('Text: > ')
        t2 += '**' + t + '**'
    elif input_str == 'italic':
        t = input('Text: > ')
        t2 += '*' + t + '*'
    elif input_str == 'header':
        a = 0
        while a != 1:
            try:
                level = int(input('Level: > '))
                if level not in range(1, 5):
                    print('The level should be within the range of 1 to 4. Try again')
                else:
                    t = input('Text: > ')
                    t2 += '#' * level + ' ' + t + '\n'
                    a = 1
            except ValueError:
                print('Value error try to input digits')
    elif input_str == 'link':
        label = input('Label: > ')
        url = input('URL: > ')
        t2 += '\n' + '[' + label + ']' + '(' + url + ')' + '\n'
    elif input_str == 'inline-code':
        t2 += '\n' + '~' + str(input('Enter your code: > ')) + '~' + '\n'
    elif input_str == 'ordered-list':
        a = 0
        while a != 1:
            try:
                nof = int(input('Number of rows: > '))
                if nof > 0:
                    for i in range(1, nof + 1):
                        row = str(input('Row #' + str(i) + ': > '))
                        t2 += str(i) + '. ' + row + '\n'
                        a = 1
                else:
                    print('The number of rows should be greater than zero')
            except ValueError:
                print('Value error try to input digits')
    elif input_str == 'unordered-list':
        a = 0
        while a != 1:
            try:
                nof = int(input('Number of rows: > '))
                if nof > 0:
                    for i in range(1, nof + 1):
                        row = str(input('Row #' + str(i) + ': > '))
                        t2 += '* ' + row + '\n'
                        a = 1
                else:
                    print('The number of rows should be bigger than zero')
            except ValueError:
                print('Value error try to input digits')
    elif input_str == 'new-line':
        t2 += '\n'
    else:
        print('Unknown formatting type or command')


def start():
    input_str = " "
    while input_str != 'done':
        input_str = input('Choose a formatter: > ')
        if input_str == 'help':
            print(form_com)
        elif input_str == 'done':
            print("Thanks for using")
            t3 = open('output.md', 'w')
            t3.write(t2)
            t3.close()
            break
        else:
            func(input_str)
            print(t2)

start()
