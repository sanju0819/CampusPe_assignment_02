# grade calculator program
# this calculates total marks, percentage, grade and result

marks = []
for i in range(1, 6):
    mark = float(input(f"enter marks for subject {i}: "))  
    marks.append(mark)

total = sum(marks)           # add all marks
percent = total / 5          # divide by 5 to get percentage
# check grade based on percentage
if percent >= 90:
    grade = "A+ (Outstanding)"
elif percent >= 80:
    grade = "A (Excellent)"
elif percent >= 70:
    grade = "B (Good)"
elif percent >= 60:
    grade = "C (Average)"
elif percent >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"
# pass only if every subject has 40 or more marks
result = "Pass" if all(m >= 40 for m in marks) else "Fail"
print("\n--- Result Card ---")
for i, m in enumerate(marks, 1):
    print(f"subject {i}: {m}")   # print each subject mark
print("total:     ", total, "/ 500")
print("percentage:", percent, "%")
print("grade:     ", grade)
print("result:    ", result)