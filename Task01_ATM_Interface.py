'''
    TASK:- To Build an ATM Interface which can perform the following operations:
        1. Show the Transactions History
        2. Withdraw Money
        3. Deposit Money
        4. Transfer some amount to another account
        5. Quit
'''
from datetime import datetime

class ATM:
    def __init__(self) -> None:
        print("Welcome to ABC Bank  \n")
        print("Please Insert your card\n")
        self.amount = 100000
        self.dic = {}

    def TransactionHistory(self):
        print("Your Transaction History is : ")
        print(self.dic)
        print("\nBalance = Rs",self.amount)
        print("*******************************************************************************************\n ")

    def withdraw(self):
        money = int(input("Enter amount to be withdrawn : "))
        if(money > self.amount):
            print("Insufficient Balance.")
        else:
            self.amount -= money
            print("Withdraw Successfull.")
            self.dic.update ({datetime.now().strftime("%d/%m/%Y  %H:%M:%S"): (" Withdraw of Rs", money)})
            print("*******************************************************************************************\n ")

    def deposit(self):
        money= int(input("Enter amount to be deposited : "))
        self.amount += money
        print("Deposit Successfull")
        self.dic.update({datetime.now().strftime("%d/%m/%Y  %H:%M:%S") : (" Deposit of Rs", money)})
        print("*******************************************************************************************\n")

    def transfer(self):
        acc = int(input("Enter account number to which you want to transfer the money : "))
        money = int(input("Enter amount to be transfered : "))
        if money > self.amount:
            print("Insufficient Balance!!")
        else:
            self.amount -= money
            print("Transfer Successfull")
            self.dic.update({datetime.now().strftime("%d/%m/%Y  %H:%M:%S") : (" Transfer of Rs ",money," to ",acc)})
            print("*******************************************************************************************\n")


customer = ATM()

def main():

    tries = 3
    flag = False
    while(tries):
        print("Tries left : ", tries)
        pw = int(input("Enter your 4 digit pin number: "))
        if pw == 1234:
            flag = True
            break
        else:
            tries -= 1

    if(flag != True):
        print("Tries over. Try accessing the ATM after 5 minutes. Thank You!")
    else:
        dic = {}

        while(True):
            print("1 : Transaction History")
            print("2 : Withdraw")
            print("3 : Deposit")
            print("4 : Transfer")
            print("5 : Quit")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    customer.TransactionHistory()
                case 2 :
                    customer.withdraw()
                case 3: 
                    customer.deposit()
                case 4:
                    customer.transfer()
                case 5:
                    print("Thank you for Visiting. Have a Good Day!! :)") 
                    exit(0)
                case default: 
                    print("Invalid Choice!!")

if __name__ == "__main__":
    main()


