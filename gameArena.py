import copy
class ChessArena:
    def __init__(self):
        self.UnitList=[
            RookUnit(0,0,1),KnightUnit(1,0,1),BishopUnit(2,0,1),QueenUnit(3,0,1),
            RookUnit(7,0,1),KnightUnit(6,0,1),BishopUnit(5,0,1),KingUnit(4,0,1),
            PawnUnit(0,1,1),PawnUnit(1,1,1),PawnUnit(2,1,1),PawnUnit(3,1,1),
            PawnUnit(4,1,1),PawnUnit(5,1,1),PawnUnit(6,1,1),PawnUnit(7,1,1),
            RookUnit(0,7,2),KnightUnit(1,7,2),BishopUnit(2,7,2),QueenUnit(3,7,2),
            RookUnit(7,7,2),KnightUnit(6,7,2),BishopUnit(5,7,2),KingUnit(4,7,2),
            PawnUnit(0,6,2),PawnUnit(1,6,2),PawnUnit(2,6,2),PawnUnit(3,6,2),
            PawnUnit(4,6,2),PawnUnit(5,6,2),PawnUnit(6,6,2),PawnUnit(7,6,2)
        ]
        self.UnitList_backup=[]
        self.canBack=False

    def moveUnit(self, x1, y1, x2, y2):
        self.UnitList_backup=copy.deepcopy(self.UnitList)
        self.canBack=True

        removedUnitID=-1
        for i in self.UnitList:
            if i.x==x2 and i.y==y2:
                removedUnitID=self.UnitList.index(i)
                break
        if removedUnitID>-1:
            del self.UnitList[removedUnitID]

        for i in self.UnitList:
            if i.x==x1 and i.y==y1:
                i.x=x2
                i.y=y2
                i.isMoved=1
                if i.UnitID=='P':
                    if i.owner==1:
                        bottom=7
                    else:
                        bottom=0
                    if i.y==bottom:
                        self.promotion(self.UnitList.index(i))
                elif i.UnitID=='K' and abs(x1-x2)==2:
                    if i.owner==1:
                        bottom=0
                    else:
                        bottom=7
                    if x2==2:
                        for j in self.UnitList:
                            if j.x==0 and j.y==bottom:
                                j.x=3
                                j.isMoved=1
                                break
                    else:
                        for j in self.UnitList:
                            if j.x==7 and j.y==bottom:
                                j.x=5
                                j.isMoved=1
                                break
                break

    def backLastMove(self):
        self.UnitList.clear()
        self.UnitList=copy.deepcopy(self.UnitList_backup)
        self.canBack=False

    def getGridInfo(self):
        Grid=[[],[],[],[],[],[],[],[]]
        for i in range(8):
            for j in range(8):
                Grid[i].append("00")
        for i in self.UnitList:
            Grid[i.y][i.x]=str(i.owner)+i.UnitID+str(i.isMoved)
        return Grid

    def printGrid(self):
        Grid=self.getGridInfo()
        GridStr=""
        for i in range(8):
            for j in range(8):
                GridStr+=Grid[7-i][j]+' '
                if Grid[7-i][j]=="00":
                    GridStr+=' '
            GridStr+="\n"
        print(GridStr)

    def promotion(self, UnitID):
        self.UnitList.append(QueenUnit(self.UnitList[UnitID].x,self.UnitList[UnitID].y,self.UnitList[UnitID].owner))
        del self.UnitList[UnitID]

    def isAttacked(self, x, y, player):
        for i in self.UnitList:
            if i.owner!=player and [x,y] in i.getMove(self.getGridInfo()):
                return True
        return False

    def checkMove(self, x1, y1, x2, y2):
        flag=True
        for i in self.UnitList:
            if i.x==x1 and i.y==y1:
                if i.UnitID=='K' and abs(x1-x2)==2:
                    i.x=x2
                    if self.isAttacked(i.x,i.y,i.owner):
                        flag=False
                    i.x=(x1+x2)//2
                    if self.isAttacked(i.x,i.y,i.owner):
                        flag=False
                    i.x=x1
                    if self.isAttacked(i.x,i.y,i.owner):
                        flag=False
                else:
                    UnitList_backup=[]
                    removedUnitID=-1
                    for j in self.UnitList:
                        if j.x==x2 and j.y==y2:
                            removedUnitID=self.UnitList.index(j)
                            UnitList_backup=copy.deepcopy(self.UnitList)
                            break
                    if removedUnitID>-1:
                        del self.UnitList[removedUnitID]
                    i.x=x2
                    i.y=y2
                    for j in self.UnitList:
                        if j.UnitID=='K' and j.owner==i.owner:
                            if self.isAttacked(j.x,j.y,j.owner):
                                flag=False
                                break
                    if UnitList_backup:
                        self.UnitList.clear()
                        self.UnitList=copy.deepcopy(UnitList_backup)
                    else:
                        i.x=x1
                        i.y=y1
                break
        return flag

    def getTotalMove(self, player):
        totalMove=[]
        for i in range(len(self.UnitList)):
            if self.UnitList[i].owner==player:
                for j in self.UnitList[i].getMove(self.getGridInfo()):
                    if self.checkMove(self.UnitList[i].x,self.UnitList[i].y,j[0],j[1]):
                        totalMove.append([[self.UnitList[i].x,self.UnitList[i].y],j])
        return totalMove

    def getAIMove(self):
        pass

    def alphabetaSearch(self, player):
        pass

