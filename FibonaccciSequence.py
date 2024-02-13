#Question 2: Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100.

num = 12
first = 0
second = 1

if num <= 0:
    print("Enter Number Greater than zero!")
else:
    for i in range(num):
        print(first, end=" ")
        temp = first
        first = second
        second = temp + first 