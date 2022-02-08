import math

# print("""Loan principal: 1000
# Month 1: repaid 250
# Month 2: repaid 250
# Month 3: repaid 500
# The loan has been repaid!""")
#
# print("Enter the loan principal:")
# loan = int(input())
# print("""What do you want to calculate?
# type "m" – for number of monthly payments,
# type "p" – for the monthly payment:""")
# type1 = str(input())
#
#
# def count_pay():
#     if type1 == "m":
#         cout_of_month = 0
#         print("Enter the monthly payment:")
#         payment = int(input())
#         cout_of_month = math.ceil(loan / payment)
#         print("It will take " + str(cout_of_month) + " months to repay the loan")
#     if type1 == "p":
#         print("Enter the number of months")
#         month = int(input())
#         pay = math.ceil(loan / month)
#         last_pay = loan - (month - 1) * pay
#
#         if last_pay != pay:
#             print("Your monthly payment = " + str(pay) + " and the last payment = " + str(last_pay) + ".")
#
#         else:
#             print("Your monthly payment = " + str(pay))
#
#
# count_pay()
#
# print("""What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:""")
#
# type1 = str(input())
#
#
# def inter():
#     if type1 == "n":
#         print("Enter the loan principal:")
#         paymant = int(input())
#         print("Enter the monthly payment:")
#         mon_pay = int(input())
#         print("Enter the loan interest:")
#         lo_int = int(input())
#         i = lo_int / (12 * 100)
#         n = math.ceil(math.log(mon_pay / (mon_pay - i * paymant), 1 + i))
#         l = math.trunc(n / 12)
#
#         z = n - l * 12
#         print("It will take " + str(l) + " years and " + str(z) + " months to repay this loan!")
#
#     if type1 == "a":
#         print("Enter the loan principal:")
#         paymant = int(input())
#         print("Enter the number of periods:")
#         period = int(input())
#         print("Enter the loan interest:")
#         lo_int = int(input())
#         i = lo_int / (12 * 100)
#         mon_pay = math.ceil((paymant * i * ((1 + i) ** period)) / (((1 + i) ** period) - 1))
#         print("Your monthly payment =" + str(mon_pay) + "")
#     if type1 == "p":
#         print("Enter the annuity payment:")
#         a_paymant = float(input())
#         print("Enter the number of periods:")
#         period = int(input())
#         print("Enter the loan interest:")
#         lo_int = float(input())
#         i = lo_int / (12 * 100)
#         loan = math.trunc(a_paymant * ((1 + i) ** period - 1) / (i * (1 + i) ** period))
#         print("Your loan principal = " + str(loan) + "!")
#
#
# inter()
import argparse


def de_f():
    parser = argparse.ArgumentParser(description='A tutorial')
    parser.add_argument("--type", type=str)
    args1 = parser.parse_args()

    parser.add_argument("--principal", type=int)
    args2 = parser.parse_args()

    parser.add_argument("--periods", type=int)
    args3 = parser.parse_args()

    parser.add_argument("--interest", type=float)
    args4 = parser.parse_args()
    if (args1 == "diff"):
        i = args4 / (12 * 100)
        z = 0
        for n in range(args3):
            dif = math.ceil(args1 / args3 + i * (args2 - (args2 * ((n + 1) - 1)) / args3))
            print("Month" + str(n + 1) + ":" + "payment is " + str(dif))
            z += dif
        over = z - args2
        print("Overpayment =" + str(over))
    else:
        print("invalid key")
de_f()

# def de_f():
#     p = int(input())
#     m = int(input())
#     l_i = float(input())
#
#     i = l_i / (12 * 100)
#     z = 0
#     for n in range(m):
#         dif = math.ceil(p / m + i * (p - (p * ((n+1) - 1)) / m))
#         print("Month" + str(n+1) + ":" + "payment is " + str(dif))
#         z += dif
#     over = z - p
#     print("Overpayment =" + str(over))
# de_f()
