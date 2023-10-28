while 1:
  number = input ("Please Enter Your Number")
  if(number .isnumeric()):
      if(len(number) == 11):
          print("Phone Number Accepted")
      else:
          print("Phone Number Incomplete")
  else:
      print("Phone Number Must Contain Only Numbers")