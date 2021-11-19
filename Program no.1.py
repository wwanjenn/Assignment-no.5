# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

# grade/mark    percentage     description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.50          79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropeed

#Steps
#1 Ask for grade percentage
def inputGrade():
    percentGradeI = input('Grade Percentage(65-100): ')
    return percentGradeI
#2 If else statements
def ifElse(percentGradeC):
        # Incomplete
    if percentGradeC == 'Incomplete' or percentGradeC == 'Inc.':
        gradeMarkC = 'Inc.'
        descriptionC = 'Incomplete' 
    # Withdrawn
    elif percentGradeC == 'Withdrawn' or percentGradeC == 'W':
        gradeMarkC = 'W'
        descriptionC = 'Withdrawn'
    # Dropped
    elif percentGradeC == 'Dropped' or percentGradeC == 'D':
        gradeMarkC = 'D'
        descriptionC = 'Dropped'
    else:
        percentGradeC = float(percentGradeC)
    #2.1
        if percentGradeC >= 97 and percentGradeC <= 100:
            gradeMarkC = 1.0
            descriptionC = 'Excellent'
    #2.2
        elif percentGradeC >= 94 and percentGradeC <= 96:
            gradeMarkC = 1.25
            descriptionC = 'Excellent'
    #2.3
        elif percentGradeC >= 91 and percentGradeC <= 93:
            gradeMarkC = 1.5
            descriptionC = 'Very Good'
    #2.4
        elif percentGradeC >= 88 and percentGradeC <= 90:
            gradeMarkC = 1.75
            descriptionC = 'Very Good'
    # 2.5
        elif percentGradeC >= 85 and percentGradeC <= 87:
            gradeMarkC = 2.0
            descriptionC = 'Good'
    # 2.6
        elif percentGradeC >= 82 and percentGradeC <= 84:
            gradeMarkC = 2.25
            descriptionC = 'Good'
    # 2.7
        elif percentGradeC >= 79 and percentGradeC <= 81:
            gradeMarkC = 2.5
            descriptionC = 'Satisfactory'
    # 2.8
        elif percentGradeC >= 76 and percentGradeC <= 78:
            gradeMarkC = 2.75
            descriptionC = 'Satisfactory'
    # 2.9
        elif percentGradeC > 74 and percentGradeC <= 76:
            gradeMarkC = 3.0
            descriptionC = 'Passing'
    # 2.10
        elif percentGradeC >= 65 and percentGradeC <= 74:
            gradeMarkC = 5.0
            descriptionC = 'Failure'
    return gradeMarkC, descriptionC

#Print
def output(percentGradeP, gradeMarkP, descriptionP):
    print(f'Input Grade: {percentGradeP}')
    print(f'Grade/Mark: {gradeMarkP}')
    print(f'Description: {descriptionP}')

percentGrade = inputGrade()
gradeMark, description = ifElse(percentGrade)
output(percentGrade, gradeMark, description)