class Unit:
    def __init__(self, x, y, owner):
        self.x=x
        self.y=y
        self.owner=owner
        self.isMoved=0

class KingUnit(Unit):
    def __init__(self, x, y, owner):
        super(KingUnit,self).__init__(x,y,owner);
        self.UnitID='K'
    
    def getMove(self, gridInfo):
        acPosition=[]
        x=self.x
        y=self.y
        if self.isMoved==0:
            if gridInfo[y][0][1]=='R' and gridInfo[y][0][2]=='0' and gridInfo[y][1]=="00" and gridInfo[y][2]=="00" and gridInfo[y][3]=="00":
                acPosition.append([x-2,y])
            if gridInfo[y][7][1]=='R' and gridInfo[y][0][2]=='0' and gridInfo[y][5]=="00" and gridInfo[y][6]=="00":
                acPosition.append([x+2,y])
        if x+1<8 and y+1<8 and (gridInfo[y+1][x+1]=="00" or gridInfo[y+1][x+1][0]!=str(self.owner)):
            acPosition.append([x+1,y+1])
        if x+1<8 and y-1>=0 and (gridInfo[y-1][x+1]=="00" or gridInfo[y-1][x+1][0]!=str(self.owner)):
            acPosition.append([x+1,y-1])
        if x-1>=0 and y+1<8 and (gridInfo[y+1][x-1]=="00" or gridInfo[y+1][x-1][0]!=str(self.owner)):
            acPosition.append([x-1,y+1])
        if x-1>=0 and y-1>=0 and (gridInfo[y-1][x-1]=="00" or gridInfo[y-1][x-1][0]!=str(self.owner)):
            acPosition.append([x-1,y-1])
        if y+1<8 and (gridInfo[y+1][x]=="00" or gridInfo[y+1][x][0]!=str(self.owner)):
            acPosition.append([x,y+1])
        if y-1>=0 and (gridInfo[y-1][x]=="00" or gridInfo[y-1][x][0]!=str(self.owner)):
            acPosition.append([x,y-1])
        if x+1<8 and (gridInfo[y][x+1]=="00" or gridInfo[y][x+1][0]!=str(self.owner)):
            acPosition.append([x+1,y])
        if x-1>=0 and (gridInfo[y][x-1]=="00" or gridInfo[y][x-1][0]!=str(self.owner)):
            acPosition.append([x-1,y])
        return acPosition

