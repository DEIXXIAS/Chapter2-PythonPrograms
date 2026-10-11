# main function --------------------------------------------

def palindrone(userInput): # WHILE IN THE FUNCTION
    palindromeCheck = False # INITIALIZE THE PALINDROME CHECKER
    if userInput == userInput[::-1]: # WHILE THE USER INPUT IS THE SAME AS IT BACKWARDS
        palindromeCheck = True # THE PALINDRONE WILL BE TRUE
    else: # IF THE USER INPUT IS NOT THE SAME BACKWARDS
        palindromeCheck = False # THE PALINDRONE IS FALSE
    return palindromeCheck # RETURN THE PALINDRONE CHECKER


# MAIN PROGRAM ---------------------------------------------
# PRINT TO GET THE STRING FROM THE USER
userInput = input("\nEnter a string to get the palindrome: ") # STORE IT IN USERINPUT

# IF THE PALINDRONE CHECKER IS TRUE
if palindrone(userInput):
    print("\nThe palindrome is balanced!") # MESSAGE WILL PRINT
else: # IF IT IS NOT A PALINDRONE
    print("\nThe palindrome is not balanced!") # MESSAGE WILL PRINT

