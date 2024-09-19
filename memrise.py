from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, base64, json

def logIn(driver, username=None, password=None):

    originalWindow = driver.current_window_handle
    time.sleep(5)
    elem = driver.find_element(By.CLASS_NAME, "L5Fo6c-bF1uUb")
    elem.click()

    for window_handle in driver.window_handles:
        if window_handle != originalWindow:
            driver.switch_to.window(window_handle)
            break

    time.sleep(3)
    elem = driver.find_element(By.ID, "identifierId")
    elem.send_keys(username)
    
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button")
    elem.click()

    time.sleep(3)
    elem = driver.find_element(By.ID, "i0116")
    elem.send_keys(username)

    elem = driver.find_element(By.ID, "idSIButton9")
    elem.click()

    time.sleep(3)
    elem = driver.find_element(By.ID, "i0118")
    elem.send_keys(password)

    elem = driver.find_element(By.ID, "idSIButton9")
    elem.click()

    time.sleep(3)
    elem = driver.find_element(By.ID, "idSIButton9")
    elem.click()

    driver.switch_to.window(originalWindow)
    time.sleep(10)

with open("DoNotTrackFiles.json", "r") as file:
    notice, usernameB64, passwordB64 = json.loads(file.read())
username = base64.b64decode(usernameB64['username-base64'])
password = base64.b64decode(passwordB64['password-base64'])
username = username.decode(encoding="utf-8")
password = password.decode(encoding="utf-8")
driver = webdriver.Firefox()
driver.get("https://app.memrise.com/signin")
assert "Log in to your account" in driver.title
logIn(driver, username=username, password=password)
driver.close()