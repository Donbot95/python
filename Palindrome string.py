#Ask the user for a string and print out whether this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)

originalString = input("Enter a string of letters: ")

separator = "" 

reversedString = separator.join(list(reversed(originalString)))



if reversedString == originalString:
    print("String is a palindrome")
elif reversedString != originalString:
    print("String is not a palindrome")

