namelist = ["ahmed" , "ali" ,"amr" ]
passlist = ["1394" , "6078" ,"9345"]
nameindex = 0


namelist = ["ahmed" , "ali" ,"amr" ]
passlist = ["1394" , "6078" ,"9345"]
nameindex = 0
name  = input ("Please Enter Your Name: ")
if(name in namelist):
  nameindex = namelist.index(name)
  password = input ("Please Enter Your Password: ")
  if( password== passlist[nameindex] ):
   print("welcome back,",end = '')
   print(name)
  else:
   print("Incorrect Password")	 
   
else:
  print("Incorrect Username") 