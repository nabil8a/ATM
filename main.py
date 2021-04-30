import datetime
import time
allowedUsers = ["nail","ross","rossa",]
allowedPassword = ["me","guest","manager"]
balance =[20.00,20.00,20.00]
optionList = ["Withdrawal","Cash Deposit","Complaint","Loggout"]
userId = int()
def Withdrawal(userId):
    print("Withdrawal")
    balance[userId] -= float(input("How much would you like to withdraw \n"))
    print("Please take your Cash")
    time.sleep(3)

def Deposit(userId):
    print("Cash Deposit")
    balance[userId] += float(input("How much would you like to deposit? \n"))
    print("You now Have $%s" %balance[userId])
    time.sleep(3)

def Complaint():
    print("Complaint")
    input("What issue will you like to report?")
    print("Thank you for contacting us")
    time.sleep(3)

def mainMenu():
    global userId
    now = datetime.datetime.now()
    print("Wellcome %s" % (allowedUsers[userId]), now.strftime("%x " + "%H"":""%M %p"),"\nthese are the available options")
    for i in range(len(optionList)):
        print(i+1,optionList[i])

    selectedOption = int(input("Please select an option \n"))
    if(selectedOption == 1): #Withdrawal
        Withdrawal(userId)

    elif(selectedOption == 2): #Deposit
        Deposit(userId)
    elif(selectedOption == 3): #Complaint
        Complaint()
    elif(selectedOption == 4):
        userId = int(-1)
        logIn()
    else:
        print("Invalid option selected, Please try again")

def logIn():
    global userId
    name = input("what is your name? \n")
    if (name in allowedUsers):
        password = input("Enter your password \n")
        if(password in allowedPassword):
            userId = allowedUsers.index(name)
        else:
            print("wrong Password")
            logIn()
    else:
        print("Name not found, Please try again")
        logIn()

while True:
    logIn()
    while True:
        mainMenu()