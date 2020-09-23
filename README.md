﻿# Password_Validation_problem

We call a password secure if it contains no space characters and consists of at least six characters, 
including at least one digit, one lowercase letter, one uppercase letter, and one special character. For the purpose of this task, we will consider just the following characters to be special: !@#$%^&*()_ 
Write a function: 

def  solutlont(s ) 

that, given a string S of length N, returns True if S is secure (as described above), and returns False if it is not secure. 

Examples: 
1 . Given string S: 'FooBarl^231', the function should return True. 
2. Given string S: 'foobarl231!', the function should return False, because there is no uppercase letter. 

3. Given string S 'FooBarl 23', the function should return False, because there is no special character. 

4. Given string S: 'FObar! FObar!', the function should return False, because string S contains a space, which is not a special character. 
5. Given string S: 'FoO*' the function should return False because string S is too short 

Assume that: 

    -the length of S is within the range lO..1 00l; 
    -S consists only of English should or uppercase letters, digits, spaces, and special characters. as indicated above; 
    -spaces won't appear as the first or last character of any password. 
In your solution, focus on correctness. the performance of your solution will not be the focus of the assessment. 

