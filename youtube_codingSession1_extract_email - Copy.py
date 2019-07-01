# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:41:10 2019
youtube video: 
https://www.youtube.com/watch?v=W1Nbkzmnyis
1h14
@author: User
"""
# Given a string, extract the email address from string typed in by a user 
# If there is no email address, print an appropriate error message
# Other specifications: 
#     - assume only string contains no more than one address 
#     - no special characters other than @ and . will be given by user 
#     - email address will be denoted between spaces 
#     - for example: hello a@b this@example.where this@.is.fun will print
#       this@example.where

"""
sometext@othertext.moretext
- @ and .
- @ before .
- @ and . not next to each other
- no multiple dots
- does not start with @
- does not end with .

"""
# checks whether string is a valid email address


"""
still to do:
 - email at the end - I don't have the last letter
    
Please enter a string: JKK GG  sss@gg.cc
Address is:   sss@gg.c

 - other email verifications
 - 
"""
def is_valid_address(some_string):
    pos_at = some_string.find('@')
    pos_dot = some_string.find('.')
    if pos_at == -1 or pos_dot == -1:
        return False
    if pos_at > pos_dot:
        return False
    if abs(pos_at-pos_dot) == 1:
        return False
    if some_string.count('.') > 1 or some_string.count('@') > 1:
        return False
    if pos_at == 0  or pos_dot == (len(some_string)-1):
        return False
    return True

print(is_valid_address("df abcgjk@255.123 tykyk  "))

# get user input

user_input = input("Please enter a string: ") #.strip()

if '@' not in user_input:
    print("No valid email address found.")
elif ' ' not in user_input:
    if is_valid_address(user_input):
        print("Address is: ", user_input)
    else:
        print("No valid email address found.")
else:
    # case where user enters string with spaces
    at = 0
    # case where valid address is the first string before any spaces
    start = 0
    end = user_input.find(' ', start+1)
    if is_valid_address(user_input[start:end]):
        print("Address is: ", user_input[start:end])
    else:
        while True:
            start = user_input.find(' ', at)
            end = user_input.find(' ', start+1)   # next spaces after start
            print("Start = ", start, "end = ", end)
            if is_valid_address(user_input[start:end]):
                print("Address is: ", user_input[start:end])
                break
            else:
                at = end 
                # valid email not found and reached end of input string
                if at == -1:
                    print("No email address found.")
                    break
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





