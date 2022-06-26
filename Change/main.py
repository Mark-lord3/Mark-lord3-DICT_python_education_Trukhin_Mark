import requests
import json


def first_part():
    print("Please, enter the number of mycoins you have:")
    my_c=float(input())
    print("Please, enter the exchange rate:")
    my_r = float(input())
    res_r_c=my_c*my_r
    print(f'The total amount of dollars:{res_r_c}')
first_part()

dict={"peso":0.82,"lempira":0.17,"avdollar":1.9622,"dirham":0.208}

def second_part():
    my_c=float(input())
    r_p=my_c*dict.get("peso")
    print(f'I will get {round(r_p,2)} ARS from the sale of {my_c} mycoins.')

    r_l = my_c * dict.get("lempira")
    print(f'I will get {round(r_l,2)} NHL from the sale of {my_c} mycoins.')

    r_ad = my_c * dict.get("avdollar")
    print(f'I will get {round(r_ad,2)} AUD from the sale of {my_c} mycoins.')

    r_d = my_c * dict.get("dirham")
    print(f'I will get {round(r_d,2)} MAD from the sale of {my_c} mycoins.')

second_part()

