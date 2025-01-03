import decimal
import time
import math
from rich.console import Console
from rich.table import Table
decimal.setcontext(decimal.ExtendedContext)
decimal.getcontext().prec = 100

def smallNumberToWords(number):
    number = str(number)
    if len(number) == 1:
        number = "00" + number
    elif len(number) == 2:
        number = "0" + number
    unitTranslations = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    tenTranslations = {0: "zero", 10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    if (number[0] == "0") and (number[1] == "0") and (number[2] == "0"): # Example: 000
        wordForm = ""
    elif (number[0] == "0") and (number[1] == "0") and (number[2] != "0"): # Example: 001
        wordForm = unitTranslations[(int(number[2]))]
    elif (number[0] == "0") and (number[1] != "0") and (number[2] != "0"): # Example: 011
        wordForm = tenTranslations[(int(number[1]) * 10)] + " " + unitTranslations[(int(number[2]))]
    elif (number[0] != "0") and (number[1] != "0") and (number[2] != "0"): # Example: 111
        wordForm = unitTranslations[(int(number[0]))] + " " + "hundred and" + " " + tenTranslations[(int(number[1]) * 10)] + " " + unitTranslations[(int(number[2]))]
    elif (number[0] != "0") and (number[1] == "0") and (number[2] == "0"): # Example: 100
        wordForm = unitTranslations[(int(number[0]))] + " " + "hundred"
    elif (number[0] != "0") and (number[1] == "0") and (number[2] != "0"): # Example: 101
        wordForm = unitTranslations[(int(number[0]))] + " " + "hundred and" + " " + unitTranslations[(int(number[2]))]
    elif (number[0] == "0") and (number[1] != "0") and (number[2] == "0"): # Example: 010
        wordForm = tenTranslations[(int(number[1]) * 10)]
    elif (number[0] != "0") and (number[1] != "0") and (number[2] == "0"): # Example: 110
        wordForm = unitTranslations[(int(number[0]))] + " " + "hundred and" + " " + tenTranslations[(int(number[1]) * 10)]
    wordForm = wordForm.replace("ten one", "eleven")
    wordForm = wordForm.replace("ten two", "twelve")
    wordForm = wordForm.replace("ten three", "thirteen")
    wordForm = wordForm.replace("ten four", "fourteen")
    wordForm = wordForm.replace("ten five", "fifteen")
    wordForm = wordForm.replace("ten six", "sixteen")
    wordForm = wordForm.replace("ten seven", "seventeen")
    wordForm = wordForm.replace("ten eight", "eighteen")
    wordForm = wordForm.replace("ten nine", "nineteen")
    return(wordForm)

def splitNumber(number):
    number = [item for item in number]
    number.reverse()
    groups = []
    digit = 0
    # Split number into groups of 3
    for _ in number:
        try:
            groups.append([number[digit] + number[digit + 1] + number[digit + 2]])
        except IndexError:
            try:
                groups.append([number[digit] + number[digit + 1]])
            except IndexError:
                try:
                    groups.append([number[digit]])
                except IndexError:
                    pass
        digit = digit + 3
    # Reverse every digit in the group
    correctedGroups = []
    for group in groups:
        newGroup = []
        for _ in group:
            for digit in _:
                newGroup.append(digit)
        newGroup.reverse()
        newGroup = "".join(newGroup)
        correctedGroups.append(newGroup)
    # Reverse corrected groups
    correctedGroups.reverse()
    return(correctedGroups)


def bigNumberToWords(number):
    seperated = splitNumber(str(number))
    powerTranslations = {0: "", 3: "thousand", 6: "million", 9: "billion", 12: "trillion", 15: "quadrillion", 18: "quintillion", 21: "sextillion"}
    power = 1
    seperated.reverse()
    words = []
    # Add powers of thousand
    for group in seperated:
        zeros = len(str(power).replace("1", ""))
        powerName = powerTranslations[zeros]
        wordForm = smallNumberToWords(group) + " " + powerName
        if wordForm.strip() in powerTranslations.values():
            pass
        else:
            words.append(wordForm)
        power = power * 1000
    words.reverse()
    if " " in words:
        words.remove(" ")
    # Add correct use of "and" and commas
    correctWords = ""
    for item in words:
        if item == words[-1]:
            if len(words) == 1:
                correctWords = item
            else:
                correctWords = correctWords + " " + "and" + " " + item
        else:
            correctWords = correctWords + "," + " " + item
    if correctWords.startswith(", "):
        correctWords = correctWords.replace(", ", "", 1)
    correctWords = correctWords.strip()
    return(correctWords)

def benchmark():
    print(f"Okay, a bench mark will be ran for {bigNumberToWords(1000000)} calculations, totalling to {bigNumberToWords(14000000)} operations. Please wait.")
    piTotal = decimal.Decimal(3)
    x, y, z = decimal.Decimal(2), decimal.Decimal(3), decimal.Decimal(4)
    decimalFour = decimal.Decimal(4)
    startTime = time.time()
    for _ in range(1000000):
        addition = decimalFour / (x * y * z)
        x, y, z = x + decimal.Decimal(2), y + decimal.Decimal(2), z + decimal.Decimal(2)
        subtraction = decimalFour / (x * y * z)
        x, y, z = x + decimal.Decimal(2), y + decimal.Decimal(2), z + decimal.Decimal(2)
        piTotal = piTotal + decimal.Decimal(addition) - decimal.Decimal(subtraction)
    stopTime = time.time()
    elapsedTime = stopTime - startTime
    first100Digits = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    increment = 0
    while True:
        if str(piTotal)[increment] == first100Digits[increment]:
            increment = increment + 1
        else:
            break
    increment = increment / 1000000 * (smallRepetition * bigRepetition)
    print(f"{bigNumberToWords(1000000)} calculations, or {bigNumberToWords(14000000)} operations, took {bigNumberToWords((math.ceil(elapsedTime * 1000 * 1000 * 1000 * 1000 * 1000)))} femtoseconds.")
    print(f"It can be infered that {bigNumberToWords((smallRepetition * bigRepetition))} calculations, or {bigNumberToWords((smallRepetition * bigRepetition * 14))} operations will take:")
    femtosecondTime = math.ceil(decimal.Decimal(elapsedTime * 1000 * 1000 * 1000 * 1000 * 1000) / decimal.Decimal(14000000) * decimal.Decimal((smallRepetition * bigRepetition * 14)))
    seconds = math.ceil(femtosecondTime / 1000 / 1000 / 1000 / 1000 / 1000)

    table = Table(title="Benchmark Results")

    table.add_column("Unit", justify="right", style="cyan", no_wrap=True)
    table.add_column("Time", style="magenta", no_wrap=True)
    table.add_column("Digits Calculated", style="blue")

    table.add_row("Days", str(seconds / 3600 / 24), str(increment))
    table.add_row("Hours", str(seconds / 3600), str(increment))
    table.add_row("Minutes", str(seconds / 60), str(increment))
    table.add_row("Seconds", str(seconds), str(increment))
    table.add_row("Milliseconds", str(seconds * 1000), str(increment))
    table.add_row("Microseconds", str(seconds * 1000 * 1000), str(increment))
    table.add_row("Nanoseconds", str(seconds * 1000 * 1000 * 1000), str(increment))
    table.add_row("Picoseconds", str(seconds * 1000 * 1000 * 1000 * 1000), str(increment))
    table.add_row("Femtoseconds", str(femtosecondTime))

    console = Console()
    console.print(table)
    
    if "y" in input("Proceed?").casefold():
        pass
    else:
        exit()


def advancedMode():
    smallRepetition = int(input("Enter how many times to repeat: "))
    bigRepetition = int(input("Enter how many times to repeat repetition: "))
    print(f"Will repeat the {bigNumberToWords(smallRepetition)} calculations {bigNumberToWords(bigRepetition)} time(s). This will total to {bigNumberToWords((smallRepetition * bigRepetition))}.")
    print(f"In the program there are four multiplications, two divisions, seven additions, and one subtraction. This subtotals to fourteen operations.")
    print(f"This will total to {bigNumberToWords((smallRepetition * bigRepetition * 14))} operations. Would you like to run a benchmark?")
    if "y" in input("").casefold():
        benchmark()

    piTotal = decimal.Decimal(3)
    x, y, z = decimal.Decimal(2), decimal.Decimal(3), decimal.Decimal(4)
    decimalFour = decimal.Decimal(4)
    startTime = time.time()
    for _ in range(bigRepetition):
        for _ in range(smallRepetition):
            addition = decimalFour / (x * y * z)
            x, y, z = x + decimal.Decimal(2), y + decimal.Decimal(2), z + decimal.Decimal(2)
            subtraction = decimalFour / (x * y * z)
            x, y, z = x + decimal.Decimal(2), y + decimal.Decimal(2), z + decimal.Decimal(2)
            piTotal = piTotal + decimal.Decimal(addition) - decimal.Decimal(subtraction)
        print(piTotal)
    stopTime = time.time()
    print("Calculation finished!")
    print(piTotal)
    first100Digits = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    increment = 0
    while True:
        if str(piTotal)[increment] == first100Digits[increment]:
            increment = increment + 1
        else:
            break
    print(f"This calculator got {bigNumberToWords(increment)} digits correct.")
    print(f"Below is a table displaying results:")
    elapsedTime = stopTime - startTime
    femtosecondTime = math.ceil(decimal.Decimal(elapsedTime * 1000 * 1000 * 1000 * 1000 * 1000))
    seconds = math.ceil(femtosecondTime / 1000 / 1000 / 1000 / 1000 / 1000)

    table = Table(title="Calculation Results")

    table.add_column("Unit", justify="right", style="cyan", no_wrap=True)
    table.add_column("Time", style="magenta", no_wrap=True)
    table.add_column("Digits Calculated", style="blue")

    table.add_row("Days", str(seconds / 3600 / 24), str(increment))
    table.add_row("Hours", str(seconds / 3600), str(increment))
    table.add_row("Minutes", str(seconds / 60), str(increment))
    table.add_row("Seconds", str(seconds), str(increment))
    table.add_row("Milliseconds", str(seconds * 1000), str(increment))
    table.add_row("Microseconds", str(seconds * 1000 * 1000), str(increment))
    table.add_row("Nanoseconds", str(seconds * 1000 * 1000 * 1000), str(increment))
    table.add_row("Picoseconds", str(seconds * 1000 * 1000 * 1000 * 1000), str(increment))
    table.add_row("Femtoseconds", str(femtosecondTime))

    console = Console()
    console.print(table)

def simpleMode():
    table = Table(title="Options")

    table.add_column("Index")
    table.add_column("Digits Calculated", style="yellow", no_wrap=True)
    table.add_column("Calcultions Required", style="green", no_wrap=True)


    for index in range(10):
        digitsCalculated = index * 3
        calculationsRequired = digitsCalculated / 21 * 1000000
        table.add_row(str(index), str(digitsCalculated), str(calculationsRequired))

    selected = input("")

    console = Console()
    console.print(table)

simpleMode()

# Note: It seems that when increasing the amount of calculations by powers of one thousand, the digits correct increases by exactly three digits each time. For example, one million calculations
# yields 21 correct digits. One hundred thousand calculations yields 18 correct digits. Ten thousand calculations yields 15 correct digits. One thousand calculations yields 12 correct digits.