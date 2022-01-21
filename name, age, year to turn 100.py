#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("What is your first name?")
age = input("What is your age in years?")
century = (100) - int(age)
year = (2022) + (century)

print("Your name is " + (name) + " ,your age is " + (age) + " and you will turn 100 years old in " + str(year))


#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message

extra1 = input("Enter a number from 1-10")
