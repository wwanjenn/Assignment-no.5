# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

# Steps 
# 1 Ask for 3 numbers
def threeNumbers():
    firstNumberI = int(input('1st Number: '))
    secondNumberI = int(input('2nd Number: '))
    thirdNumberI = int(input('3rd Number: '))
    return firstNumberI, secondNumberI, thirdNumberI
# 2 If else statments
def ifElsePrint(firstNumberP, secondNumberP, thirdNumberP):
    if firstNumberP <= secondNumberP and firstNumberP <= thirdNumberP:
        print(f'The Lowest Number is {firstNumberP}.')
    elif secondNumberP <= firstNumberP and secondNumberP <= thirdNumberP:
        print(f'The Lowest Number is {secondNumberP}.')
    elif thirdNumberP <= firstNumberP and thirdNumberP <= secondNumberP:
        print(f'The Lowest Number is {thirdNumberP}.')
# 3 Calling of Function

firstnumber, secondnumber, thirdnumber = threeNumbers()

ifElsePrint(firstnumber, secondnumber, thirdnumber)