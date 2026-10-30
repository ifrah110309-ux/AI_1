name=input("Enter Student Name:-")
n=int(input("Enter Number Of Subjects:-"))
total=0
for i in range(1,n+1):
 mark=float(input(f"Enter mark for Sub{i}:"))
 total+=mark
 percentage=total/n
if percentage>=90:
    grade="A+"
    performance="Outstanding"
elif percentage>=80:
    grade="A"
    performance="Excellent"
elif percentage>=70:
    grade="B"
    performance="Very Good"
elif percentage>=60:
    grade="C"
    performance="Good"
elif percentage>=50:
    grade="D"
    performace="Average"
else:
    grade="F"
    performance="Needs Improvement"
print("\n---Academic Performance---")
print("Student Name:-",name)
print("Total Marks:-",total)
print("Percentage:",round(percentage,2),"%")
print("Grade:-",grade)
print("Performance:-",performance)

