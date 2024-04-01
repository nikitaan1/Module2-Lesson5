#Task1

def grades(results):
    
    result = sum(results) / len(results)
    return result

all_grades = [80, 55, 43, 95, 97, 66, 41]


average_grade = grades(all_grades)

print(f"The average grade is: {average_grade}")

#Task 2

def find_highest_and_lowest(grades):
    highest_grade = max(grades)
    lowest_grade = min(grades)
    return highest_grade, lowest_grade

all_grades = [80, 55, 43, 95, 97, 66, 41]
highest, lowest = find_highest_and_lowest(all_grades)

print(f"Highest grade: {highest}")
print(f"Lowest grade: {lowest}")

#Task 3

def categorize_grade(grade):
    
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

categorized_grades = [categorize_grade(grade) for grade in all_grades]
print(f"Categorized Grades: {categorized_grades}")

