          #    Even or odd  #

#n=int(input("enter a number"))
#res=0
#while True:
 #   r=n%3
  #  n=n//10
   # res=res*10+r
    #print(res)
    #if n==0:
     #   break


         #  mailid or password  #

#imid="saihema141999@gmail.com"
#ipwd="23456"
#for i in range(5):
 #   mid=input("enter a mailid")
  #  pwd=input("enter password")
   # if imid==mid and ipwd==pwd:
    #    print("login succesfull")
     #   break
    #else:
     #   print("wrong mailid and password")
    

         #  Reverse of a number  #

#n=int(input("enter anumber"))
#res=0
#while True:
 #   rem=n%10
  #  n=n//10
   # res=res*10+rem
    #print(res)
    #if n==0:
     #   break


           #  prime number  #

#n=int(input("enter a number"))
#cnt=0
#for i in range(1,n+1):
 #   if n%i==0:
  #      cnt+=1
#if cnt==2:
 #   print("prime")
#else:
 #   print("not a prime")


        # OR #

#n=int(input("enter a number"))
#for i in range(2,n):
 #   if n%i==0:
  #      print("not a prime")
#else:
 #   print("prime")


        #  Prime number in a given range  #

#s=int(input("enter a number"))
#e=int(input("enter a number"))
#for j in range(s,e+1):
 #   cnt=0
  #  for i in range(1,j+1):
   #     if j%i==0:
    #        cnt+=1
    #if cnt==2:
     #       print(j,"prime")
            
        
    









#n=int(input("enter a number"))
#k=2*n-1
#for i in range(0,n):
 #   for j in range(0,k):
  #      print(end="")
   # k-=2
    #for j in range(0,i+1):
     #   print("*",end="")
    #print()


     # individual prime of a given number  #


#n=int(input("enter a number"))
#while n!=0:
 #   c=0
  #  rem=n%10
   # for i in range(1,rem+1):
    #    if rem%i==0:
     #       c+=1
    #if c==2:
     #   print("rem")
    #n=n//10
    


      # check wheather this is megaprime or not  #


#n=int(input("enter a number"))
#a=len(str(n))
#cnt=0
#x=0
#for i in range(1,n+1):
 #   if n%i==0:
 #       cnt+=1
#if n==2:
#    print(n,"prime")
 #   while n!=0:
  #      c=0
   #     rem=n%10
    #    for i in range(1,rem+1):
     #       if rem%i==0:
      #           c+=1
       #  if c==2:
        #    print(rem,"prime")
         #   x+=1
        #n=n//10
    #if x==a:
     #   print("mega prime as well")
    #else:
     #   print("not a mega prime")
#else:
   # print("not a prime")



#n=int(input("enter a number"))
#c=0
#while n:
 #   n-=1
  #  c+=1
   # print(''*n,'*'*c)




#n=int(input("enter a number"))           output:
#for i in range(1,n+1):                   enter a number3
 #   for j in range(1,i+1):      -->         *
  #      print("*",end="")                   * *
   # print()                                 * * *




      #  calender prgm  #
      

#import Calender
#yy=2020
#mm=5
#print(Calender.month(yy,mm))


              # OR #
              
#import calender
#yy=int(input("enter a year"))
#mm=int(input("enter a month"))
#print(calender.month(yy,mm))



       #  FUNCTIONS  #

#factorial of a number#

#def factorial(n):
#    fact=1
#   for i in range(1,n+1):
 #       fact=fact*i
  #  return(fact)
#n=int(input("enter a number"))
#print(factorial(n))


    #  recursive function #


#def function(n):
 #   if n==1:
  #      return 1
   # else:
    #    return (n*factorial(n-1))
#n=int(input("enter a number"))
#print(factorial(n))



      # MODULES #

#def add(x,y):
 #   return(x+y)
#def sub(x,y):
#    return(x-y)



#from math import sqrt,factorial
#print sqrt(16)
#print factorial(6)


#import onlinepython as op
#print(op.add(30,20))
#print(op.sub(30,20))
#print(op.div(30,20))
#print(op.mul(30,20))


#import random
#print dir(random)


# importing built-in module math 
#import math 
  
# using square root(sqrt) function contained  
# in math module 
#print math.sqrt(25)  
  
# using pi function contained in math module 
#print math.pi  
  
# 2 radians = 114.59 degreees 
#print math.degrees(2)

# 60 degrees = 1.04 radians 
#print math.radians(60)  
  
# Sine of 2 radians 
#print math.sin(2)  
  
# Cosine of 0.5 radians 
#print math.cos(0.5)  
  
# Tangent of 0.23 radians 
#print math.tan(0.23) 
  
# 1 * 2 * 3 * 4 = 24 
#print math.factorial(4)  
  
  
# importing built in module random 
#import random 
  
# printing random integer between 0 and 5 
#print random.randint(0, 5)  
  
# print random floating point number between 0 and 1 
#print random.random()


# random number between 0 and 100 
#print random.random() * 100 
  
#List = [1, 4, True, 800, "python", 27, "hello"] 
  
# using choice function in random module for choosing  
# a random element from a set such as a list 
#print random.choice(List) 
  
  
# importing built in module datetime 
#import datetime 
#from datetime import date 
#import time 
  
# Returns the number of seconds since the 
# Unix Epoch, January 1st 1970 
#print time.time()  
  
# Converts a number of seconds to a date object 
#print date.fromtimestamp(454554)  


 #output:5.0
 
#3.14159265359
#114.591559026
#1.0471975512
#0.909297426826
#0.87758256189
#0.234143362351
#24
#3
#0.401533172951
#88.4917616788
#True
#1461425771.87
#1970-01-06


  
# 60 degrees = 1.04 radians 
#print math.radians(60)  
  
# Sine of 2 radians 
#print math.sin(2)  
  
# Cosine of 0.5 radians 
#print math.cos(0.5)  
  
# Tangent of 0.23 radians 
#print math.tan(0.23) 
  
# 1 * 2 * 3 * 4 = 24 
#print math.factorial(4)  
