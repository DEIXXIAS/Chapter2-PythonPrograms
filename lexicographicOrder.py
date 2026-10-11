# Main function -------------------------------------------

def lex_insert(L, a, b):
    tuplePair = (a, b) # create a tuple using the variables in the elements in the definition

    insertedPair = False # while the inserted pair has not been appended

    for index in range(len(L)): # while the index goes through the range of the length of previous appended list
        if tuplePair < L[index]: # if the tuple is greater than the previous tuple
            L.insert(index, tuplePair) # insert it into the index using the tuple pair
            insertedPair = True
            break


    if not(insertedPair):
        L.append(tuplePair)

# MAIN Program ------------------------------------------------

List = []
#storing the lists
lex_insert(List, 0, 1) # inserting the list using the functions
lex_insert(List, 12, 15)
lex_insert(List, 5, 24)
lex_insert(List, 3, 1)
lex_insert(List, 6, 3)
lex_insert(List, 7, 4)

#printing the list once all of the lists have gone through the function
print("\nThe sorted list is ", List)








