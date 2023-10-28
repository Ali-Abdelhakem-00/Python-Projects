namelist = ["ahmed" , "ali" ,"amr" ]
passlist = ["1394" , "6078" ,"9345"]
nameindex = 0
counter = 0
while 1:
 name  = input ("Please Enter Your Name: ")
 name = name.lower()
 if(name in namelist):
   nameindex = namelist.index(name)
   counter = 0
   while counter<3:
    password = input ("Please Enter Your Password: ")
    if( password== passlist[nameindex] ):
     print("welcome back,",end = '')
     print(name)
     break
    else:
     print("Incorrect Password")	 
     counter += 1 
   if(counter<3):
    print("thanks")
   else:
    print ("no more trials") 
 else:
  print("Incorrect Username") 