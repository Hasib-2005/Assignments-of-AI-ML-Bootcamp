# Entire implementation was done by me.
# All comments and explanations were written by me.
# No external assistance was used.


# building a simple student grade management system

##### task a: asking user to enter his/her name and number of subjects between 1 & 5
name = input('Enter your name: ')
numOfSubjects = int(input("Enter number of subjects (1 - 5) : "))
#Printing Welcome message using f-string
print(f"Welcome to Grade Report Maker Site {name}")


##### Task c:
#function to calculate total marks, average score, highest score, and lowest score.
def calculate_stats(subjectScores):
    total_mark = 0
    average_score = 0
    highest_score = max(subjectScores)
    lowest_score = min(subjectScores)
    for x in subjectScores:
        total_mark += x
    list_size = len(subjectScores)
    average_score = total_mark / list_size

    # making a tuple with the values to return
    tupleval = (total_mark, average_score, highest_score, lowest_score)
    return  tupleval


##### Task d :
# function to check the grade
def assign_grade(average):
    if (average >= 80) :
        return 'A'
    elif (average >= 65) :
        return 'B'
    elif (average >= 50) :
        return 'C'
    elif (average >= 35) :
        return 'D'
    else:
        return 'F'

##### Task b:
# declaring a list to store scores of the subjects
subjectScores = []
# print(type(subjectScores))

# collecting scores using a for loop from user & if score is not valid, asking user to re-enter the score unless he/she enters a valid score
for i in range (0, numOfSubjects):
    perSubjectScore = int(input(f"Enter {i + 1}th subject score: "))
    while (perSubjectScore < 0 or perSubjectScore > 100):
        perSubjectScore = int(input(f"Score should be between (0 - 100)\nEnter {i + 1}th subject score again: "))
    # adding scores to the list
    subjectScores.append(perSubjectScore)

#print(subjectScores)
# storing total marks, average score, highest score, and lowest score in a tuple named tupleval
# calling calculate_stats function to calculate those and to return as tuple
tupleval = calculate_stats(subjectScores)

#calling function name assign_grade to check the average mark and determine which grade the student actually got
Grade = assign_grade(tupleval[1])

##### Task e:
# declaring a list to store the scores which are pass marks
passed_subjects = []
for x in subjectScores:
    if (x >= 50):
        passed_subjects.append(x)

# checking how many subject does he/she passed in
passed_in = len(passed_subjects)

##### Task e : 
# final printing as the assignment requires
print("========== Grade Report ==========")
print(f"Student  : {name}")
print(f"Scores   : {subjectScores}")
print(f"Total    : {tupleval[0]}")
print(f"Average  : {tupleval[1]:.2f}")
print(f"Highest  : {tupleval[2]}  |  Lowest: {tupleval[3]}")
print(f"Grade    : {Grade}")
print(f"Passed   : {passed_in} out of {len(subjectScores)} subjects")




