#Check whether a number is positive
num=int(input("enter a number:"))
if num>0:
    print(f"{num} is a positive number")


#Check whether a given string is empty
s=input("enter a string:")
if s=="":
    print(f'The string is empty',{s})

#Check whether a number is positive, negative, or zero using only if statements
num=int(input())
if num>0:
    print(f'{num} is a positive number')
if num<0:
    print(f'{num} is a negative number')
if num==0:
    print(f'{num} is zero')

#Check whether a number is a multiple of both 3 and 5
n=int(input("enter a number:"))
if n%3==0 and n%5==0:
    print(f'{n} is a multiple of 3 and 5')

#check whether a number is a perfect square
n=int(input("enter a number:"))
if (n**0.5)**2:
    print(f'{n} is a perfect square')

#Check whether a number is a divisible by both 2 and 3
n=int(input("enter a number:"))
if n%2==0 and n%3==0:
    print(f'{n} is divisible by both 2 and 3')

#perfect cube
num=int(input("enter a number:"))
if (num**(1/3))**3==num:
    print(f'{num} is a perfect cube')

#multiple of 4
n=int(input("enter a number:"))
if n%4==0:
    print(f'{n} is a multiple of 4')