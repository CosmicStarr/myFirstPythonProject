from email.policy import default
from re import sub
from webbrowser import get
from xmlrpc.client import DateTime
from datetime import date
from datetime import datetime

from jinja2 import Undefined
from pyCosmicSite.mongo import server
import matplotlib.pyplot as info
import numpy as numInfo



# twinkleVerse = 'Twinkle, twinkle, little star, \n \t how i wonder what you are! Up above the world so high, \n \t \t Like a diamond in the sky. \n \t \t \t Twinkle, twinkle, little star, how i wonder what you are'
# today = date.today()
# rightNow = datetime.date.today()
# whatIsPI = input('What is PI : ')
# answerToPI = '3.14'

# createNubs = tuple(input("enter some numbers : "))
# list = ['blue','red','green']
# numList = [1,2,3,4,5]
# for a in list: print(a)  
# for x in numList: 
#     if x == 4 : print(numList.count(x))
# def commuteFunc(n):
#     return n+10+100 
# ans = commuteFunc(1)
# date1 = datetime.date.today()
# date2 = datetime.date(1985,7,26)
# print(date2 - date1)
# if whatIsPI != answerToPI : print(f"{whatIsPI} Thats not the answer i was looking for! Try again!") 
# elif whatIsPI == answerToPI : print(f"{whatIsPI} Wonderful! That is right answer. You did a great job!") 
# #This does not print
# if a == 'blue': print(f"YES! {a}") 
# print(f"{twinkleVerse},This is the current date; {today}, \n This is the current time; {rightNow}",firstName[::-1],lastName[::-1], f" \n These are the numbers you typed {createNubs},{ans}")
# file = open('ZoomBaby.txt','a+')
# This program adds two numbers
# lonelyTuple = ("Normand")
# nuTuple = lonelyTuple.__add__(" Jean")
# myDic = {
#     "1":"Normand",
#     "2":"Jean",
# }
# def addKeyValue(keys,value) :
#     for k in myDic:
#         print(k)
#     if k == keys : return print(f"this key :{k} already exist")
#     myDic[keys] = value

# addKeyValue("3","Hope this works")
# carOptions = int(input('select an option: '))
# while carOptions != 0:
#     nameofCar = input("Mr Normand. Add Car Name: ")
#     Price = input("Mr Normand. Add Car Price: ")
#     server.createCars(nameofCar,Price)
#     carOptions = int(input('select an option: '))
# carOptions = int(input('select an option1: '))  

def Menu():
    print("[1] Home")
    print("[2] Profile")
    print("[0] Exit")
def subMenu():
    print("[1] Update Profile")
    print("[2] Delete Profile")
    print("[0] Exit Profile")
def StoreOptions():
    print("[1] Available Cars")
    print('[2] Satisfied Customers Chart')    
    print("[0] Exit")
def AvailableCars():
    dbCollection = server.db1["cosmic"] 
    cars = dbCollection.find({},{"Name": 1,"Price": 1,"_id": 0,})
    # listOfCars = list(cars)
    for car in cars:
        print(car)

def PaymentOption1():
    IdInfo = input('In order to proceed, enter your Id.\nIts in the informantion that was generated!: ')
    payInfo = int(input('Enter a nine digit account number: '))
    while payInfo != 9:
        if len(str(payInfo)) > 9: return print("Only 9 digits allowed")
        if len(str(payInfo)) < 9: return print(f'{payInfo} is not a vaild account number!')
        paymentObject = server.CardInfoName(IdInfo,payInfo)
        return paymentObject 

def PaymentOption2():
    IdInfo = input('In order to proceed, enter your Id.\nIts in the informantion that was generated!: ')
    payInfo = int(input('Enter your 16 digit MasterCard number: '))
    while payInfo != 16:
        if len(str(payInfo)) > 16: return print("Only 16 digits allowed")
        if len(str(payInfo)) < 16: return print(f'{payInfo} is not a vaild account number!')
        paymentObject = server.CardInfoName(IdInfo,payInfo)
        return paymentObject   

