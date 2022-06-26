import requests
import json


def first_part():
    print("Please, enter the number of mycoins you have:")
    my_c = float(input())
    print("Please, enter the exchange rate:")
    my_r = float(input())
    res_r_c = my_c * my_r
    print(f'The total amount of dollars:{res_r_c}')


first_part()

dict = {"peso": 0.82, "lempira": 0.17, "avdollar": 1.9622, "dirham": 0.208}


def second_part():
    my_c = float(input())
    r_p = my_c * dict.get("peso")
    print(f'I will get {round(r_p, 2)} ARS from the sale of {my_c} mycoins.')

    r_l = my_c * dict.get("lempira")
    print(f'I will get {round(r_l, 2)} NHL from the sale of {my_c} mycoins.')

    r_ad = my_c * dict.get("avdollar")
    print(f'I will get {round(r_ad, 2)} AUD from the sale of {my_c} mycoins.')

    r_d = my_c * dict.get("dirham")
    print(f'I will get {round(r_d, 2)} MAD from the sale of {my_c} mycoins.')


second_part()

inp1 = 0
inp2 = 0


def third_part():
    inp1 = 'usd'
    inp2 = 'eur'
    user_inp = input()
    dict_U = requests.get('http://www.floatrates.com/daily/' + user_inp + '.json')
    with open('usd.json', 'w') as file:
        json.dump(dict_U.json(), file)
    with open('usd.json', 'r') as file:
        for line in file:
            string = line
        dict_j1 = json.loads(string)

    rate = float(dict_j1[inp1]['rate'])
    count = float(input())
    print('You received ' + str(round(rate * count, 2)) + ' ' + inp1)
    dict_E = requests.get('http://www.floatrates.com/daily/' + user_inp + '.json')
    with open('eur.json', 'w') as file:
        json.dump(dict_E.json(), file)
    with open('eur.json', 'r') as file:
        for line in file:
            string = line
        dict_j2 = json.loads(string)
    rate = float(dict_j2[inp2]['rate'])
    count = float(input())
    print('You received ' + str(round(rate * count, 2)) + ' ' + inp2)


third_part()

cache_u = {}
dict_js = {}
user_i = input()
user_i1 = 0


def fourth_part():
    def req():
        global dict_js
        dict_0 = requests.get('http://www.floatrates.com/daily/' + user_i + '.json')
        with open('a.json', 'w') as file:
            json.dump(dict_0.json(), file)
        with open('a.json', 'r') as file:
            for line in file:
                string = line
            dict_js = json.loads(string)

    def cache_write():
        with open('cache.txt', 'w') as file:
            for key, values in cache_u.items():
                file.write(f'{key},{values},\n')

    def cache_read():
        try:
            with open('cache.txt', 'r') as file:
                for line in file:
                    key, values, trash = line.split(',')
                    cache_u[key] = values
        except ValueError:
            ...

    cache_read()
    while True:
        user_i1 = input()
        if user_i1 == '':
            cache_write()
            break
        count_money = int(input())
        pair = (user_i + '-' + user_i1)
        r_pair = (user_i1 + '-' + user_i)
        print('Checking the cache... ')
        try:
            if pair in cache_u:
                print('It is in the cache!')
                rate = float(cache_u[pair])
            elif r_pair in cache_u:
                print('It is in the cache!')
                rate = 1 / float(cache_u[r_pair])
            else:
                print('Sorry, but it is not in the cache!')
                if dict_js == {}:
                    req()
                    rate = float(dict_js[user_i1]['rate'])
                    cache_u[pair] = rate
                else:
                    rate = float(dict_js[user_i1]['rate'])
                    cache_u[pair] = rate
        except KeyError:
            print('Invalid input. Try again')
            continue
        print('You received ' + str(round(rate * count_money, 2)) + ' ' + str(user_i1))


fourth_part()
