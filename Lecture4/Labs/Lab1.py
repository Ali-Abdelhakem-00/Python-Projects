Mylist = ["Watching TV", "Playing VG" , "Cooking"]
Donelist = []
def addItem():
 additem = input("Add Your Item: ")
 Mylist.append(additem) 
 print("Your Item Added successfully ")

def PrintItems():
 print(Mylist)
 
def DoneList():
  Doneitem = input("Which Item Did You Done?: ")
  if(Doneitem in Mylist ):
      Donelist.append(Doneitem)
      print("Your Item Added To Your Done-List")
      Mylist.remove(Doneitem)
  else:
      print("Enter a valid Item") 

def PrintDoneList():
 print(Donelist)

Number = 1
while Number != "5":
  print("**************************************")
  print ("To Add New Item Press 1")
  print ("To Print The To_Do List 2")
  print ("To Make an item as Done Press 3")
  print ("To Print The Done List Press 4")
  print ("To Exit Press 5")
  print("**************************************")
  Number = input("Please Enter Your Choise: ")

  if(Number == "1"):
        addItem()
  elif(Number == "2"):
        PrintItems() 
  elif(Number == "3"):
        DoneList()
  elif(Number == "4"):
        PrintDoneList()
  elif(Number == "5"):
        print("Thnaks")
  else:
        print("enter a valid Number")           