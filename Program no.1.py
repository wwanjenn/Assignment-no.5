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
    percentGradeI = input('Grade Percentage: ')
    return percentGradeI
#2 If else statements
def ifElse(percentGradeC):
        # Incomplete
    if percentGradeC = 'Incomplete' or percentGradeC = 'Inc.':
        gradeMark = 'Inc.'
        description = 'Incomplete' 
    # Withdrawn
    elif percentGradeC = 'Withdrawn' or percentGradeC = 'W':
        gradeMark = 'W'
        description = 'Withdrawn'
    # Dropped
    elif percentGradeC = 'Dropped' or percentGradeC = 'D':
        gradeMark = 'D'
        description = 'Dropped'
    else:
        percentGradeC = float(percentGradeC)
    #2.1
        if percentGradeC >= 97 or percentGradeC <= 100:
            gradeMark = 1.0
            description = 'Excellent'
    #2.2
        elif percentGradeC >= 94 or percentGradeC <= 96:
            gradeMark = 1.25
            description = 'Excellent'
    #2.3
        elif percentGradeC >= 91 or percentGradeC <= 93:
            gradeMark = 1.5
            description = 'Very Good'
    #2.4
        elif percentGradeC >= 88 or percentGradeC <= 90:
            gradeMark = 1.75
            description = 'Very Good'
    # 2.5
        elif percentGradeC >= 85 or percentGradeC <= 87:
            gradeMark = 2.0
            description = 'Good'
    # 2.6
        elif percentGradeC >= 82 or percentGradeC <= 84:
            gradeMark = 2.25
            description = 'Good'
    # 2.7
        elif percentGradeC >= 79 or percentGradeC <= 81:
            gradeMark = 2.5
            description = 'Satisfactory'
    # 2.8
        elif percentGradeC >= 76 or percentGradeC <= 78:
            gradeMark = 2.75
            description = 'Satisfactory'
    # 2.9
        elif percentGradeC > 74 or percentGradeC <= 76:
            gradeMark = 3.0
            description = 'Passing'
    # 2.10
        elif percentGradeC >= 65 or percentGradeC <= 74:
            gradeMark = 5.0
            description = 'Failure'
    return gradeMark, description

#Print

