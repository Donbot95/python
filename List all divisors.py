#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#(If you don’t know what a divisor is, 
#it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

usernum = input("Please enter a number: ")
x = range(1, int(usernum))
inputList = []
y = 0
divisor = []


for num in x:
    if num in x:
        inputList.append(y + num)
        
for num in inputList:
    if (int(usernum) %num) ==0:
        divisor.append(num)
    
print(divisor)