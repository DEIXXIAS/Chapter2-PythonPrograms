
# ------------------------------------- MAIN FUNCTIONS --------------------------------- #

def balancedParenthesis(balanceInput):
    # MAIN DEFINTION
    stackVerifier = [] # STACK VERIFIER FOR THE BALANCE INPUT
    for index in balanceInput: # WHILE GOING THROUGH THE INDEXES IN THE BALANCE LIST
        if index == "(": # IF THE INDEX CONTAINS A OPEN PARENTHESIS
            stackVerifier.append(index) # APPEND IT TO THE STACK VERIFIER
        elif index == ")": # IF THE INDEX CONTAINS A CLOSE PARENTHESIS
            if not stackVerifier: # IF THE VERIFY LIST IS EMPTY
                return False # RETURN AS FALSE
            else: # IF THE VERIFY LIST IS NOT EMPTY
                stackVerifier.pop() # POP THE ITEM IN THE STACK VERIFIER
    return len(stackVerifier) == 0 # THEN RETURN LIST AS ZERO BC WE ONLY NEED THE T/F VALUE

# --------------------------------------Main Program-------------------------------------#
# BALANCE INPUT IS THE LIST FOR USER INPUT
balanceInput = []
# PRINT OUT EXPRESSION TO FIND THE INPUT
balanceInput = input(str("\nEnter the expression:"))

# IF THE BALANCE DEFINITION TRUE
if balancedParenthesis(balanceInput):
    print("\nThe parenthesis are balanced!") # PRINT THAT THEY ARE BALANCED
else: # IF FALSE
    print("\nThe parenthesis are not balanced.") # PRINT THAT THEY ARE NOT BALANCED