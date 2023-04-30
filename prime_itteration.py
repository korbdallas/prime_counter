#This is a simple program too allow user to select which prime itteration they wish to see.

#!/usr/bin/env python
from sys import exit


num=3 # number being tested
current_itteration=1 # prime number iteration counter
wanted_itteration=int(input("Enter the prime itteration you wish to see: "))

if (wanted_itteration <= 0):
  exit("Itteration must be larger than 0")  
   
else:
    while(current_itteration < wanted_itteration): 

         # method for making sure we only test odd numbers for prime
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
                 #print(num, "is a prime number")
                 current_itteration += :1
                 num=num+1

          
print (num-1, "Is the", wanted_itteration,"prime itteration")
