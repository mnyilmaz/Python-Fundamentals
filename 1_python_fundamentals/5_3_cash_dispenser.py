# BTK Academy
# Advanced Python Programming From Zero
# Lecture 5.3: Methods in Pyhton - Function Examples - Cash Dispenser
# python 5_3_cash_dispenser.py
blank = "----------------------"

# Cash Dispenser Application

harry_acnt = {
    "name" : "Harry Potter",
    "account_no" : 123456,
    "balance" : 8000,
    "additional_account" : 4000
}

hermione_acnt = {
    "name" : "Hermione Granger",
    "account_no" : 654321,
    "balance" : 5000,
    "additional_account" : 3000
}

ron_acnt = {
    "name" : "Ronald Weasley",
    "account_no" : 987654,
    "balance" : 2000,
    "additional_account" : 2000
}

def get_stone(acnt, cash):
    print(f"Welcome to the Gringotts {acnt['name']}")
    print(blank)

    if acnt['balance'] >= cash:
        acnt['balance'] -= cash 
        print(f"Here's your payment {acnt['name']}. Only {acnt['balance']} Galleons has left in your account.")
        print(blank)

    else:
        overall = acnt['balance'] + acnt['additional_account']

        if overall >= cash:
            additional = input("Do you want to use your additional account (Y/N)? :")
            
            if additional == "Y":
                left = (acnt['additional_account'] + acnt['balance']) - cash
                acnt['additional_account'] = left
                print(f"Here's your payment {acnt['name']}. Only {acnt['additional_account']} Galleons has left in your additional account.")
                print(blank)

            else: 
                print(f"You've {acnt['balance']} Galleons in account {acnt['account_no']}")
                print(blank)

        else:
            print(f"Unfortunately, your balance is insufficient.\nWe'll be so pleased to see you again {acnt['name']}")
            print(blank)

def check_balance(account):
    print(f"You have {account['balance']} in account {account['account_no']}.\nYou have {account['additional_account']} Galleons in your additional account.")


user = input("Who wants to get into the Gringotts?: ")
desire = int(input("How much Galleons do you desire?:"))
print(blank)
get_stone(hermione_acnt,desire)
print(blank)
check_balance(hermione_acnt)
print(blank)
get_stone(hermione_acnt,desire)