class QueenUnit(Unit):
    def __init__(self, x, y, owner):
        super(QueenUnit,self).__init__(x,y,owner);
        self.UnitID='Q'
    
    def getMove(self, gridInfo):
        acPosition=[]
        x=self.x
        y=self.y

        for i in range(x+1,8):
            if gridInfo[y][i]=="00":
                acPosition.append([i,y])
            else:
                if gridInfo[y][i][0]!=str(self.owner):
                    acPosition.append([i,y])
                break
        for i in reversed(range(0,x)):
            if gridInfo[y][i]=="00":
                acPosition.append([i,y])
            else:
                if gridInfo[y][i][0]!=str(self.owner):
                    acPosition.append([i,y])
                break
        for i in range(y+1,8):
            if gridInfo[i][x]=="00":
                acPosition.append([x,i])
            else:
                if gridInfo[i][x][0]!=str(self.owner):
                    acPosition.append([x,i])
                break
        for i in reversed(range(0,y)):
            if gridInfo[i][x]=="00":
                acPosition.append([x,i])
            else:
                if gridInfo[i][x][0]!=str(self.owner):
                    acPosition.append([x,i])
                break
        for i in range(1,min(7-x,7-y)+1):
            if gridInfo[y+i][x+i]=="00":
                acPosition.append([x+i,y+i])
            else:
                if gridInfo[y+i][x+i][0]!=str(self.owner):
                    acPosition.append([x+i,y+i])
                break
        for i in range(1,min(7-x,y)+1):
            if gridInfo[y-i][x+i]=="00":
                acPosition.append([x+i,y-i])
            else:
                if gridInfo[y-i][x+i][0]!=str(self.owner):
                    acPosition.append([x+i,y-i])
                break
        for i in range(1,min(x,7-y)+1):
            if gridInfo[y+i][x-i]=="00":
                acPosition.append([x-i,y+i])
            else:
                if gridInfo[y+i][x-i][0]!=str(self.owner):
                    acPosition.append([x-i,y+i])
                break
        for i in range(1,min(x,y)+1):
            if gridInfo[y-i][x-i]=="00":
                acPosition.append([x-i,y-i])
            else:
                if gridInfo[y-i][x-i][0]!=str(self.owner):
                    acPosition.append([x-i,y-i])
                break
        return acPosition

class BishopUnit(Unit):
    def __init__(self, x, y, owner):
        super(BishopUnit,self).__init__(x,y,owner);
        self.UnitID='B'
    
    def getMove(self, gridInfo):
        acPosition=[]
        x=self.x
        y=self.y

        for i in range(1,min(7-x,7-y)+1):
            if gridInfo[y+i][x+i]=="00":
                acPosition.append([x+i,y+i])
            else:
                if gridInfo[y+i][x+i][0]!=str(self.owner):
                    acPosition.append([x+i,y+i])
                break
        for i in range(1,min(7-x,y)+1):
            if gridInfo[y-i][x+i]=="00":
                acPosition.append([x+i,y-i])
            else:
                if gridInfo[y-i][x+i][0]!=str(self.owner):
                    acPosition.append([x+i,y-i])
                break
        for i in range(1,min(x,7-y)+1):
            if gridInfo[y+i][x-i]=="00":
                acPosition.append([x-i,y+i])
            else:
                if gridInfo[y+i][x-i][0]!=str(self.owner):
                    acPosition.append([x-i,y+i])
                break
        for i in range(1,min(x,y)+1):
            if gridInfo[y-i][x-i]=="00":
                acPosition.append([x-i,y-i])
            else:
                if gridInfo[y-i][x-i][0]!=str(self.owner):
                    acPosition.append([x-i,y-i])
                break
        return acPosition