def updateProfile():
    userId = input("copy and paste your ID if you wish to change your info!\nits in the information that has been generated!: ")   
    nuUserName = input("create a new username : ")
    nuPass = input("create a new Password : ")
    nuUserInfo = server.UpdateUser(userId,nuUserName,nuPass)
    if nuUserInfo == None: print("Please insert a valid data")
    print(f'Your info is updated! {nuUserInfo}')
    return nuUserInfo
def deleteUser():
    print('If you delete your account, you will end the program!')
    userID = input("copy and paste your ID\nits in the information that has been generated!: ")
    deletedUser = server.deleteUser(userID)
    return deletedUser

print('Welcome to Cosmic Cars\n\tthe exprience of the century!')
yes = int(input('Are you a currently a User?\n#1 for Yes. Enter any other number to register!: '))
if yes != 1:
    while True:
        firstName = input("Enter your first name : ")
        lastName = input("Enter your last name : ")
        UserN = input("Enter your username : ") 
        Password = input("Enter a password : ") 
        City = input("Enter your city : ") 
        State = input("Enter your state : ") 
        nuUser = server.createUser(firstName,lastName,UserN,Password,0,City,State)
        if(nuUser) : print(f"{UserN} is created!")
        break

if yes == 1 or nuUser != None:
    print("Try to login!")
    while True:
        UserName = input("Enter your Username :  ")
        lastPassW = input("Enter your last Password :  ") 
        dbCollection = server.db["users"] 
        # x = dbCollection.find()
        oneUser = dbCollection.find_one({"UName":f"{UserName}","PassW":f"{lastPassW}"})
        # db.mycol.findOne({title: "MongoDB Overview"})
        # listOfx = list(x)
        # new_list = [el for el in listOfx if el["UName"] == f"{UserName}"]
        def checkUser(x):
            if x == None : print('Your information was bad!')
            else : print(f"Welcome! {UserName} \nThis is your information {x}")
            return x 
        x = checkUser(oneUser)
        break
    if x != None:
        print('Main Menu')
        Menu()
        options = int(input('select an option : '))
        while options != 0:
            if options == 1:
                print("This is your home")
                StoreOptions()
                options2 = int(input('select an option : '))
                while options2 != 0:
                    if options2 == 1:
                        AvailableCars()
                        print("Choose a car to buy: ")
                        options3 = int(input('#1 Lamborghini\n#2 Farrai \n#3 Konenigsegg\n =>'))
                        while options3 != 0:
                            if options3 == 1:
                                dbCollection = server.db1["cosmic"]
                                filteredCar = dbCollection.find_one({"Name":"Lamborghini Huracan"})
                                print(f"You selected the Lamborghini.\nThis is your vehicle information\n {filteredCar}")
                                payment = int(input('How are you going to pay? we only accept Check or MasterCard\n#1 Check \n#2 MasterCard\n=> '))
                                if payment == 1:
                                    paymentObject = PaymentOption1()
                                    if paymentObject == None: print('Information is invalid and it was not saved in our database')
                                    if paymentObject: print("Your account Info is saved in our database\nYou can expect a payment of $200,000 to be debited from your account!")
                                    options3 = 0
                                    options2 = 0                   
                                if payment == 2:
                                    paymentObject = PaymentOption2()
                                    if paymentObject == None: print('Information is invalid and it was not saved in our database')
                                    if paymentObject: print("Your account Info is saved in our database\nYou can expect a payment of $200,000 to be debited from your account!")
                                    options3 = 0
                                    options2 = 0                           
                            elif options3 == 2:        
                                dbCollection = server.db1["cosmic"]
                                filteredCar = dbCollection.find_one({"Name":"Farrai Pista"})
                                print(f"You selected the Lamborghini.\nThis is your vehicle information\n {filteredCar}")
                                payment = int(input('How are you going to pay? we only accept Check or MasterCard\n#1 Check \n#2 MasterCard\n=> '))
                                if payment == 1:
                                    paymentObject = PaymentOption1()
                                    if paymentObject: print("Your account Info is saved in our database\nYou can expect a payment of $400,000 to be debited from your account!")
                                    options3 = 0
                                    options2 = 0                         
                                if payment == 2:
                                    paymentObject = PaymentOption2()
                                    if paymentObject: print("Your account Info is saved in our database\nYou can expect a payment of $400,000 to be debited from your account!")
                                    options3 = 0
                                    options2 = 0                          
                            elif options3 == 3:
                                dbCollection = server.db1["cosmic"]
                                filteredCar = dbCollection.find_one({"Name":"Koenigsegg"})
                                print(f"You selected the Lamborghini.\nThis is your vehicle information\n {filteredCar}")
                                payment = int(input('How are you going to pay? we only accept Check or MasterCard\n#1 Check \n#2 MasterCard\n=> '))   
                                if payment == 1:
                                    paymentObject = PaymentOption1()
                                    if paymentObject: print("Your account Info is saved in our database\nYou can expect a payment of $1,000,000 to be debited from your account!")
                                    options3 = 0
                                    options2 = 0                      
                                if payment == 2:
                                    paymentObject = PaymentOption2()
                                    if paymentObject: print("Your account Info is saved in our database\nYou can expect a payment of $1,000,000 to be debited from your account!")
                                    options3 = 0
                                    options2 = 0
                            else:
                                print('Invalid option')
                                AvailableCars()
                                print("Choose a car to buy: ")
                                options3 = int(input('#1 Lamborghini\n#2 Farrai \n#3 Konenigsegg\n =>'))
                    elif options2 == 2 :
                        x = numInfo.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
                        y = numInfo.array([5, 7, 8, 10, 12, 15, 11, 13, 16,14,17,19])
                        info.title("Customer Data")
                        info.xlabel("Months / For the year 2021")
                        info.ylabel("Average Satisfied Customer")   
                        info.plot(x, y)
                        info.grid()
                        showInfo = info.show()
                        StoreOptions()
                        options2 = int(input('select an option : '))
                    else : 
                        print('Invalid option')  
                        StoreOptions()
                        options2 = int(input('select an option : '))
                Menu()
                options = int(input('select an option : '))                
            elif options == 2:
                print("This is your profile.\nYou can update your information or delete it!\npress zero to exit")
                subMenu()
                options1 = int(input('select an option : '))
                while options1 != 0:
                    if options1 == 1:
                        nuInfo = updateProfile()
                        subMenu()
                        options1 = int(input('select an option : '))
                    elif options1 == 2:
                        zeroUser = deleteUser()
                        options1 = 0
                        options = 0
                    else:
                        subMenu()
                        print('invalid option')
                        options1 = int(input('select an option : ')) 
                try:
                    if zeroUser:        
                        pass
                except Exception as Ex:
                        Menu()
                        options = int(input('select an option : '))                        
            else: 
                Menu()
                options = int(input('select an option : '))         
    else: print('No User Present! Good Bye!')
    print('This is the End! Good Bye!')
