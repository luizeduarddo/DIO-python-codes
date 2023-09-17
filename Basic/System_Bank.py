import os

menu = f'''
=======================
[1] Deposit
[2] Withdraw
[3] Statement
[4] Quit
=======================
'''

balance = 0
limit = 500
statement = ""
WITHDRAW_LIMIT = 3
withdraw_numbers = 0

while True:

    option = (input(f"\nChoose an option according to the index.{menu}"))
                    
    if option == "1":
        deposit_value = float(input("Enter the value of deposit: "))

        if deposit_value > 0:
            balance += deposit_value
            statement += f"Deposit: R$ {deposit_value:.2f}\n"
            os.system("cls")         

        else:
            os.system("cls")         
            print("Invalide value.")
    
    elif option == "2":
        withdraw_value = float(input("Enter the value of withdraw: "))
        
        if withdraw_value > balance:
            os.system("cls")         
            print("\nAmount greater than available balance")
            print("")

        elif withdraw_value > limit:
            os.system("cls")         
            print("\nVery high withdraw amount. Limit for each withdraw R$ 500.00.")

        elif withdraw_numbers >= WITHDRAW_LIMIT:
            os.system("cls")         
            print("\nNumber of withdraws exceeded.")

        else:
            balance -= withdraw_value
            statement += f"Withdraw: R$ {withdraw_value:.2f}\n"
            withdraw_numbers += 1
            os.system("cls")         
        

    elif option == "3":
        print(f"\nYOUR COMPLETE BANK STATEMENT: ")
        print("Didn't have any account movements." if not statement else statement)
        print(f"Balance: R$ {balance:.2f}\n")

    elif option == "4":
        print("Quit")
        os.system("cls")
        break

    else:
        print("Invalid Operation. Choose a valid option.")
