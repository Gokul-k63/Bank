import random
import sys
import json
import re

# bank admin page
with open ("accounts.json","r") as f:
        data=json.load(f)

def check():
    global choice
    print("""
    1. Admin
    2. User
    """)
    choice=input("enter your choice : ")
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Enter only number")


def save():
    while True:
        global coustemer_name,aadhar_no,mail_id,phone_no,pancard_no,age,coustemer_id,balance,pin

        while True:
            coustemer_name=input("Enter your name : ").capitalize()
            if  coustemer_name.isalpha():
                break
            else:
                print ("Invalid name. re-enter the name.!")

        coustemer_id=int(input("Enter your coustemer id : "))

        while True:
            age=int(input("Enter your age : "))
            if age>=18: 
                break
            else:
                print ("Invalid age. re-enter the age.!")
                
        while True:
            mail_id=input("Enter your mail id : ")
            pattern = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}"
            if re.fullmatch(pattern, mail_id):
               break
            else:
                print("Invalid email, re-enter the e-mail")
        while True:
            aadhar_no=(input("Enter your aadhar number : "))

            if len(aadhar_no)==12 and aadhar_no.isdigit():
                break
            else:
                print("invalid aadhar no,so re-enter the aadhar number ")
            
        while True:
            phone_no=(input("Enter your phone number : "))
            if len(phone_no)==10 and phone_no.isdigit() :
                break
            else:
                print(" invalid phone number,so re-enter the phone number")
        while True:
            pancard_no=input("Enter your pancard number : ")
            if len(pancard_no)==10 and pancard_no.isdigit():
                break
            else:
                print("invalid pancard-no.so re-enter the pan number")
        a=True
        while a: 
                print("1.current account,2.saving account,3.zero balance account")
                account_type=int(input("Enter your account type : "))
                if account_type in [1, 2, 3]:
                    if account_type==1:
                        account_type="current"
                        balance=int(input("Enter your initial amount  Minimum 1000: "))
                    elif account_type==2:
                        account_type="saving"
                        balance=int(input("Enter your initial amount Minimum 500: "))
                    elif account_type==3: 
                        account_type="zero balance"
                        balance=0
            
                if account_type=="current" and balance<1000:
                    print(f"your account type is {account_type},")
                    print(" but your initial amount is below 1000,so deposite full amount.")
                elif account_type=="saving" and balance<500:
                    print(f"your account type is {account_type},")
                    print(" but your initial amount is below 500,so deposite full amount.")
                else:
                    a=False
        address=input("Enter the current address : ")
        pin=""
        account_no=random.randint(10000000000,99999999999)

        print("-"*30,"check your info","-"*30)
        print("Name:",coustemer_name)
        print("Aadhar_no:",aadhar_no)       
        print("Mail_id:",mail_id)
        print("Phone_no:",phone_no)
        print("Pancard_no:",pancard_no)
        print("Age:",age)
        print("Address:",address)
        print("Account_type:",account_type)
        print("Balance:",balance)
        print("coustemer_id:",coustemer_id)
        print("-"*60,"\n")

        cnfrm=input("if your info is correct then enter 'yes' to create account or enter 'no' to cancel : ").lower()
        if cnfrm=="yes":
                
                coustemer_list=({"Name": coustemer_name,
                                "Aadhar_no": aadhar_no,
                                "Mail_id": mail_id,
                                "Phone_no": phone_no,
                                "Pancard_no": pancard_no,
                                "Age": age,
                                "Address":address,
                                "Balance": balance,
                                "Account_type": account_type,
                                "Account_no": account_no,
                                "Coustemer_id": coustemer_id,
                                "Atm_pin":pin
                                })
               

                data.append(coustemer_list)
                with open("accounts.json", "w") as f:
                    json.dump(data, f, indent=4)
                print("your account is created sucessfully")
                break
        elif cnfrm=="no":
                print(" please try after some time to create account")
        else:
                print("your input is invalid,so your account is not created")
        break

def total_balance():
    global total
    total=0
    for i in data:
        total+= i["Balance"]
    print(f"total bank balance is {total}")

def view():
    print("------------------all account details-------------------")
    print("total coustemer in bank is :",len(data),"\n")
    for i in data:
        for  key, values in i.items():
            print(f"{key}:{values}")
        print ("-"*60)
    print("----------------------- END ---------------------------------")    

def clear():
    global coustemer_clear
    print("-"*60)
    coustemer_clear=int(input("enter your account number or customer id to clear your account : "))
    check=False
    for i in data:
            if i["Account_no"]==(coustemer_clear) or i["Coustemer_id"]==(coustemer_clear):
                check=True
                break
           
    if check:
        data.remove(i)
        print("your account is closed sucessfully")
    else:
        print("your account number or customer id is invalid")
    
    with open("accounts.json", "w") as f:
        json.dump(data, f, indent=4)

