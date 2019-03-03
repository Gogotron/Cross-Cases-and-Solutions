rotatedCases={
        'a':'b',
        'b':'c',
        'c':'d',
        'd':'a',
        'e':'i',
        'f':'j',
        'g':'k',
        'h':'l',
        'i':'m',
        'j':'n',
        'k':'o',
        'l':'p',
        'm':'q',
        'n':'r',
        'o':'s',
        'p':'t',
        'q':'e',
        'r':'f',
        's':'g',
        't':'h',
        'u':'x',
        'v':'w',
        'w':'v',
        'x':'u'
        }

mirroredCases={
        'a':'a',
        'b':'d',
        'c':'c',
        'd':'b',
        'e':'e',
        'f':'h',
        'g':'g',
        'h':'f',
        'i':'q',
        'j':'t',
        'k':'s',
        'l':'r',
        'm':'m',
        'n':'p',
        'o':'o',
        'p':'n',
        'q':'i',
        'r':'l',
        's':'k',
        't':'j',
        'u':'u',
        'v':'x',
        'w':'w',
        'x':'v'
        }

flippedCases={
        'a':'m',
        'b':'i',
        'c':'e',
        'd':'q',
        'e':'c',
        'f':'l',
        'g':'u',
        'h':'r',
        'i':'b',
        'j':'p',
        'k':'v',
        'l':'f',
        'm':'a',
        'n':'t',
        'o':'w',
        'p':'j',
        'q':'d',
        'r':'h',
        's':'x',
        't':'n',
        'u':'g',
        'v':'k',
        'w':'o',
        'x':'s'
        }

from cubeScrambling import y
def rotateCase(case):
        rotatedCase=""
        for pos in case:
                rotatedCase+=y[pos]
        rotatedCase=rotatedCase[-1]+rotatedCase[:-1]
        return rotatedCase

def mirrorCase(case):
        mirroredCase=""
        for pos in case:
                mirroredCase+=mirroredCases[pos]
        mirroredCase=list(mirroredCase)
        mirroredCase[1],mirroredCase[3]=mirroredCase[3],mirroredCase[1]
        mirroredCase="".join(mirroredCase)
        return mirroredCase


def areSimilarCases(caseA, caseB):
        tempCase=caseB
        if (caseA==tempCase):
                return True # These are exactly the same, what are you doing?!?!?
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return True
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return True
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return True
        
        tempCase=mirrorCase(caseB)
        if (caseA==tempCase):
                return True
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return True
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return True
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return True
        
        return False

def similarCases(case):
        listOfSimilarCases=[]

        tempCase=case
        listOfSimilarCases.append(tempCase)
        tempCase=rotateCase(tempCase)
        listOfSimilarCases.append(tempCase)
        tempCase=rotateCase(tempCase)
        listOfSimilarCases.append(tempCase)
        tempCase=rotateCase(tempCase)
        listOfSimilarCases.append(tempCase)

        tempCase=mirrorCase(case)
        listOfSimilarCases.append(tempCase)
        tempCase=rotateCase(tempCase)
        listOfSimilarCases.append(tempCase)
        tempCase=rotateCase(tempCase)
        listOfSimilarCases.append(tempCase)
        tempCase=rotateCase(tempCase)
        listOfSimilarCases.append(tempCase)

        return list(set(listOfSimilarCases))

def similarCaseIsAlreadyInList(case,listOfUsedCases):
        for similarCase in similarCases(case):
                if similarCase in listOfUsedCases:
                        return True
        return False


def caseDifference(caseA, caseB):      # This is to find how to go from one case to another.
        tempCase=caseB
        if (caseA==tempCase):
                return 0
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return 1
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return 2
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return 3
        
        tempCase=mirrorCase(caseB)
        if (caseA==tempCase):
                return 4
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return 5
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return 6
        tempCase=rotateCase(tempCase)
        if (caseA==tempCase):
                return 7

        return -1       # This should never have to be used.




def addToCases(case):
        if not similarCaseIsAlreadyInList(case, cases):
                cases.append(case)
                casesFile.write(case+"\n")

if __name__=="__main__":
        casesFile = open("crossCases.txt",'w')
        positions = 'abcdefghijklmnopqrstuvwx'
        cases=[]
        casesChecked=0
        availablePositionsForA=positions
        for posA in positions:
                availablePositionsForB=availablePositionsForA[:availablePositionsForA.index(posA)]+availablePositionsForA[availablePositionsForA.index(posA)+1:]
                availablePositionsForB=availablePositionsForB[:availablePositionsForB.index(flippedCases[posA])]+availablePositionsForB[availablePositionsForB.index(flippedCases[posA])+1:]
                for posB in availablePositionsForB:
                        availablePositionsForC=availablePositionsForB[:availablePositionsForB.index(posB)]+availablePositionsForB[availablePositionsForB.index(posB)+1:]
                        availablePositionsForC=availablePositionsForC[:availablePositionsForC.index(flippedCases[posB])]+availablePositionsForC[availablePositionsForC.index(flippedCases[posB])+1:]
                        for posC in availablePositionsForC:
                                availablePositionsForD=availablePositionsForC[:availablePositionsForC.index(posC)]+availablePositionsForC[availablePositionsForC.index(posC)+1:]
                                availablePositionsForD=availablePositionsForD[:availablePositionsForD.index(flippedCases[posC])]+availablePositionsForD[availablePositionsForD.index(flippedCases[posC])+1:]
                                for posD in availablePositionsForD:
                                        addToCases(posA+posB+posC+posD)
                                        casesChecked+=1
                        print(str(100*casesChecked/190080)+"% | "+str(len(cases))+"/"+str(casesChecked))
        print("Reduced from 190,080 cases to "+str(len(cases))+" cases.")
    