class KnightUnit(Unit):
    def __init__(self, x, y, owner):
        super(KnightUnit,self).__init__(x,y,owner);
        self.UnitID='N'
    
    def getMove(self, gridInfo):
        acPosition=[]
        x=self.x
        y=self.y
        if x+2<8 and y+1<8 and (gridInfo[y+1][x+2]=="00" or gridInfo[y+1][x+2][0]!=str(self.owner)):
            acPosition.append([x+2,y+1])
        if x+1<8 and y+2<8 and (gridInfo[y+2][x+1]=="00" or gridInfo[y+2][x+1][0]!=str(self.owner)):
            acPosition.append([x+1,y+2])
        if x+2<8 and y-1>=0 and (gridInfo[y-1][x+2]=="00" or gridInfo[y-1][x+2][0]!=str(self.owner)):
            acPosition.append([x+2,y-1])
        if x+1<8 and y-2>=0 and (gridInfo[y-2][x+1]=="00" or gridInfo[y-2][x+1][0]!=str(self.owner)):
            acPosition.append([x+1,y-2])
        if x-2>=0 and y+1<8 and (gridInfo[y+1][x-2]=="00" or gridInfo[y+1][x-2][0]!=str(self.owner)):
            acPosition.append([x-2,y+1])
        if x-1>=0 and y+2<8 and (gridInfo[y+2][x-1]=="00" or gridInfo[y+2][x-1][0]!=str(self.owner)):
            acPosition.append([x-1,y+2])
        if x-2>=0 and y-1>=0 and (gridInfo[y-1][x-2]=="00" or gridInfo[y-1][x-2][0]!=str(self.owner)):
            acPosition.append([x-2,y-1])
        if x-1>=0 and y-2>=0 and (gridInfo[y-2][x-1]=="00" or gridInfo[y-2][x-1][0]!=str(self.owner)):
            acPosition.append([x-1,y-2])
        return acPosition

class RookUnit(Unit):
    def __init__(self, x, y, owner):
        super(RookUnit,self).__init__(x,y,owner);
        self.UnitID='R'
    
    def getMove(self, gridInfo):
        acPosition=[]
        x=self.x
        y=self.y

        for i in range(x+1,8):
            if gridInfo[y][i]=="00":
                acPosition.append([i,y])
            else:
                if gridInfo[y][i][0]!=str(self.owner):
                    acPosition.append([i,y])
                break
        for i in reversed(range(0,x)):
            if gridInfo[y][i]=="00":
                acPosition.append([i,y])
            else:
                if gridInfo[y][i][0]!=str(self.owner):
                    acPosition.append([i,y])
                break
        for i in range(y+1,8):
            if gridInfo[i][x]=="00":
                acPosition.append([x,i])
            else:
                if gridInfo[i][x][0]!=str(self.owner):
                    acPosition.append([x,i])
                break
        for i in reversed(range(0,y)):
            if gridInfo[i][x]=="00":
                acPosition.append([x,i])
            else:
                if gridInfo[i][x][0]!=str(self.owner):
                    acPosition.append([x,i])
                break
        return acPosition

class PawnUnit(Unit):
    def __init__(self, x, y, owner):
        super(PawnUnit,self).__init__(x,y,owner);
        self.UnitID='P'
    
    def getMove(self, gridInfo):
        acPosition=[]
        x=self.x
        y=self.y
        if self.owner==1:
            direction=1
        else:
            direction=-1

        if 0<=y+direction<8:
            if gridInfo[y+direction][x]=="00":
                acPosition.append([x,y+direction])
                if self.isMoved==0 and gridInfo[y+2*direction][x]=="00":
                    acPosition.append([x,y+2*direction])
            if x+1<8:
                if gridInfo[y+direction][x+1]!="00" and gridInfo[y+direction][x+1][0]!=str(self.owner):
                    acPosition.append([x+1,y+direction])
            if x-1>=0:
                if gridInfo[y+direction][x-1]!="00" and gridInfo[y+direction][x-1][0]!=str(self.owner):
                    acPosition.append([x-1,y+direction])
        return acPosition

def ArenaTest():
    game1=ChessArena()
    game1.printGrid()
    game1.moveUnit(5,0,5,4)
    game1.moveUnit(6,0,6,4)
    game1.moveUnit(3,7,5,1)
    game1.printGrid()
    
    for i in game1.UnitList:
        if i.owner==1:
            print([i.x,i.y],i.getMove(game1.getGridInfo()))
    print(game1.getTotalMove(1))
    game1.printGrid()

if '__main__' == __name__:
    ArenaTest()
