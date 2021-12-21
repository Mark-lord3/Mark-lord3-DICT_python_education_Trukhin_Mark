class interface:
    def fir(self):
        print("Starting to make a coffee")
        print("Grinding coffee beans")
        print("Boiling water")
        print("Mixing boiled water with crushed coffee beans")
        print("Pouring coffee into the cup")
        print("Pouring some milk into the cup")
        print("Coffee is ready!")

    def sec(self):
        print("Write how many cups of coffee you will need:")
        a = int(input())
        print("For " + str(a) + " cups of coffee you will need:")
        b = a * 200
        c = a * 50
        d = a * 15
        print(str(b) + " ml of water")
        print(str(c) + " ml of milk")
        print(str(d) + " g of coffee beans")
    def thi(self):
        print("Write how many ml of water the coffee machine has:")
        a = int(input())
        print("Write how many ml of milk the coffee machine has:")
        b = int(input())
        print("Write how many grams of coffee beans the coffee machine has:")
        c = int(input())
        print("Write how many cups of coffee you will need:")
        d = int(input())
        z = int(a / 200)
        y = int(b / 50)
        f = int(c / 15)
        if min(z, y, f) == d:
            print("Yes, I can make that amount of coffee")
        elif min(z, y, f) < d:

            print("No, I can make only " + str(min(z, y, f)) + " cups of coffee")
        elif min(z, y, f) > d:
            k = min(z, y, f) - d
            print("Yes, I can make that amount of coffee (and even " + str(k) + " more than that)")


    def uf(self,second,w,m,c,d,o):

            if (second == 1):
                w = w - 250
                m = m
                c = c - 16
                d = d - 1
                o = o + 4
                print("The coffee machine has:\n" + str(w) + " of water\n" + str(m) + " of milk\n" + str(
                c) + " of coffee beans\n" + str(d) + " of disposable cups\n" + str(o) + " of money")

            if (second == 2):
                w = w - 350
                m = m - 75
                c = c - 20
                d = d - 1
                o = o + 7
                print("The coffee machine has:\n" + str(w) + " of water\n" + str(m) + " of milk\n" + str(
                    c) + " of coffee beans\n" + str(d) + " of disposable cups\n" + str(o) + " of money")

            if (second == 3):
                w = w - 200
                m = m - 100
                c = c - 12
                d = d - 1
                o = o + 6
                print("The coffee machine has:\n" + str(w) + " of water\n" + str(m) + " of milk\n" + str(
                    c) + " of coffee beans\n" + str(d) + " of disposable cups\n" + str(o) + " of money")



    def main(self):

        self.fir()
        self.sec()
        self.thi()

        w = 400
        m = 540
        c = 120
        d = 9
        o = 550
        print(
            "The coffee machine has:\n " + str(w) + " of water\n" + str(m) + " of milk\n" + str(
                c) + " of coffee beans\n" + str(
                d) + " of disposable cups\n" + str(o) + " of money")
        print("Нажмите на кнопки для продолжения работы:0-Exit;1-Buy ;2-Fill ;3-Take;")
        first = int(input())
        while (first != 0):
            print("Нажмите на кнопки для продолжения работы:0-Exit;1-Buy ;2-Fill ;3-Take;")
            first = int(input())

            if(first==0):
                break


            if (first == 1):
                print("Выберите тип кофе:1-Эспрессо;2-Латте;3-Капучино.")
                second = int(input())
                self.uf(second,w,m,c,d,o)



            if (first == 2):
                print("Сколько воды ,молока,зерен,стаканчиков вы хотите добавить");
                v = int(input())
                w = w + v
                mol = int(input())
                m = m + mol
                bob = int(input())
                c = c + bob
                stak = int(input())
                d = d + stak
                print("The coffee machine has:\n" + str(w) + " of water\n" + str(m) + " of milk\n" + str(
                    c) + " of coffee beans\n" + str(d) + " of disposable cups\n" + str(o) + " of money")

            if (first == 3):
                print("I gave you: " + str(o));
                o = o - o
                print("The coffee machine has:\n" + str(w) + " of water\n" + str(m) + " of milk\n" + str(
                    c) + " of coffee beans\n" + str(d) + " of disposable cups\n" + str(o) + " of money")


m=interface()

m.main()


water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def first():
    print("Starting to make a coffee")
    print("Grinding coffee beans")
    print("Boiling water")
    print("Mixing boiled water with crushed coffee beans")
    print("Pouring coffee into the cup")
    print("Pouring some milk into the cup")
    print("Coffee is ready!")

def remaining():
    print('The coffee machine has:')
    print(str(water) + ' of water')
    print(str(milk) + ' of milk')
    print(str(coffee_beans) + ' of coffee beans')
    print(str(cups) + ' of disposable cups')
    print(str(money) + ' of money')


