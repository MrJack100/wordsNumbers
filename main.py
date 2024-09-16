import math

class RectangleFunctions:
    def area(length, width):
        return(length * width)
    
    def perimeter(length, width):
        return((length * 2) + (width * 2))

class TriangleFunctions:
    def area(height, width):
        return((height * width) / 2)
    
    def perimeter(hypo=0, opposite=0, adjacent=0):
        if hypo == 0:
            hypo = math.sqrt((opposite ^ 2) + (adjacent ^ 2))
        elif opposite == 0:
            opposite = math.sqrt((hypo ^ 2) - (adjacent ^ 2))
        elif adjacent == 0:
            adjacent = math.sqrt((hypo ^ 2) - (opposite ^ 2))
        return(hypo + opposite + adjacent)

class CircleFunctions:
    def area(radius):
        return((2 * math.pi * radius) ^ 2)
    
    def perimeter(radius):
        return(2 * math.pi * radius)
    
class Menu:
    def __init__(self):
        pass

    def mainMenu():
        functions = [RectangleFunctions, TriangleFunctions, CircleFunctions]