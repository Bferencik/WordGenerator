# Borrowed permutation algorithm. Takes a list and returns all possible permutations of the list. See 
# https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/


def permutation(lst):

    if len(lst) == 0: 

        return [] 

    if len(lst) == 1:
        
        return[lst]

    l = []

    for i in range(len(lst)):

        m = lst[i]

        remLst = lst[:i] + lst[i+1:]

        for p in permutation(remLst):
            l.append([m] + p)
 
    
    return l

#Uses the bijection between binary numbers to power sets to create the power set. For example,
# if binary string is '100' for S = {a,b,c}, then the corresponding subset would be {a}
# Example 2: binary string '101' for S = {a,b,c} has subset {a,c}


def powerSet(lst):

    pSet = []
    subSet = []

    for i in range(1,2 ** len(lst)):

        binary = bin(i)[2:]     #Create binary string
        subSet = []

        if(len(binary) < len(lst)):
            while(len(binary) < len(lst)):

                binary = '0' + binary       #if length of binary string not equal to length of list, 
                                            #push 0's to front
                                            
        for j in range(len(binary)):

            if(binary[j] == '1'):           #Decribing the bijection, if 1 in string then corresponding element in subset
                subSet.append(lst[j])

        pSet.append(subSet)

    return pSet


#Converts list to string


def listToString(lst):

    string = ''

    for i in range(len(lst)):

        string = string + str(lst[i])

    return string