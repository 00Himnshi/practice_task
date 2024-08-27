import pickle
import os


#--------------------------------------------------

#program for creating the file
def createfile():
     cust_list=[]
     ans='y'
     while ans=='y':
          phone_no=int(input("Enter your phone no: "))
          name=input("Enter your name: ")
          age=input('Enter your age: ')
          email=input("Enter your Email-ID: ")
          nationality=input("Enter your nationality: ")
          rent=room()
          foodbill=cuisine()
          gamingbill=games()
          bill=billing_details(rent,foodbill,gamingbill)
          print("thank you ! your total bill is:",bill)
          cust_list.append([name,phone_no,age,email,nationality,{"rent":rent,"foodbill":foodbill,"gamingbill":gamingbill,"total bill":bill }])
          ans=input('Continue? y/n: ')
     f=open('customer.dat','wb')
     for rec in cust_list:
          pickle.dump(rec,f)
#--------------------------------------------------

#program for cuisine
def cuisine():
     print("WE HAVE THE FOLLOWING CUISINES: ")
     print("1. Vegetarian Combo >>>> 300 Rs.")
     print("2. Non-Vegetarian Combo >>>>> 500 Rs.")
     print("3. Vegetarian & Non-Vegetarian Combo >>>> 750 Rs.")
     print("4. If no food is to be chosen")
     dish = int(input("Enter Your Cusine : "))
     foodbill=0
     if dish==4:
          foodbill=0
     elif dish == 1:
          qty=int(input("Enter Quantity : "))
          foodbill=300*qty
     elif dish==2:
          qty=int(input("Enter Quantity : "))
          foodbill=500*qty
     elif dish==3:
          qty=int(input("Enter Quantity : "))
          foodbill=750*qty
     else:
         print("wrong option chosen")   
     print("Your Total food Bill Amount Is : Rs. ",foodbill)
     a=foodbill
     return a

#-----------------------------------------------
    
#program for games
def games():
    print(""" WE HAVE THE FOLLOWING GAMING OPTIONS :
                  1. Table Tennis -----> 150 Rs./HR
                  2. Bowling -----> 100 Rs./HR 
                  3. Snooker -----> 250 Rs./HR
                  4. VR World Gaming -----> 400 Rs./HR 
                  5. Video Games -----> 300 Rs./HR 
                  6. Swimming Pool Games -----> 350 Rs./HR
                  7. If you want to choose no game""")
    game=int(input("Enter what game you want to play : "))
    gamefare=0
    if game==1:
         hour=int(input("Enter No of hours you want to play : "))
         gamefare=150*hour
    elif game==2:
         hour=int(input("Enter No of hours you want to play : "))
         gamefare=100*hour
    elif game==3:
         hour=int(input("Enter No of hours you want to play : "))
         gamefare=250*hour
    elif game==4:
         hour=int(input("Enter No of hours you want to play : "))
         gamefare=400*hour
    elif game==5:
         hour=int(input("Enter No of hours you want to play : "))
         gamefare=300*hour
    elif game==6:
         hour=int(input("Enter No of hours you want to play : "))
         gamefare=350*hour
    elif game==7:
        gamefare=0
    else:
        print("Invalid option chosen: ")
    print("Your Total Gaming Bill Is : Rs. ",gamefare)
    g=gamefare
    return g



#-------------------------------------------------------

#program for booking of room
def room():
    print("WE HAVE THE FOLLOWING ROOMS FOR YOU: ")
    print('''
                A ultra royal  >> 10,000 /day
	B royal >> 5000 / day
	C elite >> 3500 / day
	D budget >> 2500 / day
	''')
    roomchoice=input("Enter your room preference: ")
    days=int(input("Enter how many days u want to stay: "))
    roomfare=0
    #for fare calculation
    if roomchoice.upper() == 'A':
        roomfare= 10000*days
    elif roomchoice.upper() == 'B':
        roomfare= 5000*days
    elif roomchoice.upper()== 'C':
        roomfare=3500*days
    elif roomchoice.upper()== 'D':
        roomfare=2500*days
    else:
        print("Oh! you have chosen wrong choice: ")
    print("Thank you, your room has been booked for: ",days,'days')
    print("Your total roomrent is: ",roomfare)
    r=roomfare
    return r
    

#---------------------------------------------

#program for calculating total bill
def billing_details(room_rent, food, gaming):
    total=room_rent+food+gaming
    return total



#------------------------------------------------

#program for appending records
def append_rec():
     phone_no=int(input("Enter your phone no: "))
     name=input("Enter your  name: ")
     age=input('Enter your age: ')
     email=input("Enter your Email-ID: ")
     nationality=input("Enter your nationality: ")
     rent=room()
     foodbill=cuisine()
     gamingbill=games()
     bill=billing_details(rent,foodbill,gamingbill)
     print("thank you ! your total bill is:",bill)
     ls=[name,phone_no,age,email,nationality,{"rent":rent,"foodbill":foodbill,"gamingbill":gamingbill,"total bill":bill }]
     f=open('customer.dat','ab')
     pickle.dump(ls,f)


#----------------------------------------------------------------


