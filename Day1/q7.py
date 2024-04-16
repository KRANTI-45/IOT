#7) Using for loop, write and run a Python program to find factorial from 0 to 10.
#num=[0,1,2,3,4,5,6,7,8,9,10]
num=(input("Enter the num:"))

for value  in num:
    fact=value*(value-1)
print(fact)
    