from termcolor import colored
asciiText = {"jurassic world system": '''

     _                         _       __        __         _     _ 
    | |_   _ _ __ __ _ ___ ___(_) ___  \\ \\      / /__  _ __| | __| |
 _  | | | | | '__/ _` / __/ __| |/ __|  \\ \\ /\\ / / _ \\| '__| |/ _` |
| |_| | |_| | | | (_| \\__ \\__ \\ | (__    \\ V  V / (_) | |  | | (_| |
 \\___/ \\__,_|_|  \\__,_|___/___/_|\\___|    \\_/\\_/ \\___/|_|  |_|\\__,_|
/ ___| _   _ ___| |_ ___ _ __ ___                                   
\\___ \\| | | / __| __/ _ \\ '_ ` _ \\                                  
 ___) | |_| \\__ \\ ||  __/ | | | | |                                 
|____/ \\__, |___/\\__\\___|_| |_| |_|                                 
       |___/                                                        

''', "access denied": '''


    _    ____ ____ _____ ____ ____    ____  _____ _   _ ___ _____ ____  
   / \\  / ___/ ___| ____/ ___/ ___|  |  _ \\| ____| \\ | |_ _| ____|  _ \\ 
  / _ \\| |  | |   |  _| \\___ \\___ \\  | | | |  _| |  \\| || ||  _| | | | |
 / ___ \\ |__| |___| |___ ___) |__) | | |_| | |___| |\\  || || |___| |_| |
/_/   \\_\\____\\____|_____|____/____/  |____/|_____|_| \\_|___|_____|____/ 

''', "access granted": '''

    _    ____ ____ _____ ____ ____            
   / \\  / ___/ ___| ____/ ___/ ___|           
  / _ \\| |  | |   |  _| \\___ \\___ \\           
 / ___ \\ |__| |___| |___ ___) |__) |          
/_/___\\_\\____\\____|_____|____/____/____ ____  
 / ___|  _ \\    / \\  | \\ | |_   _| ____|  _ \\ 
| |  _| |_) |  / _ \\ |  \\| | | | |  _| | | | |
| |_| |  _ <  / ___ \\| |\\  | | | | |___| |_| |
 \\____|_| \\_\\/_/   \\_\\_| \\_| |_| |_____|____/ 

'''}

class data():
    def __init__(self):
        self.paddocks = {
            1: True,
            2: True,
            3: True,
            4: False,
            5: True
        }

class commands():
    def __init__(self, data):
        self.data = data

    def levelOneClearance(self):
        input(colored("The action you are attempting requires level one clearance. Please enter password: ", "cyan"))
        return(True)
    
    def levelTwoClearance(self):
        input(colored("The action you are attempting requires level two clearance. Please insert card and then press enter on this workstation.", "cyan"))
        return(True)
    
    def levelThreeClearance(self):
        input(colored("The action you are attempting requires level three clearance. Facial recognition accepted, welcome Mr Masrani. Please press enter on workstation.", "cyan"))
        return(True)

    def stop(self):
        return(False)
    
    def getPaddockStatus(self):
        status = "\n"
        for item in self.data.paddocks:
            if self.data.paddocks[item]:
                status = f"{status}\n{colored(f"Paddock {item}:", "dark_grey")} {colored("LOCKED", "light_green")}"
            else:
                status = f"{status}\n{colored(f"Paddock {item}:", "dark_grey")} {colored("UNLOCKED", "light_red")}"
        status = status.replace("\n\n", "")
        return(status)
    
    def openPaddock(self):
        def open(target):
            target = int(target)
            if self.data.paddocks[target] == False:
                return(colored("Paddock already unlocked.", "light_red"))
            else:
                self.data.paddocks[target] = False
                return(colored("Paddock unlocked.", "light_green"))
        target = input(colored("Please enter paddock to unlock: ", "cyan"))
        if target == "*":
            self.levelThreeClearance()
            for item in range(1, 5):
                print(open(item))
            print(colored("All paddocks now unlocked.", "light_green"))
        else:
            self.levelTwoClearance()
            return(open(target))
            
        
    def closePaddock(self):
        def close(target):
            target = int(target)
            if self.data.paddocks[target] == True:
                return(colored("Paddock already locked.", "light_red"))
            else:
                self.data.paddocks[target] = True
                return(colored("Paddock locked.", "light_green"))
        target = input(colored("Please enter paddock to lock: ", "cyan"))
        if target == "*":
            self.levelThreeClearance()
            for item in range(1, 5):
                print(close(item))
            print(colored("All paddocks now locked.", "light_green"))
        else:
            self.levelTwoClearance()
            return(close(target))
            

def runConsole(commands: commands):
    running = True
    commandList = {
        "stop": commands.stop,
        "paddock status": commands.getPaddockStatus,
        "paddock unlock": commands.openPaddock,
        "paddock lock": commands.closePaddock
    }
    while running:
        command = input(colored("Please enter command: ", "cyan"))
        if command in commandList:
            response = (commandList[command])()
            if (response) == (False):
                running = False
            else:
                print(response)
        else:
            print(colored("No such command.", "light_red"))

print(colored(asciiText["jurassic world system"], "dark_grey"))
print(colored("Please enter credentials: ", "cyan"), end="")
credential = input()
if (credential.casefold()) != ("jack"):
    print(colored(asciiText["access denied"], "red"))
    exit("Invalid Credentials!")
else:
    print(colored(asciiText["access granted"], "light_green"))
    print(colored("Welcome to Jurassic World. Console mode enabled.", "light_green"))
    commands = commands(data())
    runConsole(commands)