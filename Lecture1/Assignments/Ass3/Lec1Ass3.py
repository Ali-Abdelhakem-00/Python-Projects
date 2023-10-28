def ISHFTC(num, shift, Noofdigits):  
    return ((num << shift) % (1 << Noofdigits)) | (num >> (Noofdigits - shift))


num = int(input("Enter a number: "))
shift = int(input("Enter the number of positions to rotate: "))
Noofdigits = int(input("Enter the No of Digits: "))
result = ISHFTC(num, shift, Noofdigits)
print("The result of the rotation is:", result)