def search():
    global coustemer_search
    print("-"*60)
    coustemer_search=int(input("enter your account number or customer id to search your account : "))
    check=False
    for i in data:
            if i["Account_no"]==(coustemer_search) or i["Coustemer_id"]==(coustemer_search):
                check=True
                break
           
    if check:
        for  key, values in i.items():
            print(f"{key}:{values}")
        print ("-"*60)
    else:
        print("Check your account number or customer id is invalid")

def deposite():
    global coustemer_deposite
    print("-"*60)
    coustemer_deposite=int(input("enter your account number or customer id to deposite amount : "))
    check=False
    for i in data:
            if i["Account_no"]==(coustemer_deposite) or i["Coustemer_id"]==(coustemer_deposite):
                check=True
                break
           
    if check:
        amount=int(input("enter the amount to deposite : "))
        i["Balance"]=i["Balance"]+amount
        print(f"your account balance is {i['balance']}")
    else:
        print("Check your account number or customer id is invalid")

    with open("accounts.json", "w") as f:
        json.dump(data, f, indent=4)

def withdraw():
    global coustemer_withdraw
    coustemer_withdraw=int(input("enter your account number or customer id to withdraw amount : "))
    check=False
    for i in data:
            if i["Account_no"]==(coustemer_withdraw) or i["Coustemer_id"]==(coustemer_withdraw):
                check=True
                break
           
    if check:
        amount=int(input("enter the amount to withdraw : "))
        
        if i["Balance"]>=amount:
            i["Balance"]=i["Balance"]-amount
            print(f"your account balance is {i['balance']}")
        else:
            print("your account balance is insufficient")
    else:
        print("Check your account number or customer id is invalid")

    with open("accounts.json", "w") as f:
        json.dump(data, f, indent=4)

def alter():
    print("-"*30,"update page","-"*30)
    change_id=int(input("Enter the coustermer id or account number to update : "))
    check=False
    for id in data:
        if id["Coustemer_id"]==change_id or id["Account_no"]==change_id:
            check=True
            break
    if check:
        print("Enter the updated value \n")
        print("-"*60)
        w=True
        while w:
            print("""
                    1.Name
                    2.Phone number
                    3.E-mail id
                    4.Address
                    5.Back
                    
                """)
            value=(input("enter the option to update :"))
            if value=="1":
                new_name=input("enter new name :").capitalize()
                id["Name"]=new_name
                print("name update sucessfull..!")
            elif value=="2":
                ch=True
                while ch:
                    new_num=(input("enter new phone number : ")).isdigit()
                    if len(new_num)==10:
                        id["Phone_no"]=new_num
                        print("phone number sucessful..!")
                        ch=False
                    else:
                        print("enter valid number")
            elif value=="3":
                id["Mail_id"]=input("enter new e-mail id : ")
            elif value=="4":
                id["Address"]=input("enter new address : ")
            elif value=="5":
                w=False
            else:
                print("enter valid option")
                
            with open("accounts.json", "w") as f:
                json.dump(data, f, indent=4)
        else :
            print("your coustemer id or account number is invalid")
        

        
def a_check():

    for i in range(3):
        name=input("\n\nenter your name : ")
        password=input("enter your password : ")
        if name==admin_name and password==admin_password:
            a=True
            while a: 
                print("-"*30,"welcome to admin page","-"*30)
                print("""
                                    1. Create account
                                    2. View all account
                                    3. Search account
                                    4. Close account
                                    5. Update account
                                    6. Deposite to coustemer account
                                    7. Withdraw to coustemer account
                                    8. Total bank balance
                                    9. Logout
                                """)
                select=int(input("enter your choice : "))
                        
                if select==1: # create account
                    save()
                elif select==2: # view all account
                    view()
                elif select==3: # search account
                    search()
                elif select==4: # close account
                    clear()
                elif select==5: # update account
                    alter()
                elif select==6: # deposite to coustemer account
                    deposite()
                elif select==7: # withdraw from coustemer account
                    withdraw()
                elif select==8: # total bank balance
                    total_balance()
                elif select==9 : # logout
                    print("logout sucess\n")
                    a=False
                    sys.exit()
                else:
                    print("enter the valid choice")
        else:
                print("\nyour name or password is incorrect")
        
        
    

        
# main program
admin_name="admin"
admin_password="admin123"
# file import pannum pothu inside wrk vara file la call agathu.
if __name__ == "__main__":
    try:
        a_check()
    except Exception as err:
        print(err)




