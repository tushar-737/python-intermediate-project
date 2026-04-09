balance=0
def bank_deposit():
    global balance
    deposit=float(input("Money to deposit: "))
    print(f'''{deposit} depostied in bank''')
    balance += deposit
def bank_withdraw():
    global balance
    withdraw=float(input("Money to withdraw: "))
    if(withdraw<=balance):
        balance-=withdraw
        print(f'''{withdraw} deposited in bank''')    
    else:
        print("Insufficient Balance")
def bank_check_balance():
    global balance
    amount=balance
    print(f'''Acount Balance: {amount}''')
def exit():
    print("Exitng")
while True:
    print("\n----- Bank Account -----")
    print("1 for depositing money")
    print("2 for withdrawing money")
    print("3 for checking balance")
    print("4 for exiting")
    choice=input("Enter your choice: ")
    if(choice=="1"):
        bank_deposit()
    elif(choice=="2"):
        bank_withdraw()
    elif(choice=="3"):
        bank_check_balance()
    elif(choice=="4"):
        exit()
        break
    else:
        print("Invalid choice")                

  