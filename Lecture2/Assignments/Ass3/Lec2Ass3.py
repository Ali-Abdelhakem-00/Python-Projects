
Hight = int(input("Enter height of the diamond (Recommended an odd Number): "))

if(Hight//2 == 0):
 Hight = int(Hight /2)
else:
    Hight = Hight -int(Hight/2)

for i in range (1 , (Hight+1) ):
     print (" "*(Hight-i), "*" * (i*2-1) )
     
for i in range (1 , (Hight+1) ):
     print (" "*(i),"*" * ( (Hight*2-1)-(i*2) ) ) 




