# STUDENT GRADING SYSTEM

student_number = input("Enter number of student: ")

students_all_data =[]
student_percent = []
student_grade = []

def myGrade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 65:
        return "C"
    elif percent >= 50:
        return "D"
    elif percent >= 35:
        return "E"
    else:
        return "F"

for student in range(int(student_number)):
    student_name = input("Enter Student name: ")
    student_data = []
    student_data.append(student_name)
    for subject in range(1):
        student_marks =[]
        English = int(input("Enter English Marks: "))
        student_marks.append(English)
        Hindi = int(input("Enter Hindi Marks: "))
        student_marks.append(Hindi)
        Marathi = int(input("Enter Marathi Marks: "))
        student_marks.append(Marathi)
        Science = int(input("Enter Science Marks: "))
        student_marks.append(Science)
        student_data.append(student_marks)
       
        percent = float(((English + Hindi + Marathi +Science) / 400) * 100)
        student_data.append(percent)
        grade = myGrade(percent)
        student_data.append(grade)
        students_all_data.append(tuple(student_data))


sorted_students = sorted(students_all_data, key=lambda x: x[2], reverse=True)


print("===================================================================================")
print("===================================================================================")
print("STUDENT GRADING SYSTEM")
print("===================================================================================")
print("===================================================================================")

for x in students_all_data:
     print(f"Student Name: {x[0]}")
     print(f"Student Percent: {x[2]}")
     print(f"Grade: {x[3]}")
     print("-------------------------------------")


print("===================================================================================")
print("Topper List")
print("===================================================================================")
for i, student in enumerate(sorted_students, start=1):
    print(f"        {i} :  {student[0]}  |  {student[2]}")


print("-------------------------------------")
# Highest and lowest grade average
highest = sorted_students[0][2]
lowest = sorted_students[-1][2]

print(f"Highest Grade :  {highest}")
print(f"Lowest Grade :  {lowest}")

print("===================================================================================")



