#Question 5: Reverse Integer
#Write a program that takes an integer as input and returns an integer with reversed digit 
#ordering.
#Examples:
#For input 500, the program should return 5.
#For input -56, the program should return -65.
#For input -90, the program should return -9.
#For input 91, the program should return 19.

num = int(input("Enter Number: "))
rev = 0
while num > 0:
    last_dig = num % 10
    rev = rev * 10 + last_dig
    num = num // 10
print("The reversed digit ordering is: ", rev)
    
    