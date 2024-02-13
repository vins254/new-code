#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence.
#eg " Hello World " => returns 2

sentence = str(input("Enter a sentence:"))
string = sentence.lower()
print(string)
count = 0
vowels = "aeiou"
for i in string:
    if i in vowels:
        count+=1
print("Number of vowels: ", count)

    