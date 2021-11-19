# # Program 3: Life stages
# # Create a program that ask for an age of a person
# # Display the life stage of the person.
# # Rules:
# # 0 - 12 : Kid
# # 13 - 17 : Teen
# # 18 : Debut
# # 19 above : Adult

# Steps
# 1 Ask for age
def inputAge():
    ageI = int(input('Age: '))
    return ageI

# 2 If else statement
def ifElsePrint(ageF):
    if ageF >= 0 and ageF <= 12:
        ageE = 'Kid'
    elif ageF >= 13 and ageF <= 17:
        ageE = 'Teen'
    elif ageF == 18:
        ageE = 'Debut'
    elif ageF > 18:
        ageE = 'Adult'

# 3 Print

# 4 Call for function