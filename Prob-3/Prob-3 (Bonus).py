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
    print("Torm got 100 and earnned an", letterGrade(100))
    print("Azael got 92 and earnned an", letterGrade(92))
    print("Blain got 88.6 and earned a", letterGrade(88.6))
    print("Lucian got 84.6 and earned a", letterGrade(84.3))
    print("One of Lucian's emoloyies earned a 82.9 Returns", letterGrade(82.9))
    print("Amaon was drunk as usual and when taking the test only got 77.6", letterGrade(77.7))
    print("Aarron did not study and was out all night being a vigilanty and got 71.3 ", letterGrade(71.3))
    print("Some one, who wishes to remain anonamous out of shame got 66.6", letterGrade(66.6))
    print("Rockanoth was working all night than got drunk and came to the test with a hang over and got 53.3 Returns", letterGrade(53.3))
    print("Grim got 1.5 and earned an", letterGrade(1.5))

if __name__ == "__main__":
    unitTest()
