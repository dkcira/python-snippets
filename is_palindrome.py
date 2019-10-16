# check if a given string is a palindrome by comparing to the reverse

original_string = "abcba"

if original_string == original_string[::-1]:
     print(original_string + " is a palindrome")
else:
     print(original_string + " is NOT a palindrome")

