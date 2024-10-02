from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, base64, json, keyboard
from termcolor import colored

class Databank:
    def __init__(self):
        self.translations = {}
    
    def upload(self, english, spanish):
        self.translations.update({english: spanish})

    def checkIfTranslationPresent(self, englishOrSpanish):
        if englishOrSpanish in self.translations.keys():
            return(self.translations[englishOrSpanish])
        elif englishOrSpanish in self.translations.values():
            for translation in self.translations:
                if englishOrSpanish in self.translations[translation]:
                    return(translation)
        else:
            return(False)

def logIn(driver: webdriver.Firefox, username: str = str, password: str = str, timeout: int = 10) -> None:
    originalWindow = driver.current_window_handle
    # elem = driver.find_element(By.CLASS_NAME, "L5Fo6c-bF1uUb")
    elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "L5Fo6c-bF1uUb")))
    elem.click()

    for window_handle in driver.window_handles:
        if window_handle != originalWindow:
            driver.switch_to.window(window_handle)
            break

    # elem = driver.find_element(By.ID, "identifierId")
    elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "identifierId")))
    elem.send_keys(username)
    
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button")
    elem.click()

    # elem = driver.find_element(By.ID, "i0116")
    elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "i0116")))
    elem.send_keys(username)

    elem = driver.find_element(By.ID, "idSIButton9")
    elem.click()

    # elem = driver.find_element(By.ID, "i0118")
    elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "i0118")))
    elem.send_keys(password)

    elem = driver.find_element(By.ID, "idSIButton9")
    elem.click()

    # elem = driver.find_element(By.ID, "idSIButton9")
    elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "idSIButton9")))
    elem.click()

    driver.switch_to.window(originalWindow)
    return(True)

def navigateToLesson(driver: webdriver.Firefox, timeout: int = 10):
    while "Groups - Memrise" != driver.title:
        pass
    driver.refresh()
    elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[1]/a")))
    elem.click()

    elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div[2]/a[4]")))
    elem.click()

    elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div[4]/a")))
    elem.click()

    return(True)

def answerQuestion(driver: webdriver.Firefox, databank: Databank, timeout: int = 10):
    checkboxButton = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div/div[5]/button/div")))
    checkboxText = (checkboxButton.text).lower()
    if ("next" in checkboxText) or ("correct" in checkboxText):
        checkboxButton.click()
    elif "know" in checkboxText:
        #options = {}
        #for increment in range(1, 5):
        #    path = f"/html/body/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[{increment}]/button/div[2]/span"
        #    elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, path)))
        #    options.update({path: elem})
        #print(options)
        #for path in options:
        #    translation = databank.checkIfTranslationPresent(options[path])
        #    if translation == False:
        #        options[path].click()
        #        break
        #if "correct" in checkbox:
        try:
            elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[1]/button/div[2]/span")))
            elem.click()
        except:
            try:
                while True:
                    try:
                        elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-10ppnn4-0 gUhKLZ")))
                        elem.click()
                        break
                    except:
                        break
            except:
                print("?")

    return(True)

def _authenticationInfo() -> tuple[str, str]:
    with open("DoNotTrackFiles.json", "r") as file:
        notice, usernameB64, passwordB64 = json.loads(file.read())
    username = base64.b64decode(usernameB64['username-base64'])
    password = base64.b64decode(passwordB64['password-base64'])
    username = username.decode(encoding="utf-8")
    password = password.decode(encoding="utf-8")
    return(username, password)

def main():
    driver = webdriver.Firefox()
    driver.get("https://community-courses.memrise.com/signin?next=/groups/")
    username, password = _authenticationInfo()
    logIn(driver, username=username, password=password, timeout=60)
    print(colored("SUCCESS: Logged in successfully.", "green"))
    for increment in range(int(input(colored("Enter how many times to run: ", "green", on_color="on_white")))):
        navigateToLesson(driver, timeout=60)
        print(colored("SUCCESS: Opened lesson.", "green"))
        databank = Databank()

        lessonOngoing = True
        while lessonOngoing:
            lessonOngoing = answerQuestion(driver, databank, timeout=10)
        
        driver.get("https://community-courses.memrise.com/groups/")
        print(colored(f"SUCCESS: {increment} lesson(s) have been completed.", "green"))
    driver.quit()
    print(colored("INFO: Driver closed.", "blue"))

def restartProtocol(limit=3):
    crashes = 0
    while limit != crashes:
        try:
            print(colored("INFO: Starting program.", "blue"))
            main()
            break
        except:
            print(colored("CRITICAL: Crash detected.", "red"))
            crashes = crashes + 1
    if crashes == limit:
        return(False)
    else:
        return(True)

if __name__ == "__main__":
    if restartProtocol(limit=3):
        print(colored("SUCCESS: Program ran within given parameters.", "green"))
    else:
        print(colored("CRITICAL: Program crashes exceeded given parameters and has been terminated.", "red"))

"/html/body/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[4]/button/div[2]/span"
"/html/body/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[2]/button/div[2]/span"