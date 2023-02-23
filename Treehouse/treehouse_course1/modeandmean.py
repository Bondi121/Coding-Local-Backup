from statistics import mode

test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
test_mode = mode(test_grades)
print(f"The most often seen grade is: {test_mode}")



from statistics import mode

essay_grades = [63, 68, 72, 75, 84, 87, 89, 91, 93, 97]
essay_mode = mode(essay_grades)
print(f"The most often seen essay grade is: {essay_mode}")




from statistics import mode

project_grades = [80, 75, 68, 80, 92, 84, 77, 100, 100, 88, 82]
project_mode = mode(project_grades)
print(f"The most often seen project grade is: {project_mode}")




from statistics import multimode

project_grades = [80, 75, 68, 80, 92, 84, 77, 100, 100, 88, 82]
project_mode = multimode(project_grades)
print(f"The most often seen project grade is: {project_mode}")




from statistics import mean

test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
essay_grades = [63, 68, 72, 75, 84, 87, 89, 91, 93, 97]

test_average = mean(test_grades)
essay_average = mean(essay_grades)

print(f"The average test grade is: {test_average}")
print(f"The average essay grade is: {essay_average}")






test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]

passed = 0
total_grades = len(test_grades)

for grade in test_grades:
    if grade >= 70:
        passed += 1

percentage_passed = round(passed / total_grades * 100)

print(f"The number of students who passed: {passed}")
print(f"The number of students who did not pass: {total_grades - passed}")
print(f"The percentage of students who passed: {percentage_passed}")
print(f"The percentage of students who did not pass: {100 - percentage_passed}")

print ("hello1")
print ("hello2")
