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

        counter = 0
        i = 0
        last =-1;

        while i+3 <= len(self.inputLines):
            
            current = self.GetCurrent(i)
            #next = self.GetNext(i)
            
            if(last>0):
                
                if(last < current):              
                    counter+=1
                    last = current
                    print(str(i) + str(current) + "(increased)")
                else:
                    print(str(i) + str(current) + "(decreased / no change)")
            else:
                print(str(i) + str(current) + "(N/A - no previous sum)")
                last = current

            
            i += 1 

        return "Puzzle Part 2 solution is "+ str(counter)

    def GetCurrent(self, i):

        a = int(self.inputLines[i])
        b = int(self.inputLines[i+1])
        c = int(self.inputLines[i+2])
        # print("Current =")
        # print(a)
        #print(b)
        # print(c)
        return a+b+c
