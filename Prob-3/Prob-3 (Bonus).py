# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Frank Dvorak

def letterGrade(score):
    if score >= 94:
        grade = 'A'
    elif score < 94 and score >= 90:
        grade = 'A-'
    elif score < 90 and score >= 87:
        grade = 'B+'
    elif score < 87 and score >= 84:
        grade = 'B'
    elif score < 84 and score >= 80:
        grade = 'B-'
    elif score < 80 and score >= 75:
        grade = 'C+'
    elif score < 75 and score >= 70:
        grade = 'C'
    elif score < 70 and score >= 65:
        grade = 'C-'
    elif score < 65 and score >= 50:
        grade = 'D'
    elif score < 50 and score >= 0:
        grade = 'F'
    return grade

    

def unitTest():
    print("Score = 96 Returns", letterGrade(96))
    print("Score = 92 Returns", letterGrade(92))
    print("Score = 88.6 Returns", letterGrade(88.6))
    print("Score = 84.3 Returns", letterGrade(84.3))
    print("Score = 82.9 Returns", letterGrade(82.9))
    print("Score = 77.7 Returns", letterGrade(77.7))
    print("Score = 71.3 Returns", letterGrade(71.3))
    print("Score = 66.6 Returns", letterGrade(66.6))
    print("Score = 53.3 Returns", letterGrade(53.3))
    print("Score = 1.5 Returns", letterGrade(1.5))

if __name__ == "__main__":
    unitTest()
