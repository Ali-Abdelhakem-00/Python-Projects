EmpolyeeList={}

def AddEmpolyee():
   global Idcounter 

   name =input("Enter Empolyee Name: ")
   age = input("Enter Empolyee Age: ")
   job = input("Enter Empolyee Job: ")   
   Idcounter = input("Enter Empolyee ID: ")   
   EmpolyeeDic = {'Name': name,'Age': age ,'Job':job, 'ID':Idcounter} 
   print("Empolyee Added")
   EmpolyeeList[Idcounter]=EmpolyeeDic
 

def PrintEmpolyee():
   Idprint = input("Enter Emolyee ID: ")
   if Idprint in EmpolyeeList :
     print (EmpolyeeList[Idprint])
   else:
     print("ID Not Found")

def DeleteEmpolyee():
   Idprint = input("Enter Emolyee ID: ")
   if Idprint in EmpolyeeList :
     del(EmpolyeeList[Idprint])
     print("Empolyee Deleted")
   else:
     print("ID Not Found")

choise = 10

while choise != "4":
    print("**************************************")
    print("To Add New Empolyee Press 1")
    print("To Print Empolyee Data Press 2")
    print("To Delete Empolyee Press 3")
    print("To Exit Press 4")
    print("**************************************")
    choise = input("Please Enter Your Choise: ")

    if(choise == "1"):
        AddEmpolyee()
    elif(choise == "2"):
        PrintEmpolyee() 
    elif(choise == "3"):
       DeleteEmpolyee() 
    elif(choise == "4"):
        print("Thnaks")  
    else:    
        print("enter a valid Number") 