#program for deleating record
def delete_rec():
     dumlst=[]
     tempfile=open("dumyfile.dat","wb")
     f=open("customer.dat","rb")
     while True:
         try:
             lst=pickle.load(f)
             dumlst.append(lst)
         except EOFError:
             break
     l=len(dumlst)
     while True:
          phone=int(input('Enter phone no. of the customer whose details are to be deleted: '))
          for j in range(l):
               if dumlst[j][1]==phone:
                    cus=dumlst.pop(j)
                    print('Deleted the details of the customer: ',cus)
                    break
          else:
               print("Invalid phone no")
          choose=input('Do you want to delete more? (Y/N): ')
          if choose.upper()=='N':
               break
     if choose.upper()=='N':
          for rec in dumlst:
               pickle.dump(rec,tempfile)
          tempfile.close()
          f.close()
          os.remove("customer.dat")
          os.rename("dumyfile.dat","customer.dat")


#--------------------------------------------------------------

#program for updating record     
def updatefile():
     reclist=[]
     fo=0
     tempfile=open("dumfile.dat","wb")
     f=open('customer.dat','rb')   
     while True :
         try:
             file=pickle.load(f)
             reclist.append(file)
         except EOFError :
             break
     l="Y"
     while l.upper() == "Y" :
          s=int(input("Enter the phone number to search previously existing record: "))
          for rec in reclist:
              fo=0
              if s == rec[1] :
                  fo=1
                  print("Original details of the customer are-",rec)
                  print("1. name")
                  print('2. phone number')
                  print("3. age")
                  print("4. email ID")
                  print("5. nationality")
                  print('''6.Booking preferences
                                        A room preferences
                                        B gaming
                                        C cuisine
                                             ''')
                  ch=int(input("Enter which detail to update: "))
                  if ch==1:
                      na=input("Enter new name: ")
                      rec[0]=na
                  elif ch==2:
                      n=int(input("Enter new phone number: "))
                      rec[1]=n
                  elif ch==3:
                      a=int(input('Enter new age: '))
                      rec[2]=a
                  elif ch==4:
                      em=input("Enter new email: ")
                      rec[3]=em
                  elif ch==5:
                      n=input("Enter new nationality: ")
                      rec[4]=n
                  elif ch==6:
                       p=input("choose Out of A,B and C ")
                       if p.upper()== 'A':
                            roomrent=room()
                            for key in rec[5]:
                                 if key =='rent':
                                      rec[5][key]=roomrent
                       elif p.upper()== 'B':
                            gamingbill=games()
                            for key in rec[5]:
                                 if key == 'gamingbill':
                                      rec[5][key]=gamingbill
                       elif p.upper()== 'C':
                            foodbill=cuisine()
                            for key in rec[5]:
                                 if key =='foodbill':
                                      rec[5][key]=foodbill
                       else:
                             print("invalid choice")
                       for key in rec[5]:
                            if key == 'rent':
                                 roomrent=rec[5][key]
                            elif key == 'gamingbill':
                                 gamingbill=rec[5][key]
                            elif key == 'foodbill':
                                 foodbill=rec[5][key]
                       for key in rec[5]:
                             if key == 'total bill':
                                  rec[5][key]=billing_details(roomrent,foodbill,gamingbill)
                  else:
                      print("Invalid choice")
                      fo=2
                      break
                  break
              else:
                   continue
          if fo == 1:
               print('Modified data is: ',rec)
          elif fo==0:
               print("wrong phone number entered")
          l=input("Do you want to continue? (Y/N): ")      
          if l.upper() == 'N':
              for rec in reclist:
                  pickle.dump(rec,tempfile)
              tempfile.close()
              f.close()
              os.remove("customer.dat")
              os.rename("dumfile.dat","customer.dat")
#-------------------------------------------------------------------

#program for searching record
def search_rec():
     reclist=[]
     file=[]
     f=open('customer.dat','rb')
     s=int(input("Enter the phone number to search: "))
     while True:
         try:
             file=pickle.load(f)
             reclist.append(file)
         except  EOFError:
             break
     for rec in reclist:
         if s == rec[1] :
             print("Details of the customer are: ",rec)

#--------------------------------------------------------------------
#program for displaying all records
def displayfile():
     ls=[]
     lst=[]
     f=open("customer.dat","rb")
     while True:
         try:
             lst=pickle.load(f)
             ls.append(lst)
         except EOFError:
             break
     print("NAME       PHONE_NO       AGE       EMAIL                        NATIONALITY         {BOOKING DETAILS}  ")
     if len(ls)==0:
          print("the file contains no records")
     else:
          for i in range(len(ls)):
               for j in range(0,6):
                    print(ls[i][j],end='        ')
               print()
#---------------------------------------------------------------------
#Menu 
ch='Y'
while ch.lower()=="y":
     print("   ")
     print('''                                           WELCOME TO H&S HOTEL
A >>>>>
     Enter customer details.
     Book for a room
     Book for Cuisine
     Book for Gaming
     Generate total bill
B >>>>>
     Search customer record
C >>>>>
     Delete customer record
D >>>>>
     Update customer record
E >>>>>
     Display all records
F >>>>>
     append record
G >>>>>
     Return to Main Menu ''')
     n= input("Which option do you want? ")
     if n.upper() =='A':
          createfile()
     elif n.upper() =='B':
          search_rec()
     elif n.upper() =='C':
          delete_rec()
     elif n.upper() =='D':
          updatefile()
     elif n.upper() =='E':
          displayfile()
     elif n.upper()=='F':
          append_rec()
     elif n.upper() =='G':
          continue
     else:
         print("Option number is invalid")
         ch=input("do you want to continue (y/n)")     

