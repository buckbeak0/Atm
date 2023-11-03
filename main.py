import os
import pickle
import getpass
import random

accounts_file = "accounts.dat"

try:
    f = open(accounts_file, "rb")
    accounts = pickle.load(f)
except (FileNotFoundError, EOFError):
    accounts = {}

while True:
    os.system("cls")

    print("*******************************************************************")
    print("*                                                                 *")
    print("*                   Welcome to ATM (SOME BANK)                    *")
    print("*                                                                 *")
    print("*******************************************************************\n")

    print("=" * 20, "Main Menu", "=" * 89)
    print("     >>> 1 To Insert Card number")
    print("     >>> 2 To Create Account")
    print("     >>> 0 To Exit")
    print("=" * 120)
    ch = int(input("        >>>Enter choice :- "))
    print("=" * 120)
    if ch == 1:
        card = input("      >>>Enter Card Number :- ")
        print("=" * 120)
        if card in accounts.keys():
            account = accounts[card]

        else:
            print("*" * 120)
            print("     *No card found*")
            print("*" * 120)
            continue
        if account["lock"]:
            print("     >>> Your card is locked cannot access!!!")
            continue
        for i in range(3):
            pin = getpass.getpass("       >>> Enter 4 digit pin :- ")
            if pin != account["pin"]:
                print("     >>> Pin incorrect!!!, ", i + 1, "attempts left")
            else:
                break
        else:
            print("     >>> All attempts failed!, Card locked!")
            input("     >>> Press enter to continue")
            account["lock"] = True
            accounts[card] = account
            f = open(accounts_file, "wb")
            pickle.dump(accounts, f)
            f.close()
            continue
        print("=" * 120)
        while True:
            os.system("cls")
            print("     >>> Welcome", account["name"])
            print("\n     >>> What would you like to do?")
            print("     >>> 1 To Withdraw money")
            print("     >>> 2 To Deposit money")
            print("     >>> 3 To Check balance")
            print("     >>> 4 To Change pin")
            print("     >>> 0 TO exit")
            ch = input("        >>>Enter choice :- ")
            if ch == 1:
                if account["balance"] == 0:
                    print("     >>> 0 balance!!!")
                    continue
                print("="*120)
                while True:
                    try:
                        amt = float(input("     >>> Enter amount to withdraw :- "))
                    except ValueError:
                        print("     *Invalid input please enter a valid amount*")
                        continue
                    if account["balance"] > amt:
                        c = input("     >>> Confirm withdrawal?(y) :- ")
                        if c.lower() == "y":
                            account["balance"] -= amt
                            accounts[card] = account
                            f = open(accounts_file, "wb")
                            pickle.dump(accounts, f)
                            f.close()
                            print("     >>> Amount withdrawn")
                            print("="*120)
                            break
                        else:
                            break

            elif ch == 2:
                print("=" * 120)
                while True:
                    try:
                        amt = int(input("       >>> Enter amount to deposit :- "))
                    except ValueError:
                        print("     *Invalid input please enter a valid amount*")
                    c = input("     >>> Confirm deposit? (y) :- ")
                    if c.lower() == "y":
                        account["balance"] += amt
                        accounts[card] = account
                        f = open(accounts_file, "wb")
                        pickle.dump(accounts, f)
                        f.close()
                        break
                print("     >>> Amount deposited")

            elif ch == 3:
                print("="*120)
                print("     >>> Balance :- ", account["balance"])
                print("="*120)
                input("     >>> Press enter to continue")

            elif ch == 4:
                print("="*120)
                old_pin = getpass.getpass("     >>> Enter current pin :- ")
                if old_pin == account["pin"]:
                    new_pin = getpass.getpass("     >>> Enter new pin :- ")
                    check = getpass.getpass("       >>> Re enter new pin :- ")
                    if new_pin == check:
                        account["pin"] = new_pin
                        f = open(accounts_file, "wb")
                        pickle.dump(accounts, f)
                        f.close()
                        print("     >>> Pin changed!")
                        input("     >>> Press enter to continue")
                else:
                    continue

    elif ch == 2:
        name = input("      >>>Enter name :- ").strip()
        for i in range(3):
            try:
                pno = input("       >>>Enter phone number :- ")
            except ValueError:
                print("     *INVALID INPUT!!! TRY AGAIN,", i + 1, "attempts left*")
                continue
            if len(pno) == 10 and pno.isdigit():
                break
            else:
                print("     *INVALID INPUT!!! TRY AGAIN,", i + 1, "attempts left*")
        else:
            continue
        temp = True
        while temp:
            try:
                age = int(input("       >>>Enter age :- "))
            except ValueError:
                print("     *INVALID INPUT!!! TRY AGAIN", i + 1, "attempts left*")
            if age >= 18:
                break
            else:
                print("     *Not eligible*")
                temp = False
        else:
            continue
        print("=" * 120)
        print("     >>> Generating card.....")
        card = ""
        while True:
            for i in range(5):
                x = random.randint(0, 9)
                card += str(x)
            if card not in accounts:
                break
        print("     >>> Your card number is :- ", "\""+card+"\"")
        print("     >>> Must remember!!!")
        print("     >>> Generating 4 digit pin.....")
        pin = ""
        for i in range(4):
            x = random.randint(0, 9)
            pin += str(x)
        print("     >>> Your 4 digit pin is :- ", pin)
        print("     >>> Must remember and do not share!!!")
        print("=" * 120)
        c = input("     >>> Confirm? (y) :- ")
        if c.lower() == "y":
            print("=" * 120)
            print("     >>> Creating account....")
            print("     >>> Name :- ", name)
            print("     >>> Phone number :- ", pno)
            print("     >>> Age :- ", age)
            print("     >>> Card number :- ", card)

            account = {
                "name": name,
                "age": age,
                "phone number": pno,
                "pin": pin,
                "balance": 0,
                "lock": False
            }
            accounts[card] = account
            f = open(accounts_file, "wb")
            pickle.dump(accounts, f)
            f.close()
            print("     >>> Account created with 0 balance!")
            input("     >>> Press enter to continue")
