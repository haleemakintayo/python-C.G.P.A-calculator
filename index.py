# CGPA calculator
username = input('Kindly enter your name:')
courses_Num = int(input('How many courses do you offer?'))

course_list = []
unit_list = []
score_list = []
grade_list = []
point_list = []
total_points = 0
total_units = 0

for i in range(courses_Num):
    course = input(f'Enter the course title {i + 1}: ')
    unit = int(input('Enter the course unit: '))
    score = int(input('Enter your score: '))

    # Calculate grade
    if 70 <= score <= 100:
        grade = 'A'
        points = 5.0
    elif 60 <= score < 70:
        grade = 'B'
        points = 4.0
    elif 50 <= score < 60:
        grade = 'C'
        points = 3.0
    elif 45 <= score < 50:
        grade = 'D'
        points = 2.0
    elif 40 <= score < 45:
        grade = 'E'
        points = 1.0
    else:
        grade = 'F'
        points = 0.0

    # Append values to lists
    course_list.append(course)
    unit_list.append(unit)
    score_list.append(score)
    grade_list.append(grade)
    point_list.append(points)

    # Update total points and total units
    total_points += points * unit
    total_units += unit

# Calculate CGPA
cgpa = total_points / total_units

# Display results
print('\nCGPA CALCULATION RESULTS')
print(f'Student: {username}')
print(f'Total Points: {total_points}')
print(f'Total Units: {total_units}')
print(f'CGPA: {cgpa:.2f}')
