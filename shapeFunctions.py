import math, inspect

def userInput(func): #creates a function that does what i need it to do and sends it off
    def wrapper_func(): #does what i need it to do
        arguments = inspect.signature(func).parameters
        userResponse = {}
        for item in arguments:
            userResponse.update({item: (int(input(f"Enter value for {item}: ")))})
        return(func(**userResponse))
    return(wrapper_func)

class RectangleFunctions:
    def __str__(self):
        return("Rectangle Functions")
    
    @userInput #sneakily calls another function
    def area(length, width):
        return(length * width)
    
    @userInput
    def perimeter(length, width):
        return((length * 2) + (width * 2))

class TriangleFunctions:
    def __str__(self):
        return("Triangle Functions")
    
    @userInput
    def area(height, width):
        return((height * width) / 2)
    
    @userInput
    def perimeter(hypo=0, opposite=0, adjacent=0):
        if hypo == 0:
            hypo = math.sqrt((opposite ^ 2) + (adjacent ^ 2))
        elif opposite == 0:
            opposite = math.sqrt((hypo ^ 2) - (adjacent ^ 2))
        elif adjacent == 0:
            adjacent = math.sqrt((hypo ^ 2) - (opposite ^ 2))
        return(hypo + opposite + adjacent)

class CircleFunctions:
    def __str__(self):
        return("Circle Functions")
    
    @userInput
    def area(radius):
        return((2 * math.pi * radius) ^ 2)
    
    @userInput
    def perimeter(radius):
        return(2 * math.pi * radius)
    
class Menu:
    def __init__(self):
        pass

    def start(self):
        selection = self.mainMenu()
        targetFunction = getattr(selection, self.subMenu(selection))
        print(f"Result: {targetFunction()}")
    
    def subMenu(self, selection):
        allFunctions = dir(selection)
        requiredFunctions = []
        for item in allFunctions:
            if item.startswith("__") and item.endswith("__"):
                pass
            else:
                requiredFunctions.append(item)
        increment = 0
        for item in requiredFunctions:
            increment = increment + 1
            print(f"{increment})\t{item.title()}")
        selection = input("Please enter number of target: ")
        try:
            selection = int(selection)
            if selection > 0 and selection <= len(requiredFunctions):
                selection = selection - 1
                return(requiredFunctions[selection])
            else:
                print(f"Must be within range provided: 1-{len(requiredFunctions)}")
                return(self.subMenu(selection))
        except ValueError:
            print("Must be a number")
            return(self.subMenu(selection))

    def mainMenu(self):
        functions = [RectangleFunctions, TriangleFunctions, CircleFunctions]
        increment = 0
        for item in functions:
            x = item()
            increment = increment + 1
            print(f"{increment})\t{x}")
        selection = input("Please enter number of target: ")
        try:
            selection = int(selection)
            if selection > 0 and selection <= len(functions):
                selection = selection - 1
                return(functions[selection])
            else:
                print(f"Must be within range provided: 1-{len(functions)}")
                return(self.mainMenu())
        except ValueError:
            print("Must be a number")
            return(self.mainMenu())

app = Menu()
app.start()