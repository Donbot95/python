#Take two lists and write a program that returns a 
#list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.
#Extras:
#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

randomList = []
listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [1, 2, 3, 4, 5, 6, 7]
listThree = []
x = 0
randomTwo = []
randomMatch = []

for num in listOne:
    if num in listTwo:
        listThree.append(num)

print(listThree)

#generate list with random numbers

randomTwo = random.sample(range(10, 30), 5)
randomList = random.sample(range(10, 30), 5)

for num in randomTwo:
    if num in randomList:
        randomMatch.append(num)
    
print(randomMatch)