import PuzzleBase

class Day01(PuzzleBase.PuzzleBase):
    inputLines = []

    def __init__(self):        
        self.inputLines = self.ReadInputLines(__file__)
       

    def Puzzle01(self):
        print("puzzle01 start")
        
        
        i = 0
        counter = 0

        while i+1 < len(self.inputLines):

            if(int(self.inputLines[i]) < int (self.inputLines[i+1] )):              
                counter+=1
            i += 1        

        return "Puzzle Part 1 solution is " + str(counter)

    def Puzzle02(self):
        print("puzzle02 start")

        return "Puzzle Part 2 solution is"
