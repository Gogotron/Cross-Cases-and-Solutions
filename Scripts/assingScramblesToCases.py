from ast import literal_eval as litEval
from cubeScrambling import applyMoves as scrambleACube

crossCasesLocation=r"C:\Users\ggtrn\Desktop\Cross Cases and Solutions\Files"+"\\"
scramblesLocation=r"F:"+"\\"
solutionsSaveLocation=r"C:\Users\ggtrn\Desktop\Cross Cases and Solutions\Files\Solution Files"+"\\"

def addSolutionScrambleToCaseList(case,scramble):
        if len(casesDict[case])==0 or len(scramble)==len(casesDict[case][0]):
                casesDict[case].append(scramble)
        elif len(scramble)<len(casesDict[case][0]):
                casesDict[case]=[scramble]

def testScrambleForCases(scramble):
        scrambledState = scrambleACube(scramble)
        if scrambledState in casesDict:
                addSolutionScrambleToCaseList(scrambledState,scramble)


with open(crossCasesLocation+"crossCases.txt",'r') as casesFile:
        casesDict = {line.strip("\n"):[] for line in casesFile}

print("Starting reduction of solutions.")
testScrambleForCases([])
totalCompletion = 0
for i in range(18):
        with open(scramblesLocation+"possible7MoveScrambles"+str(i)+".txt",'r') as scramblesFile:
                partialCompletion=0
                for line in scramblesFile:
                        scramble = litEval(line)
                        testScrambleForCases(scramble)
                        partialCompletion+=1
                        totalCompletion+=1
                        if partialCompletion%5000==0:
                                print(str(totalCompletion*100/219676338)+"% | "+str(partialCompletion*100/12204241)+"%")
                print(str(totalCompletion*100/219676338)+"% | "+str(partialCompletion*100/12204241)+"%")
        print(str(totalCompletion*100/219676338)+"%")
print("Completed reduction of solutions.")
print()
print("Starting saving of solutions in case files.")
saveCompletion=0
for case in casesDict:
        with open(solutionsSaveLocation+"case_"+case+".txt",'w') as caseFile:
                for solution in casesDict[case]:
                        caseFile.write(str(solution)+"\n")
                caseFile.write(str(len(casesDict[case]))+"|")
                if len(casesDict[case])==0:
                        caseFile.write(str(8)+"\n")
                else:
                        caseFile.write(str(len(casesDict[case][0]))+"\n")
        saveCompletion+=1
        print("----"+str(saveCompletion*100/24098)+"%")
        print("----"+str(saveCompletion*100/24098)+"%")
        print("----"+str(saveCompletion*100/24098)+"%")
print("Completed saving of solutions in case files.")
print()
input("All done!")
print()
print("Starting saving of casesDict in casesDict file.")
with open(r"C:\Users\ggtrn\Desktop\Cross Cases and Solutions\Files\crossCasesDict.txt",'w') as casesDictFile:
        casesDictFile.write(str(casesDict))
print("Completed saving of casesDict in casesDict file.")