def enough():
    global water, milk, coffee_beans, cups
    if water < 0:
        return "Sorry, not enough water"
    elif milk < 0:
        return "Sorry, not enough milk"
    elif coffee_beans < 0:
        return "Sorry, not enough coffee_beans"
    elif cups < 0:
        return "Sorry, not enough disposable cups"


def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:')
    global water, milk, coffee_beans, money, cups
    answer_user = input()
    if answer_user == str(1):
        water -= 250
        coffee_beans -= 16
        cups -= 1
        money += 4
        if enough() == None:
            print('I have enough resources, making you a coffee!')
        else:
            print(enough())
        return 'espresso'
    elif answer_user == str(2):
        water -= 350
        milk -= 75
        coffee_beans -= 20
        cups -= 1
        money += 7
        if enough() == None:
            print('I have enough resources, making you a coffee!')
        else:
            print(enough())
        return 'latte'
    elif answer_user == str(3):
        water -= 200
        milk -= 100
        coffee_beans -= 12
        cups -= 1
        money += 6
        if enough() == None:
            print('I have enough resources, making you a coffee!')
        else:
            print(enough())
        return 'cappuccino'
    elif answer_user == 'back':
        return 'back'


def fill():
    global water, milk, coffee_beans, money, cups
    print("Write how many ml of water you want to add:")
    add_water = int(input())
    water += add_water
    print("Write how many ml of milk you want to add:")
    add_milk = int(input())
    milk += add_milk
    print("Write how many grams of coffee beans you want to add:")
    add_coffee_beans = int(input())
    coffee_beans += add_coffee_beans
    print("Write how many disposable coffee cups you want to add:")
    add_cups = int(input())
    cups += add_cups


def take():
    global money
    print("I gave you " + str(money))
    money = 0


def action():
    print('\nWrite action (buy, fill, take, remaining, exit):')
    action_user = str(input())
    if action_user == 'buy':
        print('')
        buy()
        return 'buy'
    elif action_user == 'fill':
        print('')
        fill()
        return 'fill'
    elif action_user == 'take':
        take()
        return 'take'
    elif action_user == 'remaining':
        print('')
        remaining()
        return 'remaining'
    elif action_user == 'exit':
        return 'exit'


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def remaining(self):
        print('The coffee machine has:')
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.coffee_beans) + ' of coffee beans')
        print(str(self.cups) + ' of disposable cups')
        print(str(self.money) + ' of money')

    def enough(self):
        global water, milk, coffee_beans, cups
        if self.water < 0:
            return "Sorry, not enough water"
        elif self.milk < 0:
            return "Sorry, not enough milk"
        elif self.coffee_beans < 0:
            return "Sorry, not enough coffee_beans"
        elif self.cups < 0:
            return "Sorry, not enough disposable cups"

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:')
        global water, milk, coffee_beans, money, cups
        answer_user = input()
        if answer_user == str(1):
            self.water -= 250
            self.coffee_beans -= 16
            self.cups -= 1
            money += 4
            if enough(self) == None:
                print('I have enough resources, making you a coffee!')
            else:
                print(enough(self))
            return 'espresso'
        elif answer_user == str(2):
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.cups -= 1
            self.money += 7
            if enough(self) is None:
                print('I have enough resources, making you a coffee!')
            else:
                print(enough(self))
            return 'latte'
        elif answer_user == str(3):
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.cups -= 1
            self.money += 6
            if enough(self) is None:
                print('I have enough resources, making you a coffee!')
            else:
                print(enough(self))
            return 'cappuccino'
        elif answer_user == 'back':
            return 'back'

    def fill(self):
        global water, milk, coffee_beans, money, cups
        print("Write how many ml of water you want to add:")
        add_water = int(input())
        self.water += add_water
        print("Write how many ml of milk you want to add:")
        add_milk = int(input())
        self.milk += add_milk
        print("Write how many grams of coffee beans you want to add:")
        add_coffee_beans = int(input())
        self.coffee_beans += add_coffee_beans
        print("Write how many disposable coffee cups you want to add:")
        add_cups = int(input())
        self.cups += add_cups

    def take(self):
        global money
        print("I gave you " + str(money))
        money = 0

    def action(self):
        print('\nWrite action (buy, fill, take, remaining, exit):')
        action_user = str(input())
        if action_user == 'buy':
            print('')
            objects.buy()
            return 'buy'
        elif action_user == 'fill':
            print('')
            objects.fill()
            return 'fill'
        elif action_user == 'take':
            objects.take()
            return 'take'
        elif action_user == 'remaining':
            print('')
            objects.remaining()
            return 'remaining'
        elif action_user == 'exit':
            return 'exit'


objects = CoffeeMachine()

while_action = 0

while while_action != 'exit':
    while_action = action()

