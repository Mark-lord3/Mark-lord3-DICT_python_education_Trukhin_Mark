import random


class DinnerParty:
    def __init__(self, friends, money, lucky):
        self.friends = friends
        self.money = money
        self.lucky = lucky

    def invite(self):
        self.friends = ['Mark', 'm', 'a', 'r', 'k']
        invite_list_amount = int(input('введите количество людей:>>> '))
        print(self.friends[:invite_list_amount])
        if invite_list_amount <= 0:
            print('никто не присоединиться ')
        elif invite_list_amount > 0:
            select = int(input('''Хочешь выбрать счастливчика
                            1 - нет
                            2 - да
                            '''))
            if select == 1:
                print('Все лузеры')
                cash = int(input("Введите количество денег:>>> "))
                amount = cash / invite_list_amount
                sum_true = round(amount, 2)
                for i in range(invite_list_amount):
                    self.money.append(sum_true)
                print(dict(zip(self.friends[:invite_list_amount], self.money)))
            else:
                lucky = random.choice(self.friends[:invite_list_amount])
                print(lucky)
                cash = int(input("Введите колисество денег:>>> "))
                amount = cash / (invite_list_amount - 1)
                sum_true = round(amount, 2)
                clever = self.friends.index(lucky)
                for i in range(invite_list_amount):
                    if i == clever:
                        self.money.append(0)
                    else:
                        self.money.append(sum_true)
                print(dict(zip(self.friends[:invite_list_amount], self.money)))


dinner_party = DinnerParty([], [], 'default')
dinner_party.invite()
