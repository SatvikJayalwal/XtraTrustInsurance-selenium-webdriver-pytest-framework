from pages.login_page import LoginPage
from pages.client_page import ClientPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_add_client(driver,config,wait):
    #creating object of class LoginPage 
    login=LoginPage(driver)
    #calling login function under LoginPage class through login object
    login.login(config["credentials"]["email"],config["credentials"]["password"])
    
    #creating object of class ClientPage 
    client=ClientPage(driver,wait)

    #calling all functions under ClientPage class through its object
    client.go_to_client_page()
    client.click_add_client()
    client.fill_client_form()
    client.submit_client_form()
    client.search_and_confirm_client()






