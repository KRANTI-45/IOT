# 5)The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
# ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

m=float(input("Enter the mark of marathi:"))
h=float(input("Enter the mark of hindi:"))
e=float(input("Enter the mark of english:"))
avg=((m+e+h)/3)
print(avg)
if  avg>=90  :
    print("Grade A")
elif avg>=80 :
    print("Grade B")
elif avg>=70:
    print("Grade C")
elif avg>=60 :
    print("Grade D")
else:
    print(" Grade F")    

 