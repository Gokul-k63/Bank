#from admin import data as l
import json
import sys

with open ("accounts.json","r") as f:
         data=json.load(f)


def enter():
    global id,use,i
    a=0
    # while a<3:
    for i in range(3):
        id=(input("Enter your id or account number : "))
        if id.isnumeric():
            id=int(id)
            break
        elif id=="exit":
            exit()
        elif id.isnumeric()==False:
            raise InvalidInputError("enter correct id number..")
        else:
            print("\nEnter vaild input ")
            
    
    use=False
    for i in data:
        if id==i["Account_no"] or id==i["Coustemer_id"]:
            use=True
            break
def home():
    global choice
   
    print("""
            1.Balance check.
            2.Witdrawal.
            3.Deposite.
            4.Pin set / change
            5.Transfer money
            6.Logout
            """)
    print ("-------------------------------------------------------")
    choice=input("Enter a choice..")
    if choice=="exit":
        choice=choice
    elif choice.isdigit():
        choice=int(choice)
    else:
       raise InvalidInputError("enter the number ")

def change():
    global set_pin,cnfrm_pin
    if i["Atm_pin"]=="":
        max_time=0
        while max_time<2:
            set_pin=input("enter a 4 digit pin :")
            cnfrm_pin=input("re-enter a  4 digit pin :")
            if (set_pin and  cnfrm_pin).isdigit() :
                if len(set_pin and cnfrm_pin)==4:
                    if set_pin==cnfrm_pin:
                        i["Atm_pin"]=set_pin
                        print("pin set sucess")
                        break
                    else :
                        print("pin miss match check it")
                        max_time+=1
                else :
                    print ("pin is too length.enter only 4 digit only..!")
            else:
                print ("enter values only..!")
    else:
        pin=input("enter a old  pin")    
        if pin==i["Atm_pin"] and pin.isdigit():
            new_pin=input("enter a new pin ")
            check_pin=input("re-enter a new pin :")
            if len(new_pin and check_pin)==4 :
                if(new_pin and check_pin).isdigit():
                    if new_pin!=pin and new_pin==check_pin:
                        i["Atm_pin"]=new_pin 
                        print("Pin Number is Updated")
                    else:
                        print("pin number mismatch")
                else:
                    print ("enter values only..!")
            else :
                print ("pin is too length.enter only 4 digit only..!")
                
        else :
            print("in-valid pin")

    with open("accounts.json", "w") as f:
        json.dump(data, f, indent=4)
def sum():
    add=(input("enter the amount to deposite"))
    if add%100!=0:
            raise ValueError("Enter the 100 multiple's amount ")
    if add.isalnum()==False:
            raise InvalidInputError("Enter the amount properly ")
    add=int(add)
    i["Balance"]=i["Balance"] + add
    print(f"""Your amount added sucess...!
        your current balance is{i["Balance"] }
        """)
    with open("accounts.json", "w") as f:
        json.dump(data, f, indent=4)

def take():
    
    # try:
    amount=int(input("enter the amount to withdraw : "))
    if amount%100!=0:
            raise ValueError("Enter the 100 multiple's amount ")
    if amount.isalnum()==False:
            raise InvalidInputError("Enter the amount properly ")
    # except ValueError as v:
    #     print(v)

    if i["Balance"] <amount:
        print("your balance is low")            
    else:
        i["Balance"] -=amount
        print("withdrawl sucess")
        print(f"your remaining balance {i["Balance"] }")

    with open("accounts.json", "w") as f:
        json.dump(data, f, indent=4)


def tranf():
    coustmer=False
    a_tranf=int(input("enter their  account no or id : "))
    
    for c in data:
        if a_tranf==c["Account_no"] or a_tranf==c["Coustemer_id"]:
            coustmer=True
            break
    if coustmer:

        if i["Balance"]<=0 :
            print("you can't transfer amount..!")
            print("your balance is 0..!")
            return
        elif c==i:
            print("you cant transfer to your account ")
            return
        
        amnt=int(input(f"enter a amount to transfer to mr/mrs. {c["Name"]} 's account : "))
        if i["Balance"]>=amnt:
            c["Balance"]+=amnt
            i["Balance"]-=amnt
            print("transfer sucess")
            print(f"your remaining balance {i["Balance"]}\n")
        else:
            print("in-sufficent balance")
    else :
        print("no user found")

    with open("accounts.json", "w") as f:
        json.dump(data, f, indent=4)


def cnt():
    conti=input("do you want to continue ").lower()

    if conti=="yes":
         return True
    else :
        return False

def act():
 d=0
 ct=True
 while d<3 and ct:
    enter() # check account is have or not
    if i["Atm_pin"]=="":
        print(f"welcome mr/mrs.{i['Name']} ")
        print("you are new coustemer so set a pin to continue transcation")
        change()
    if use:
            cd=True
            while cd:
                chance=True
                t=0
                print(f"welcome mr/mrs.{i['Name']} ")
                home() #option kekum [ choice ]
                if choice==1: # balance check
                    while t<3 and chance:
                        pin_check=(input("enter a pin"))
                        if pin_check==i["Atm_pin"]:
                            print(f"Your available balance :{i["Balance"]}\n")
                            chance=False
                        else:
                            print("invalid pin.try again\n")
                            t+=1
                    print()
                    # sys.exit()
                  
                elif choice==2: # withdrawl
                    while t<3 and chance:
                        pin_check=(input("enter a pin"))
                        if pin_check==i["Atm_pin"]:
                           take()
                           chance=False
                        else:
                           print("invalid pin.try again\n")
                           t+=1
                    # sys.exit()
                                        
                elif choice==3: #deposite
                    while t<3 and chance:
                        pin_check=(input("enter a pin"))
                        if pin_check==i["Atm_pin"]:
                            sum()
                            chance=False
                        else:
                            print("invalid pin.try again\n")
                            t+=1
                    # sys.exit()
                        
                elif choice==4:# pin set/change
                    while t<3 and chance:
                        pin_check=(input("enter a pin"))
                        if pin_check==i["Atm_pin"]:
                            change()
                            chance=False
                        else:
                            print("invalid pin.try again\n")
                            t+=1
                    # sys.exit()
                     
                elif choice==5: #trasfer money
                    while t<3 and chance:
                        pin_check=(input("enter a pin"))
                        if pin_check==i["Atm_pin"]:
                            tranf()
                            chance=False
                        else:
                            print("invalid pin.try again\n")
                            t+=1
                    # sys.exit()
                     
                elif choice==6  or choice=="exit": 
                    print("thank you ..!\n")
                    cd=False
                    ct=False
                    break
                    
                else:
                   try: 
                    raise InvalidInputError("enter the number 1 to 6 ")    
                   except InvalidInputError as a:
                       print( "Error :",a) 
    else:
        print("no user found ..!")
        d+=1
           
class InvalidInputError(Exception):
    pass
            
if __name__ == "__main__":  
   q=0
   while q<3:
    try:
            act()
            break
    except KeyboardInterrupt:
            print("\n\nkey bord intupted\n")
    except ValueError as v:
            print(v)
    except InvalidInputError as ii:
            print("Error : ",ii)
    q+=1