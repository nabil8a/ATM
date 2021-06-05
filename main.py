import datetime
import time
import json
from getpass import getpass
import random
import os

optionList = ["Withdrawal", "Cash Deposit", "Complaint", "Logout"]
userId = '-1'
# bankAccounts = {'000': {"name": "nail", "password": "pass", "Email": "Nail@mail.com", "age": 18, "$": 50.00, 'complaint': {}}}
bankAccounts = {}


def save_file(account_number, user_detail):
    """ f = open("dataSaved.txt", "w")
    f.write(json.dumps(bankAccounts))
    f.close()"""
    f = open('data/%s.txt' % account_number, 'w')
    f.write(json.dumps(user_detail))
    f.close()


def readFile(account_number):
    global bankAccounts
    try:
        f = open('data/%s.txt' % account_number, 'r')
        bankAccounts = json.loads(f.read())
        f.close()
    except FileNotFoundError:
        pass
    finally:
        pass
# except:save_file()
def updateRec(userId):
    f = open('data/%s.txt' %userId, 'w')
    f.write(json.dumps(bankAccounts))
    f.close()

def auth_session(userId,action):
    if action == 'start':
        s = open('data/sessionID_%s.txt' %userId, 'w')
        s.write(userId)
        s.close()
    elif action == 'stop':
        os.remove('data/sessionID_%s.txt' %userId)
    else:
        pass


def Withdrawal(userId):
    print("-----Withdrawal-----")
    print('To go back Enter 0\nyou have $%s in you Account' % bankAccounts[userId]['$'])
    askingnum = float(input("How much would you like to withdraw \n"))
    if askingnum > bankAccounts[userId]['$']:
        print("You can not withdraw more than what you have in your account")
        print('If you would like to take a load Please see our customer service')
        time.sleep(3)
        Withdrawal(userId)
    elif askingnum < 0:
        print('invalid amount to withdraw \n Please try again')
        time.sleep(3)
        Withdrawal(userId)
    elif askingnum <= bankAccounts[userId]['$']:
        bankAccounts[userId]['$'] -= askingnum
        print("Please take your Cash")
        time.sleep(3)
    mainMenu()


def Deposit(userId):
    print("-----Cash Deposit-----")
    print('To Go back Enter 0')
    dep = float(input("How much would you like to deposit? \n"))
    if dep < 0:
        print("you can not deposit %s" % dep)
        time.sleep(3)
        Deposit(userId)
    elif dep >= 0:
        bankAccounts[userId]['$'] += dep
    print("You now Have $%s" % bankAccounts[userId]['$'])
    time.sleep(3)
    mainMenu()


def Complaint(userId):
    print("-----Complaint-----")
    cmplt = input("What issue will you like to report?\n")
    now = datetime.datetime.now()
    tt = now.strftime('%c')
    print(tt)
    bankAccounts[userId]['complaint']["date %s" % tt] = cmplt
    print("Thank you for contacting us")
    time.sleep(3)


def mainMenu():
    global userId
    global bankAccounts
    now = datetime.datetime.now()
    print("Wellcome %s" % (bankAccounts[userId]['name']), now.strftime("%x " + "%H"":""%M %p"),
          "\nthese are the available options")
    for i in range(len(optionList)):
        print(i + 1, optionList[i])
    selectedOption = int(input("Please select an option \n"))
    if selectedOption == 1:  # Withdrawal
        Withdrawal(userId)
    elif selectedOption == 2:  # Deposit
        Deposit(userId)
    elif selectedOption == 3:  # Complaint
        Complaint(userId)
    elif selectedOption == 4:
        updateRec(userId)
        auth_session(userId,'stop')
        userId = int(-1)
        bankAccounts = {}
        homeScreen()
    else:
        print("Invalid option selected, Please try again")


def logIn():
    global userId
    num = input("what is your account #? \n")
    readFile(num)

    if num in bankAccounts.keys():
        password = getpass("Enter your password \n")
        if password == bankAccounts[num]['password']:
            print("yey")
            userId = num
            auth_session(userId,'start')
            mainMenu()
        else:
            print("wrong Password")
            logIn()
    else:
        print("The account Number was not found, Please try again \nOr Register With Us account")

        homeScreen()


def registerAccount():
    name = input("what is your First name \n")
    password = input("choose a New password \n")
    email = input("what is your email Address \n")
    age = int(input("what is your age \n"))
    if age < 18:
        print('YOU CAN NOT REGISTER WITHOUT A GUARDIAN/PARENT')
        time.sleep(4)
        homeScreen()
    mny = int(input("How much would you like to open your account with? \n"))
    accNum = str(len(bankAccounts) + 1) + str(age) + str(random.randrange(100, 999))
    bankAccounts[accNum] = {"name": name, "password": password, "email": email, "age": age, "$": mny, 'complaint': {}}
    print("your account number is %s" % accNum)

    save_file(accNum, bankAccounts)
    logIn()


def homeScreen():
    while True:
        print(' 1. login \n 2. register')
        selectOp = int(input("Please select an option \n"))
        if selectOp == 1:
            logIn()
            mainMenu()
        elif selectOp == 2:
            registerAccount()
        elif selectOp == 0:
            break
        else:
            print("Invalid option")


# readFile()
homeScreen()