else: print('Registration was unsuccessful.') 
# if nuInfo:
#     print('Where do want to go from here?')
#     Menu()
#     options = int(input('select an option : '))
#     while options != 0:
#         if options == 1:
#             print("This is your home")
#             break
#         elif options == 2:
#             print("This is your profile.\nYou can update your information or delete it!\npress zero to exit")
#             subMenu()
#         options1 = int(input('select an option : '))
#         if options1 == 1:
#             nuInfo = updateProfile()
#             break
#         elif options1 == 2:
#             print('If you wish to delete your account')  
#             zeroUser = deleteUser()
#             break
#         elif options1 == 3:
#             print("press zero if you want to end the program") 
#             break
#         else:
#             Menu()
#             print('invalid option')
#             options1 = int(input('select an option : '))
# elif zeroUser != 0:  
#     print('do something')
# else: 
#     Menu()
#     print('invalid option')
#     options = int(input('select an option : '))


    

    
       

# Id = '6266004a24605ece68c49c63'
# nuUserN = 'Normandj85'
# UserId = server.UpdateUser(Id,nuUserN)




 



        

 
















# num1 = 1.5
# num2 = 6.3
# # Add two numbers
# sum = num1 + num2
# # Display the sum
# print(f'The sum of {0} and {1} is {2}'.format(num1, num2, sum),nuTuple,myDic)

# file = open("C:/Users/admin/OneDrive/Documents/ZoomLink.txt","a+")
# file.write('I can do this')
# print(file.read())
# file.close()
