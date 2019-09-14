"""
Name: William Davies
Date: 12.09.19 - ONGOING
Program: File Runner 9000
"""

# Imports
from datetime import datetime
from os import listdir, system

# Variable Initialisation
asking = True
uinp = ""
REGISTRY = []
# Functions
def quitProgram():
    print("Thank You For Using My Program!")
    input()
    quit()

def runFile(filenum):
    system('python "pyfiles/' + REGISTRY[filenum-1][2] + '.py"')

def addToRegistry(ind,filename,programname):
    REGISTRY.append([ind, filename, programname])

def initialiseRegistry():
    #print("Reg Init")
    for i in REGISTRY: REGISTRY.remove(i)
    pyfilesfolder = listdir("pyfiles")
    for i in pyfilesfolder:
        if i[-3:] != ".py":
            pyfilesfolder.remove(i)
    for i in range(len(pyfilesfolder)):
        found = False
        for j in REGISTRY:
            if pyfilesfolder[i] in j:
                found = True
                break
        if pyfilesfolder[i][-3:] == ".py" and found == False:
            addToRegistry(i + 1,pyfilesfolder[i],pyfilesfolder[i][:-3])
        
    #print(REGISTRY)
    REGISTRY.sort()

def printRegistry():
    for i in range(len(REGISTRY)):
        print("{}: {}".format(REGISTRY[i][0],REGISTRY[i][2]))
    print("{}: Make File".format(len(REGISTRY) + 1))
    print("{}: EXIT".format(len(REGISTRY) + 2))

def makeFile():
    undate = datetime.now()
    tdate = "{}.{}.{}".format(undate.strftime("%d"),undate.strftime("%m"),undate.strftime("%y"))
    fasking = True
    while fasking:
        fname = input("What Is The Python File Called > ")
        if fname == "": print("False Input!")
        else: fasking = False
    system('type tempst.txt >> "pyfiles/{}.py"'.format(fname))
    system('echo {} >> "pyfiles/{}.py"'.format(tdate,fname))
    system('type tempnd.txt >> "pyfiles/{}.py"'.format(fname))

def runLogic(uInp):
    # TDOD: Integrate makeFile and quitProgram into initialiseRegistry
    if uInp == len(REGISTRY) + 1: makeFile(); return
    if uInp == len(REGISTRY) + 2: quitProgram()
    runFile(uInp)

# Main Function
def main():
    while True:
        # Variable Redefinition
        asking = True
        # Initialise The Registry
        initialiseRegistry()

        # User Input
        print("Python File Index V1.0")
        printRegistry()
        while asking:
            uinp = input("> ")
            try:
                uinp = int(uinp)
                if uinp < 1 or uinp > len(REGISTRY) + 2: break
                asking = False
            except:
                print("Incorrect Input!")
        system('cls')
        runLogic(uinp)
        input("<ENTER> To Continue")
        system('cls')

# Run Code
if __name__ == '__main__':
    main()
