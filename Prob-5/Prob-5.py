# Module 3
#   Programming Assignment 4
#     Prob-5.py

# <YOUR NAME>

def main():
    try:    
        x = eval(2)
        print("x:", x)
        
    except TypeError:
        print("Invalid input, must be string, bytes or code")
    
    except SyntaxError:
        print("missing indented block in Line 20")
main()