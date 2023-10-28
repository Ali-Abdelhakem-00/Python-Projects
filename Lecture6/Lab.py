file1 = open("E:\\ITI\\03-python\\List\\file.txt",'w+')
file1.write("void Init_PORTA_DIR (void)\n\n {")
DDRA = ''
i=0
while i <8:
  print("Please enter Bit",i," mode: ",end ='')
  bit = input()
  bit = bit.lower()
  if(bit == "input"):
   DDRA = '0'+ DDRA
  elif(bit == "output"):
   DDRA = '1'+ DDRA
  else:
   print("Please enter a valid mode")
   i-=1 
 
  i +=1   


DDRA = '0b'+DDRA
file1.write("DDRA = ")
file1.write(DDRA)
file1.write("\n\n")
file1.write("}")
