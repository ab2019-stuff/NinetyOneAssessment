
import Code
print('please make sure the file you wish to parse is in the correct directory')
print('please enter the name of the txt file you would like to parse e.g. file1 or file1.txt and press enter')
print('(if you want to run the provided test cases please type in \'Test\')')
print('the dictionary object \'Numbers\' will contain a list of the integers in each line of the file indexed by the line number')
file=input()
Numbers=None
while Numbers==None:
    try:
        Numbers = Code.readFile(file)
    except:
        print('sorry invalid option please check the file name and directory and try again!')
        file = input()




