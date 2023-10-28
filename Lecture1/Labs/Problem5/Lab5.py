res = int(input("Please enter the timer resolution: "))

fre = int(input("Please enter the system frequency in MHz: "))

pre = int(input("Please enter the Prescaller value: "))

freq = (fre*1000000)/pre
reso = (freq/ 2**res)
value = str( (1/reso) *100010 )
print("The timer would overflow after ", value ,"milliseconds")