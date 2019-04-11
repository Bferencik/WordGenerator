import wordList #For object 'wordList' 
import sys      #system arguments

def main(): 

    MasterList = wordList.wordList()

    #If bad string entered, return
    if(MasterList.setTestString(sys.argv[2]) == False):
        return 
        
     #if input file does not exist, return   
    if(MasterList.loadContent(sys.argv[1]) == False): 
        return 

    MasterList.createWords()
    MasterList.clean()
    MasterList.displayWords()

main()