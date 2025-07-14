from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

class ClientPage:

    def __init__(self,driver,wait):
        #initialize driver
        self.driver=driver

    def go_to_client_page(self):
        #go to client page
        self.driver.find_element(By.XPATH,"//a[@href='/clients/v1/index']").click()

    def click_add_client(self):
        #click add to client
        self.driver.find_element(By.XPATH,"//a[@href='/clients/v1/basic-info/']").click()

    def fill_client_form(self):
        self.driver.find_element(By.ID, "client_name").send_keys("TEST CLIENT2")
        Select(self.driver.find_element(By.ID, "company_type")).select_by_visible_text("Private Ltd")
        self.driver.find_element(By.ID, "pan_number").send_keys("AACFA1234B")
        self.driver.find_element(By.ID, "gst_number").send_keys("29AACFA1234B1Z5")
        self.driver.find_element(By.ID, "cin_number").send_keys("U12345KA2010PTC000069")
        self.driver.find_element(By.ID, "official_email").send_keys("contact@aaryatech.in")
        self.driver.find_element(By.ID, "mobile").send_keys("9876543210")
        self.driver.find_element(By.ID, "landline").send_keys("080-23456789")
        self.driver.find_element(By.ID, "country").send_keys("India")

        Select(self.driver.find_element(By.ID, "state")).select_by_visible_text("KERALA")

        self.wait.until(EC.text_to_be_present_in_element((By.ID, "city"), "Kollam"))
        Select(self.driver.find_element(By.ID, "city")).select_by_visible_text("Kollam")

        self.driver.find_element(By.ID, "address").send_keys("MG Road, Bengaluru")

    def submit_client_form(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='clientForm']/div[2]/button"))).click()

    def search_and_confirm_client(self):
        self.driver.find_element(By.XPATH, "//input[@class='form-field']").send_keys("TestClient")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()