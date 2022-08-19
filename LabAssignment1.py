# Input taken from user 
userinput= input("\nEnter your string --> ")

# Revers the string 
# Like --> abcde = edcba 
revstr = (userinput[::-1])

# Checking the strings are same or not
# By using if-else statements
if revstr == userinput:
    print("This string is palindrome")
else:
    print("This string is not palindrome")
