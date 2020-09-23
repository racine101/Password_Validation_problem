#import the regular expression module
import re

#the solution function validates the password passed to it
def solution(S):
    # this loop will run until False in invoke 
    while True:
        if (len(S)<6):#check that the lenght of S is more than 6
            return False
        elif not re.search(r"[a-z]", S):#use the regular expression search function to check for lowercase letters
            return False
        elif not re.search(r"[A-Z]", S):#use the regular expression search function to check for uppercase letters
            return False
        elif not re.search(r"[0-9]", S):#use the regular expression search function to check for digits
            return False
        elif not re.search(r"[!@#\$%^&\*()_]", S):#use the regular expression search function to check for special characters 
            return False
        elif re.search(r'\s', S):#use the regular expression search function to check for white spaces
            return False
        else:#if the previous checks pass the function will return True
            return True

#password 
password = "mJGdp499&"

#calling the function and printing the return value to the terminal
print(solution(password))
