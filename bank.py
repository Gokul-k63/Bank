from user import act 
from admin import a_check
try:
    c=True
    while c:
        print("""
                1.admin
                2.user
                3.exit
                """)
        a=input("enter the value:")
        a=int(a)
        if a==1  :
            a_check()
        elif a==2:
            act()
        elif a==3:
            print("Thank you...!")
            c=False
        else :
            print("enter a valid input")
except Exception as err:
    print(err)