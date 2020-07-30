str=(input("enter a string:"))
str=str.lower()
if str==str[::-1]:
   print(str,"is palindrome")
else:
   print(str,"is not a palindrome")
