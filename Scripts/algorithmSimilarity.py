def generateMovesDict(affectedMoves, offset):
        movesDict={i:i for i in ["F","F'","F2","B","B'","B2","R","R'","R2","L","L'","L2","U","U'","U2","D","D'","D2"]}
        for cycle in affectedMoves:
                for i in cycle:
                        movesDict[i]=cycle[(cycle.index(i)+offset)%len(cycle)]
        return movesDict

rotatedMovesByX,rotatedMovesByXp,rotatedMovesByX2 = [generateMovesDict([["F","U","B","D"],["F'","U'","B'","D'"],["F2","U2","B2","D2"]],i) for i in [1,-1,2]]
rotatedMovesByY,rotatedMovesByYp,rotatedMovesByY2 = [generateMovesDict([["F","L","B","R"],["F'","L'","B'","R'"],["F2","L2","B2","R2"]],i) for i in [1,-1,2]]
rotatedMovesByZ,rotatedMovesByZp,rotatedMovesByZ2 = [generateMovesDict([["U","R","B","L"],["U'","R'","B'","L'"],["U2","R2","B2","L2"]],i) for i in [1,-1,2]]

mirroredMoves = generateMovesDict([["F","F'"],["U","U'"],["B","B'"],["D","D'"],["R","L'"],["R'","L"],["R2","L2"]],1)
reversedMoves = generateMovesDict([["F","F'"],["U","U'"],["B","B'"],["D","D'"],["R","R'"],["L","L'"]],1)


def rotateAlgorithmByX(algorithm):
        rotatedAlgorithm=[]
        for move in algorithm:
            rotatedAlgorithm.append(rotatedMovesByX[move])
        return rotatedAlgorithm
def rotateAlgorithmByY(algorithm):
        rotatedAlgorithm=[]
        for move in algorithm:
            rotatedAlgorithm.append(rotatedMovesByY[move])
        return rotatedAlgorithm
def rotateAlgorithmByYp(algorithm):
        rotatedAlgorithm=[]
        for move in algorithm:
            rotatedAlgorithm.append(rotatedMovesByYp[move])
        return rotatedAlgorithm

def mirrorAlgorithm(algorithm):
        mirroredAlgorithm=[]
        for move in algorithm:
            mirroredAlgorithm.append(mirroredMoves[move])
        return mirroredAlgorithm

def reverseAlgorithm(algorithm):
        reversedAlgorithm=[]
        for move in algorithm:
            reversedAlgorithm.append(reversedMoves[move])
        return reversedAlgorithm

def transformAlgorithm(algorithm,transformation):
        transformedAlgorithm=[]
        for move in algorithm:
            transformedAlgorithm.append(transformation[move])
        return transformedAlgorithm


def areSimilarAlgorithms(alg1,alg2):
        if (len(alg1)!=len(alg2)):
                return False
        
        tempAlg=alg2
        if (alg1==tempAlg):
                return True # These ae exactly the same, what are you doing?!?!?
        tempAlg=rotateAlgorithm(tempAlg)
        if (alg1==tempAlg):
                return True
        tempAlg=rotateAlgorithm(tempAlg)
        if (alg1==tempAlg):
                return True
        tempAlg=rotateAlgorithm(tempAlg)
        if (alg1==tempAlg):
                return True
        
        tempAlg=mirrorAlgorithm(alg2)
        if (alg1==tempAlg):
                return True
        tempAlg=rotateAlgorithm(tempAlg)
        if (alg1==tempAlg):
                return True
        tempAlg=rotateAlgorithm(tempAlg)
        if (alg1==tempAlg):
                return True
        tempAlg=rotateAlgorithm(tempAlg)
        if (alg1==tempAlg):
                return True
    
        return False

def similarAlgs(alg):
        listOfSimilarAlgs=[]

        tempAlg=alg
        listOfSimilarAlgs.append(tempAlg)
        tempAlg=rotateAlgorithm(tempAlg)
        listOfSimilarAlgs.append(tempAlg)
        tempAlg=rotateAlgorithm(tempAlg)
        listOfSimilarAlgs.append(tempAlg)
        tempAlg=rotateAlgorithm(tempAlg)
        listOfSimilarAlgs.append(tempAlg)

        tempAlg=mirrorAlgorithm(alg)
        listOfSimilarAlgs.append(tempAlg)
        tempAlg=rotateAlgorithm(tempAlg)
        listOfSimilarAlgs.append(tempAlg)
        tempAlg=rotateAlgorithm(tempAlg)
        listOfSimilarAlgs.append(tempAlg)
        tempAlg=rotateAlgorithm(tempAlg)
        listOfSimilarAlgs.append(tempAlg)

        return listOfSimilarAlgs

def similarAlgorithmIsAlreadyInList(alg,listOfUsedAlgs):
        for similarAlg in similarAlgs(alg):
            if similarAlg in listOfUsedAlgs:
                return True
        return False
