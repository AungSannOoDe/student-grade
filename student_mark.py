
name = input("Enter student's name: ")

mark1 = float(input("Enter mark for subject 1: "))
mark2 = float(input("Enter mark for subject 2: "))
average = (mark1 + mark2) / 2

if average >= 50:
    result = "Pass"
else:
    result = "Fail"

print("Student Name:", name)
print("Total Mark:", int(total))
print("Average Mark:", int(average))
print("Result:", result)
