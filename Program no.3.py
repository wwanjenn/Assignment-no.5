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
    while True:
        try:
            ageI = int(input('Age: '))
            if ageI >= 0:
                return ageI
            elif ageI < 0:
                print('Please Enter Valid Age.')
                exit()
        except ValueError:
            print('Please Enter Valid Age.')
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
    return stageF
# 3 Print
def printFunction(stageP):
    print(f'Life Stage: {stageP}')
# 4 Call for function
 
age = inputAge()

stage = ifElse(age)

printFunction(stage)
