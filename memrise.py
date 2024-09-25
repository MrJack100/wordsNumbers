from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, base64, json
from termcolor import colored

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
    return("Success")

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

    return("Success")

def answerQuestion(driver: webdriver.Firefox, timeout: int = 10):
    elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div/div[5]/button/div")))
    print(colored(elem.text, "red"))
    elem.click()
    return(True)

def _authenticationInfo() -> tuple[str, str]:
    with open("DoNotTrackFiles.json", "r") as file:
        notice, usernameB64, passwordB64 = json.loads(file.read())
    username = base64.b64decode(usernameB64['username-base64'])
    password = base64.b64decode(passwordB64['password-base64'])
    username = username.decode(encoding="utf-8")
    password = password.decode(encoding="utf-8")
    return(username, password)

driver = webdriver.Firefox()
driver.get("https://community-courses.memrise.com/signin?next=/groups/")
username, password = _authenticationInfo()
logIn(driver, username=username, password=password, timeout=60)
print(colored("SUCCESS: Logged in successfully.", "green"))
navigateToLesson(driver, timeout=60)
print(colored("SUCCESS: Opened lesson.", "green"))

lessonOngoing = True
increment = 0
while lessonOngoing:
    lessonOngoing = answerQuestion(driver, timeout=60)
    increment = increment + 1
    if increment % 20 == 0:
        print(increment)

time.sleep(120)
driver.quit()
print(colored("INFO: Driver closed.", "blue"))

"/html/body/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[4]/button/div[2]/span"
"/html/body/div[2]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[2]/button/div[2]/span"