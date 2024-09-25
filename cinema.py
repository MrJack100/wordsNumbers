from termcolor import colored
import base64, nltk, os

class ASCIIArt:
    def __init__(self):
        self.cinema = "ICBfX19fIF8gICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAvIF9fXyhfKV8gX18gICBfX18gXyBfXyBfX18gICBfXyBfIAp8IHwgICB8IHwgJ18gXCAvIF8gXCAnXyBgIF8gXCAvIF9gIHwKfCB8X19ffCB8IHwgfCB8ICBfXy8gfCB8IHwgfCB8IChffCB8CiBcX19fX3xffF98IHxffFxfX198X3wgfF98IHxffFxfXyxffA=="

    def print(self, artwork: str) -> str:
        if artwork == "cinema":
            artwork = self.cinema
        decoded = base64.b64decode(artwork)
        return(decoded.decode(encoding="utf-8"))

def displayCurrentFilms(currentFilms: list[str]):
    increment = 0
    for film in currentFilms:
        print(f"{colored(increment, "cyan")}: {film}")
        increment = increment + 1
    userInput = input("")
    if userInput == 0 or userInput.isnumeric():
        return(int(userInput))
    elif userInput in currentFilms:
        return(currentFilms.index(userInput))
    else:
        editDistance = {}
        for film in currentFilms:
            editDistance.update({nltk.edit_distance(film, userInput): film})
        mostLikelyMatch = [value for value in editDistance.keys()]
        largestValue = 0
        for item in mostLikelyMatch:
            if item > largestValue:
                largestValue = item
        smallestValue = largestValue
        for item in mostLikelyMatch:
            if item < smallestValue:
                smallestValue = item
        print(colored(f"\"{userInput}\" couldn't be found.", "yellow"))
        confirmation = input(colored(f"Did you instead mean: \"{editDistance[smallestValue]}\"? ", "green"))
        if "y" in confirmation:
            return(currentFilms.index(editDistance[smallestValue]))
        else:
            return(None)

os.system("cls")
currentFilms = ["L4D2", "American Pie", "El Camino", "Titanic"]
ASCIIArt = ASCIIArt()
print(colored(ASCIIArt.print("cinema"), "red"))
print("Welcome to the cinema, please enter either the films name or the films ID number: ")
while True:
    selected = displayCurrentFilms(currentFilms)
    if selected == None:
        pass
    else:
        break
print(selected)