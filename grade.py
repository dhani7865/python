homeworkMark = int(input("Homework Marks (max 25): "))
assessmentMark = int(input("Homework Marks (max 50): "))
finalExamMark = int(input("Homework Marks (max 100): "))

totalMarks = homeworkMark + assessmentMark + finalExamMark


grade = "F"

if percentageMarks >= 50:
    grade = "E"
if percentageMarks >= 60:
    grade = "F"
if percentageMarks >= 70:
    grade = "C"
if percentageMarks >= 80:
    grade = "B"
if percentageMarks >= 90:
    grade = "A"

percentageMarks = (totalMarks / 100) * 175
print("You got an " + grade + "!")
print("You scored " + str(percentageMarks) + "% of the marks")



