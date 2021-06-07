class Atm:
    def __init__(self,card_number,pin):
        self.card_number = card_number
        self.pin = pin

    def checkBalance(self):
        print("Your balance is 50000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    CardNumber = input("insert your card number:- ")
    pinNumber  = input("enter your pin number:- ")

    new_user =  Atm(CardNumber ,pinNumber)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.checkBalance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()
