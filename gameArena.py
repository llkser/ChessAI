class ChessArena:
    def __init__(self):
        self.UnitList=[
            RookUnit(0,0,1),KnightUnit(1,0,1),BishopUnit(2,0,1),KingUnit(3,0,1),
            RookUnit(7,0,1),KnightUnit(6,0,1),BishopUnit(5,0,1),QueenUnit(4,0,1),
            PawnUnit(0,1,1),PawnUnit(1,1,1),PawnUnit(2,1,1),PawnUnit(3,1,1),
            PawnUnit(4,1,1),PawnUnit(5,1,1),PawnUnit(6,1,1),PawnUnit(7,1,1),
            RookUnit(0,7,2),KnightUnit(1,7,2),BishopUnit(2,7,2),KingUnit(3,7,2),
            RookUnit(7,7,2),KnightUnit(6,7,2),BishopUnit(5,7,2),QueenUnit(4,7,2),
            PawnUnit(0,6,2),PawnUnit(1,6,2),PawnUnit(2,6,2),PawnUnit(3,6,2),
            PawnUnit(4,6,2),PawnUnit(5,6,2),PawnUnit(6,6,2),PawnUnit(7,6,2)
        ]

    def moveUnit(self, x1, y1, x2, y2):
        for i in self.UnitList:
            if i.x==x2 and i.y==y2:
                del i
                break
        for i in self.UnitList:
            if i.x==x1 and i.y==y1:
                i.x=x2
                i.y=y2
                i.isMoved=1
                break

    def promotion(self, UnitID):
        pass

    def castling(self, KingID, RookID):
        pass
    
    def getGridInfo(self):
        Grid=[[],[],[],[],[],[],[],[]]
        for i in range(8):
            for j in range(8):
                Grid[i].append("00")
        for i in self.UnitList:
            Grid[i.y][i.x]=str(i.owner)+i.UnitID
        return Grid

    def printGrid(self):
        Grid=self.getGridInfo()
        GridStr=""
        for i in range(8):
            for j in range(8):
                GridStr+=Grid[7-i][j]+' '
            GridStr+="\n"
        print(GridStr)

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
        if x+1<8 and y+1<8 and (gridInfo[y+1][x+1]=="00" or gridInfo[y+1][x+1][0]!=str(self.owner)):
            acPosition.append([x+1,y+1])
        if x+1<8 and y+1<8 and (gridInfo[y+1][x+1]=="00" or gridInfo[y+1][x+1][0]!=str(self.owner)):
            acPosition.append([x+1,y+1])
        if x+1<8 and y-1>=0 and (gridInfo[y-1][x+1]=="00" or gridInfo[y-1][x+1][0]!=str(self.owner)):
            acPosition.append([x+1,y-1])
        if x+1<8 and y-1>=0 and (gridInfo[y-1][x+1]=="00" or gridInfo[y-1][x+1][0]!=str(self.owner)):
            acPosition.append([x+1,y-1])
        if x-1>=0 and y+1<8 and (gridInfo[y+1][x-1]=="00" or gridInfo[y+1][x-1][0]!=str(self.owner)):
            acPosition.append([x-1,y+1])
        if x-1>=0 and y+1<8 and (gridInfo[y+1][x-1]=="00" or gridInfo[y+1][x-1][0]!=str(self.owner)):
            acPosition.append([x-1,y+1])
        if x-1>=0 and y-1>=0 and (gridInfo[y-1][x-1]=="00" or gridInfo[y-1][x-1][0]!=str(self.owner)):
            acPosition.append([x-1,y-1])
        if x-1>=0 and y-1>=0 and (gridInfo[y-1][x-1]=="00" or gridInfo[y-1][x-1][0]!=str(self.owner)):
            acPosition.append([x-1,y-1])
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
        for i in range(0,x):
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
        for i in range(0,y):
            if gridInfo[i][x]=="00":
                acPosition.append([x,i])
            else:
                if gridInfo[i][x][0]!=str(self.owner):
                    acPosition.append([x,i])
                break
        for i in range(1,min(7-x,7-y)):
            if gridInfo[y+i][x+i]=="00":
                acPosition.append([x+i,y+i])
            else:
                if gridInfo[y+i][x+i][0]!=str(self.owner):
                    acPosition.append([x+i,y+i])
                break
        for i in range(1,min(7-x,y)):
            if gridInfo[y-i][x+i]=="00":
                acPosition.append([x+i,y-i])
            else:
                if gridInfo[y-i][x+i][0]!=str(self.owner):
                    acPosition.append([x+i,y-i])
                break
        for i in range(1,min(x,7-y)):
            if gridInfo[y+i][x-i]=="00":
                acPosition.append([x-i,y+i])
            else:
                if gridInfo[y+i][x-i][0]!=str(self.owner):
                    acPosition.append([x-i,y+i])
                break
        for i in range(1,min(x,y)):
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

        for i in range(1,min(7-x,7-y)):
            if gridInfo[y+i][x+i]=="00":
                acPosition.append([x+i,y+i])
            else:
                if gridInfo[y+i][x+i][0]!=str(self.owner):
                    acPosition.append([x+i,y+i])
                break
        for i in range(1,min(7-x,y)):
            if gridInfo[y-i][x+i]=="00":
                acPosition.append([x+i,y-i])
            else:
                if gridInfo[y-i][x+i][0]!=str(self.owner):
                    acPosition.append([x+i,y-i])
                break
        for i in range(1,min(x,7-y)):
            if gridInfo[y+i][x-i]=="00":
                acPosition.append([x-i,y+i])
            else:
                if gridInfo[y+i][x-i][0]!=str(self.owner):
                    acPosition.append([x-i,y+i])
                break
        for i in range(1,min(x,y)):
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
        for i in range(0,x):
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
        for i in range(0,y):
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

def main():
    game1=ChessArena()
    game1.printGrid()
    game1.moveUnit(0,1,0,2)
    game1.printGrid()
    for i in game1.UnitList:
        print(i.getMove(game1.getGridInfo()))

if '__main__' == __name__:
    main()
