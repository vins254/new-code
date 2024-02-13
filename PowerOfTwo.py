#Question 3: Power of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.
#Examples: 
#8=> returns true
#6=> returns false


num = int(input("Enter number:"))
i = 0
result = 0

while result < num:
    result = 1<<i
    if result == num:
        print(result, "True")
        break
    i+=1
else:
        print("False")
        