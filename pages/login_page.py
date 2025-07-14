from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver=driver
    
    #function to login the webpage
    def login(self,email,password):
        self.driver.find_element(By.NAME,"email").send_keys(email)
        self.driver.find_element(By.NAME,"password").send_keys(password)
        self.driver.find_element(By.XPATH,"//label[@for='rememberme']").click()
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
