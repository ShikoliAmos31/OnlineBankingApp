import math
print("Welcome to the Online Banking Application")
def signin():
    global name #username
    global pin #password
    global cb #current balance
    name = str(input("Please create your username: "))
    pin = str(input("Please create your pasword: "))
    if len(pin) == 6:
        pin = pin 
        print("Thank you for creating your bank account!")
    else:
        print("The pin has to be 6 digidts")
        newpin = str(input("Please create your 6 digits pin: "))
        if len(newpin) != 6:
            print("The pin has to be 6 digits long: ")
            signin()
        else:
            pin = newpin
            
def forgetpin():
    recoverpin = str(input("Please create your new 6 digits pin: "))
    if len(recoverpin) != 6:
        print("The pin has to be 6 digits: ")
        forgetpin()
    else:
        print("The new pin has been reseted, Please login: ")
        pin = recoverpin
        login()
        
def depositinterest(p,r,t):             
 # A = Pe^(rt) compound interest formula
 p = float(p)
 r = float(r)
 t = float(t)
 rt = r * t
 e = math.exp(rt)
 #calculations
 a = p * e #investment future value
 return a

def login():
    #name1 represent the username
    #pin1 represent the user pin
    name1 = str(input("Please enter your username: "))
    pin1 = str(input("Please enter your pin: "))
    #check if the pin and the name matches
    if name1 == name and pin1 ==pin:
        print("Welcome to online banking" + " " + name)
        print("Please choose from the menu below!:")
        listmenu =["1-Deposit", "2-Withdaw", "3-Transfer Money", "4-Check Balance", "5-Deposit Interest", "6-Calculate Compound Interest"]
        #deposit money
        for i in listmenu:
            print(i)
        choose = int(input("Please enter your choice: "))
        d = 0 #deposit
        w = 0 #withdraw
        cb = 0 #current balance
        if choose == 1:
            d = int(input("Please enter the amount you want to deposit: "))
            cb = d
            print("You curren balance is" +" "+ str(cb) +" "+ "Thanky you for banking with us. ")
        #withdraw money logics
        elif choose == 2:
            w = int(input("Please enter the amoubt you want to withdraw: "))
            if w > cb:
                print("Insufficient funds in your account")
                login()
            else:
                cb = d-w
                print(str(w) +" "+ "has been withdrawn from your account" +" "+ "your current balance is" + " " + str(cb))
            #transfer money logics
        elif choose == 3:
            dest = str(input("Please enter the account number you want to transfer money to in 8 digits: "))
            if len(dest) == 8:
                amount = int(input("Please enter the amount you want to transfer: "))
                if amount > cb:
                    print("Insufficient funds in your account.")
                    login()
                else:
                    cb = cb - amount
                    print("The transaction of" + " " + str(amount) + " " + "has been made to" + " " + str(dest) + " " + "your current balance is" + " " + str(cb))
            else:
                print("Invalid account number the acount number has to be 8 digits")
                login()
        #checking the balance logics
        elif choose == 4:
            print("Your current balance is: " + " " + str(cb))
            
        #deposit interest logics
        elif choose == 5:
            if d > 50000:
                rate = 3
            elif d > 30000:
                rate = 2
            else:
                rate = 1.5
            print("Your deposit interest rate is: " + " " + str(rate) + "%")
        #compound interest rates logics
        elif choose == 6:
            listoption = ["1-Calculate your deposit compound interest based on your current balance", "2-Calculate your deposit compound interest based on youur deposit amount "]
            for n in listoption:
                print(n)
            choice = int(input("Please enter your choice from the above: "))
            if choice == 1:
                timing = str(input("Please enter the years you want to invest the money: "))
                if d > 50000:
                    rate = 3/100
                elif d > 30000:
                    rate = 2/100
                else:
                    rate = 1.5/100
                print("Your current balance in" + " " + "timing" + " " + "Years will be: ")
                print(depositinterest(cb, rate, timing))
            elif choice == 2:
                timing1 = str(input("Please enter the years you want to invest the money: "))
                money = str(input("Please enter the amount of money you want to deposit: "))
                money = int(money)
                if d > 50000:
                    rate = 3/100
                elif d > 30000:
                    rate = 2/100
                else:
                    rate = 1.5/100
                print("Your current balance in" + " " + "timing" + " " + "Years will be: ")
                print(depositinterest(money, rate, timing))
        else:
            print("Invalid choice, back to the main menu")
            login()
            
    else:
        print("Either the username or the pin is incorrect, did you create your account?: ")
        list1 = ["1-Yes", "2-No"]
        for i in list1:
            print(i)
        input = int(input("Enter your choice below"))
        if input == 1:
            list2 = ["1-do you want to attempt log in again?: ", "2-you forgot your pin: "]
            for e in list2:
                print(e)
            theanswer = str(input("Please enter your choice: "))
            theanswer = int(theanswer)
            if theanswer == 1:
                login()
            elif theanswer == 2:
                forgetpin()
            else:
                print("Invalid choice")
                login()
                
        elif input == 2:
            print("Please create your account")
            signin()
    exit()
          
def mainmenu():
    optionone = int(input("Choose 1 to sign in and choose 2 to login: "))
    if optionone == 1:
        signin()
    elif optionone == 2:
        login()
    else:
        print("Invalid choice")
        mainmenu()
    exit()
    
def exit():
    answer = str(input("Do you want to continue with the transaction? Yes or No: "))
    if answer == "Yes":
        login()
    elif answer == "No":
        print("Thank you for banking with us")
    else:
        print("Invalid choice")
        mainmenu()
        
mainmenu()