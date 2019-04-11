import combinatorics

class wordList:

    #initialization

    def __init__(self):
        self.wordPath = ""
        self.content = []
        self.testString = ""
        self.Words = []
        self.pSet = []


    #Sets our word string to the input string. If there are any numbers in the string, return false
    #Also, if string is valid, creates power set with elements of the string. Refer to combinatorics.powerSet for algorithm

    def setTestString(self,inputString):

        for i in range(len(inputString)):

            char = inputString[i]

            if(char.isalpha() == False):
                print("\nERROR: STRING NOT VALID\n")
                return False

        self.testString = inputString 
        self.pSet = combinatorics.powerSet(list(inputString))
        return True



    #loadContent loads dictionary words into content list
    #Raises error if input file does not exist

    def loadContent(self,inputFile):

        try:
            self.wordPath = open(inputFile,'r')
        
        except IOError:
            print("\nERROR: FILE DOES NOT EXIST\n")
            return False

        line = self.wordPath.readline()
        line = line.rstrip('\n')

        while(line != '' ):
            self.content.append(line)
            line = self.wordPath.readline()
            line = line.rstrip('\n')

        return True
   
    #createWords creates a tempList with the permutations of the power set. Then, the tempList is iterated 
    #through to check if entries in tempList are actual words. This is accomplished by refering to the 
    #dic.txt file

    def createWords(self):

        if(self.testString == ''):
            print("\nERROR: 'testString' NOT LOADED\n")
            return

        elif(len(self.content) == 0):
            print("\nERROR: content not loaded\n")
            return

        for i in range(len(self.pSet)):

            tempList = combinatorics.permutation(self.pSet[i])

            for j in range(len(tempList)):

                tempString = combinatorics.listToString(tempList[j])

                if(tempString in self.content):
                    self.Words.append(tempString)

#Cleans list. Free list of duplicate entries

    def clean(self):

        temp = []

        for i in range(len(self.Words)):

            if(self.Words[i] not in temp):
                
                temp.append(self.Words[i])

        
        self.Words = temp

    
    #Display

        
    def displayWords(self):

        print('\n')

        for i in range(3,len(self.testString)+1):

            print("Length = ",i)
            print("---------")

            for j in range(1,len(self.Words)):

                if(len(self.Words[j]) == i):
                    print(self.Words[j])

            print('\n')

    