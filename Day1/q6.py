#6) Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)

num=int(input("Enter the number:"))
#print("factorial of", num ,"is ",fact(num))
print ( f"factorial of is:{fact(num)}")
