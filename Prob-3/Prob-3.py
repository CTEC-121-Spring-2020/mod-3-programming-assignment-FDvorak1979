# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Frank Dvorak

def letterGrade(score):
    if score == 5:
        grade = 'A'
    elif score == 4:
        grade = 'B'
    elif score == 3:
        grade = 'C'
    elif score == 2:
        grade = 'D'
    elif score == 1:
        grade = 'F'
    elif score == 0:
        grade = 'F'
    return grade

    

def unitTest():
    print("Score = 5 Returns", letterGrade(5))
    print("Score = 4 Returns", letterGrade(4))
    print("Score = 3 Returns", letterGrade(3))
    print("Score = 2 Returns", letterGrade(2))
    print("Score = 1 Returns", letterGrade(1))
    print("Score = 0 Returns", letterGrade(0))

if __name__ == "__main__":
    unitTest()
