# Anagram :

def anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)
word1 = input ("Enter First Word to Check Anagram Condition: ")
word2 = input ("Enter Second Word to Check Anagram Condition: ")

if anagram(word1, word2):
    print(f"{word1} and {word2} are Anagram")
    
else:
    print(f"{word1} and {word2} are not Anagram")
    
    
# Armstrong Number:

def armstrong(number):
    num_str = str(number)
    num_digit = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit)**num_digit
    return total == number

num = int(input("Enter Number to Check Armstrong Condition: "))

if armstrong(num):
    print(f"{num} is an Armstrong Number")
    
else:
    print(f"{num} is not Armstrong Number")
    