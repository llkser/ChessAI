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
    
    def getGridInfo(self):
        Grid=[[],[],[],[],[],[],[],[]]
        for i in range(8):
            for j in range(8):
                Grid[i].append(0)
        for i in range(len(self.UnitList)):
            Grid[self.UnitList[i].Position[1]][self.UnitList[i].Position[0]]=str(self.UnitList[i].owner)+self.UnitList[i].UnitID
        return Grid

    def printGrid(self):
        print(self.getGridInfo())

class Unit:
    def __init__(self, x, y, owner):
        self.Position=[x,y]
        self.owner=owner

class KingUnit(Unit):
    def __init__(self, x, y, owner):
        super(KingUnit,self).__init__(x,y,owner);
        self.UnitID='K'
        self.isMoved=0
    
    def getMove(self, gridInfo):
        pass

class QueenUnit(Unit):
    def __init__(self, x, y, owner):
        super(QueenUnit,self).__init__(x,y,owner);
        self.UnitID='Q'
    
    def getMove(self, gridInfo):
        pass

class BishopUnit(Unit):
    def __init__(self, x, y, owner):
        super(BishopUnit,self).__init__(x,y,owner);
        self.UnitID='B'
    
    def getMove(self, gridInfo):
        pass

class KnightUnit(Unit):
    def __init__(self, x, y, owner):
        super(KnightUnit,self).__init__(x,y,owner);
        self.UnitID='N'
    
    def getMove(self, gridInfo):
        pass

class RookUnit(Unit):
    def __init__(self, x, y, owner):
        super(RookUnit,self).__init__(x,y,owner);
        self.UnitID='R'
        self.isMoved=0
    
    def getMove(self, gridInfo):
        pass

class PawnUnit(Unit):
    def __init__(self, x, y, owner):
        super(PawnUnit,self).__init__(x,y,owner);
        self.UnitID='P'
        self.isMoved=0;
    
    def getMove(self, gridInfo):
        pass

def main():
    ChessArena().printGrid()

if '__main__' == __name__:
    main()
