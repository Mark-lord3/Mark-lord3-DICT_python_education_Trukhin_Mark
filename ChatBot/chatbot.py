print("Hello !My name is ChatBot")
print("I was created in 2021")
print("Please,remind me your name.")
a = input()
print("what a great name you have,"+a)
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

re3 = int(input())
re5 = int(input())
re7 = int(input())
age = (re3 * 70 + re5 * 21 + re7 * 15) % 105
print("Your age is"+str(age)+"; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
d=int(input())
i=0
while(i<d):
    print("!"+i)
    i+=1


print("Completed, have a nice day!")
