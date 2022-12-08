import os

class PuzzleBase:

    #def __init__(self):
    #    print("BaseClass")

    def ReadInputLines(self, f):              
    
        filename = self.GetFileName(f)

        file1 = open(filename, 'r')
        Lines = file1.readlines()
        file1.close()

        return Lines

    def GetFileName(self, f):
        path = os.path.dirname(os.path.abspath(f))
        fileName = "input.txt"

        return path + "\\" + fileName