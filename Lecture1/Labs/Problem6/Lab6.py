name = input("Please Enter Customer Name: ")
amount = int (input ("Please Enter shopping amount: "))
per = int (input("Please Enter Discount Percentage: "))

result = amount- (amount*(per/100) )
print("\nDear",name,"\n\n\nThank you for shopping in IMT shopping Center." )
print("Total amount of your items is ",amount ,"L.E.")
print("You got ",per,"% , the value after \ndiscount is ", result,"L.E. ,Thank You")