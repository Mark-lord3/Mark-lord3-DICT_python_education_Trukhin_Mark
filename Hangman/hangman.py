import random

print('''HANGMAN - best game in the world''')

old_list = ['python', 'java', 'javascript', 'php']




tries = 0


def restart():
    restart_string = str(input('Type "play" to play the game, "exit" to quit: '))
    if restart_string == 'play':
        start_game()
    elif restart_string == 'exit':
        print('Have a nice day :)')
    else:
        print('Pls, try again')
        restart()


def start_game():
    global tries, old_list
    word = random.choice(old_list)
    sliced_word = list(word)
    searched = ['-' for letter in sliced_word]
    tries = 8
    print('''Game started!''')
    while True:
        if tries <= 0:
            print('You LOST!')
            tries = 8
            restart()
            break
        print(' '.join(searched))
        print('Tries - ' + str(tries))
        letter = input('Write a letter: ').strip(' ')
        len_of_letter = len(letter)
        if letter.isalpha():
            if letter.islower():
                if len_of_letter == 1:
                    if letter in sliced_word:
                        for i, c in enumerate(sliced_word):
                            if letter in searched[i]:
                                tries -= 1
                                print('You\'ve already guessed this letter.')
                                continue
                            if letter == c:
                                searched[i] = letter
                            if '-' not in searched:
                                print('YOU WORD: ' + ' '.join(searched))
                                print('''Thanks for playing!  We'll see how well you did in the next stage''')

                                restart()
                                break
                    elif letter not in sliced_word:
                        tries -= 1
                        print('That letter doesn\'t appear in the word')
                        continue
                else:
                    print('You should input a single letter.')
            else:
                print('Please enter a lowercase English letter.')
        else:
            print('Please enter a lowercase English letter.')


start_game()