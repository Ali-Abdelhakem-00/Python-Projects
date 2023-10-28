MaxNumber = 0
MinNumber = 1000000
avr = 0
sum =0

for i in range(0,10):
    Number = int(input('Enter Number: ')) 
    if(Number > MaxNumber):
      MaxNumber = Number
    if(Number < MinNumber):
       MinNumber = Number
    sum = sum + Number
avr = sum/10
print("Maximum Value : ", int(MaxNumber))
print("Minimum Value : " ,int(MinNumber))
print("Average of the data = " ,float(avr) )



