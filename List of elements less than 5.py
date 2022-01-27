#Take a file and write a program that prints out all the elements of the list that are less than 5.
#Instead of printing the elements one by one,
#make a new list that has all the elements less than 5 from this list in it and print out this new list.


numbers = [1, 2, 3, 4, 5, 7, 26, 30]
newList = []
x = 0
y = 0

for num in numbers:
    if num < 5:
        newList.append(x + num)

print(newList)


#Write this in one line of Python.
#Not sure what this means?

#Ask the user for a number and return a list 
#that contains only elements from the original list a that are smaller than that number given by the user.

newListTwo = []
inputNumber = input("Enter a number: ")

for num in numbers:
    if int(inputNumber) > num:
        newListTwo.append(y + num)

print(newListTwo)







