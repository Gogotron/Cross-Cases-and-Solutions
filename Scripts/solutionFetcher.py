from ast import literal_eval as litEval

from caseSimilarity import similarCases, caseDifference
from cubeScrambling import applyMoves as applyScramble, applyMove, x,xp,x2,z,zp
from algorithmSimilarity import (
        mirrorAlgorithm,reverseAlgorithm,
        
        transformAlgorithm,
        rotatedMovesByX,rotatedMovesByXp,rotatedMovesByX2,
        rotatedMovesByZ,rotatedMovesByZp,rotatedMovesByZ2
)

transformationToFunction = lambda transformation: (lambda x:transformAlgorithm(x,transformation))

crossCasesLocation=r"C:\Users\ggtrn\Desktop\Cross Cases and Solutions\Files"+"\\"
solutionsSaveLocation=r"C:\Users\ggtrn\Desktop\Cross Cases and Solutions\Files\Solution Files"+"\\"

with open(crossCasesLocation+"crossCases.txt",'r') as casesFile:
        crossCasesUsed = [line.strip("\n") for line in casesFile]

def findSimilarCrossCaseUsed(case):
        crossCasesUsedAsFilesNames = list(filter(lambda x: x in crossCasesUsed,similarCases(case)))        # Intersection between similar cases and file names.
        if len(crossCasesUsedAsFilesNames)==1:
                return crossCasesUsedAsFilesNames[0]    # Normally only one cross case exists that's used as a file name.
        else:
                # This shouldn't be possible.
                print("Multiple possible files found.")

def solutionRetriver(case):     # This function given 1 case takes into account the 1 cross case corresponding to it.
        crossCaseUsed = findSimilarCrossCaseUsed(case)
        solutionsFileName = "case_"+crossCaseUsed+".txt"   # Many cases correspond to a single file, case and file names don't always match.
        solutionsFile = open(solutionsSaveLocation+solutionsFileName, 'r')
        
        lines = solutionsFile.readlines()
        numberOfSolutions = len(lines)-1        # The last line isn't a solution.
        
        if numberOfSolutions>0:
                scrambles = list(map(lambda x: litEval(x.strip("\n")), lines[:-1]))     # Again, the last line isn't a solution.
                rawSolutions = list(map(reverseAlgorithm,scrambles))
                transformation = caseDifference(crossCaseUsed,case)     # Find out how to convert the solutions for the general case to the solutions for the requested case.
                if transformation>=4:
                        rawSolutions = list(map(mirrorAlgorithm,rawSolutions))
                for i in range(transformation%4):
                        rawSolutions = list(map(transformationToFunction(rotatedMovesByX),rawSolutions))
                solutions = rawSolutions
                return solutions
        else:
                print("No solutions found.")
                return []       # No solutions found.

def reduceSolutions(solutionsA,solutionsB):
        if len(solutionsA)==0 or len(solutionsB)==0:
                return solutionsA+solutionsB
        if len(solutionsA[0])==len(solutionsB[0]):
                return solutionsA+solutionsB
        if len(solutionsA[0])<len(solutionsB[0]):
                return solutionsA
        if len(solutionsB[0])<len(solutionsA[0]):
                return solutionsB

def otherFunctionWithOtherName(scramble,mode="w"):      # This function given 1 scramble takes into account the 6 cross cases corresponding to it. Mode can be "w","wy","n".
        scrambledCube = applyScramble(scramble,"abcdefghijklmnopqrtsuvwx")      # Calling it a cube when it's really just edge stickers.
        solutions=[]
        if mode in ["w","wy","n"]:
                whiteCase = scrambledCube[:4]
                whiteSolutions = solutionRetriver(whiteCase)
                solutions = reduceSolutions(solutions,whiteSolutions)
        if mode in ["wy","n"]:
                yellowCase = applyMove(x2,scrambledCube[-4:])
                
                yellowSolutions = list(map(transformationToFunction(rotatedMovesByX2),solutionRetriver(yellowCase)))
                solutions = reduceSolutions(solutions,yellowSolutions)
        if mode=="n":
                greenCase = applyMove(x,scrambledCube[4:8])
                greenSolutions = list(map(transformationToFunction(rotatedMovesByXp),solutionRetriver(greenCase)))
                solutions = reduceSolutions(solutions,greenSolutions)
                
                redCase = applyMove(zp,scrambledCube[8:12])
                redSolutions = list(map(transformationToFunction(rotatedMovesByZ),solutionRetriver(redCase)))
                solutions = reduceSolutions(solutions,redSolutions)
                
                blueCase = applyMove(xp,scrambledCube[12:16])
                blueSolutions = list(map(transformationToFunction(rotatedMovesByX),solutionRetriver(blueCase)))
                solutions = reduceSolutions(solutions,blueSolutions)
                
                orangeCase = applyMove(z,scrambledCube[16:20])
                orangeSolutions = list(map(transformationToFunction(rotatedMovesByZp),solutionRetriver(orangeCase)))
                solutions = reduceSolutions(solutions,orangeSolutions)
        return list(set(solutions))
