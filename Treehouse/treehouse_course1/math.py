test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
min_grade = min(test_grades)
print(f"The minimum grade is: {min_grade}")

test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
max_grade = max(test_grades)
print(f"The maximum grade is: {max_grade}")


test_grades.sort()
print(test_grades)


essay_grades = [93, 97, 84, 91, 87, 68, 63, 72, 75, 89]
essay_grades.sort()
print(essay_grades)


from statistics import median

test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
essay_grades = [93, 97, 84, 91, 87, 68, 63, 72, 75, 89]

median_grade = median(test_grades)
median_essay = median(essay_grades)
print(f"The median test grade is: {median_grade}")
print(f"The median essay grade is: {median_essay}")