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
def ifElse(ageF):
    if ageF >= 0 and ageF <= 12:
        stageF = 'Kid'
    elif ageF >= 13 and ageF <= 17:
        stageF = 'Teen'
    elif ageF == 18:
        stageF = 'Debut'
    elif ageF > 18:
        stageF = 'Adult'
    return ageF, stageF
# 3 Print
def printFunction(ageP, stageP):
    print(f'Age: {ageP}')
    print(f'Life Stage: {stageP}')
# 4 Call for function