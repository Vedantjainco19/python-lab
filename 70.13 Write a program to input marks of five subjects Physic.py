#Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. 
#Calculate percentage and grade according to following:
#Percentage >= 90% : Grade A
#Percentage >= 80% : Grade B
#Percentage >= 70% : Grade C
#Percentage >= 60% : Grade D
#Percentage >= 40% : Grade E
#Percentage < 40% : Grade F

ph=int(input("enter physics marks"))
c=int(input("enter chemistry marks"))
b=int(input("enter biology marks"))
m=int(input("enter maths marks"))
co=int(input("enter computer marks"))
total= ph+c+b+m+co 
per=total/5
if per>= 90 :
    print("Grade A")
elif per>=80 :
    print("Grade B")
elif per>=70 :
    print("Grade C")
elif per>=60 :
    print("Grade D")
elif per>=40 :
    print("Grade E")
else :
    print("Grade F")
