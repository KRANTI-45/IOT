#7) Using for loop, write and run a Python program to find factorial from 0 to 10.
#num=[0,1,2,3,4,5,6,7,8,9,10]
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)

for i in range (1,11):
   fact(i)
   print ( f"factorial of {i} is:{fact(i)}")

