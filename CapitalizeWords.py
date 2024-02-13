#Question 4: Capitalize Words
#Write a program that accepts a string as input, capitalizes the first letter of each word in the 
#string, and then returns the result string.
#Examples: 
#"hi"=> returns "Hi"
#"i love programming"=> returns "I Love Programming"



import string
input_string = str(input("Enter a string:"))
print(string.capwords(input_string))

