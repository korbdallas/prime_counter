#This is a simple program to print all prime number to the 1000'th itteration.

#!/usr/bin/env python

num=2 # number being tested
y=1 # prime number iteration counter
z=1000 # prime iteration we want

while (y < z): 

     if (num % 2) == 0:
        num=num+1
     else:
        for i in range(2,int(num/2)+1):
             # If num is divisible by any number between
             # 2 and n / 2, it is not prime
             if (num % i) == 0:
                 num=num+1
                 break 
            
        else: 
             print(num, "is a prime number")
             y=y+1
             num=num+1

          
else: print (num-1, "Is the 1000th prime itteration")
