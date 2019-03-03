def generateMovesDict(affectedPositions, offset):
        movesDict={i:i for i in "abcdefghijklmnopqrtsuvwx"}
        for cycle in affectedPositions:
                for i in cycle:
                        movesDict[i]=cycle[(cycle.index(i)+offset)%len(cycle)]
        return movesDict

F,Fp,F2=[generateMovesDict(['efgh','clur'],i) for i in [1,-1,2]]
U,Up,U2=[generateMovesDict(['abcd','eqmi'],i) for i in [1,-1,2]]
R,Rp,R2=[generateMovesDict(['ijkl','bpvf'],i) for i in [1,-1,2]]
L,Lp,L2=[generateMovesDict(['qrst','dhxn'],i) for i in [1,-1,2]]
D,Dp,D2=[generateMovesDict(['uvwx','gkos'],i) for i in [1,-1,2]]
B,Bp,B2=[generateMovesDict(['mnop','atwj'],i) for i in [1,-1,2]]

x,xp,x2=[generateMovesDict(['ijkl','qtsr','bpvf','nxhd','aoue','cmwg'],i) for i in (1,-1,2)]
y,yp,y2=[generateMovesDict(['abcd','uxwv','eqmi','gsok','frnj','htpl'],i) for i in (1,-1,2)]
z,zp,z2=[generateMovesDict(['efgh','mpon','clur','ajwt','bkxq','divs'],i) for i in (1,-1,2)]

moveDicts = {"F":F,"F'":Fp,"F2":F2,"B":B,"B'":Bp,"B2":B2,"U":U,"U'":Up,"U2":U2,"D":D,"D'":Dp,"D2":D2,"R":R,"R'":Rp,"R2":R2,"L":L,"L'":Lp,"L2":L2}

def applyMove(move, piecePositions):
        moveTransformationDict = moveDicts[move]
        newPiecePositions=""
        for piecePosition in piecePositions:
                newPiecePositions+=moveTransformationDict[piecePosition]
        return newPiecePositions

def applyMoves(moves,piecePositions="abcd"):
        newPiecePositions = piecePositions
        for move in moves:
                newPiecePositions = applyMove(move,newPiecePositions)
        return newPiecePositions
