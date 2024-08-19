from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from .web_elements import RpaChallengeElements

class RpachallengeActions:

    def __init__(self,
                 driver:webdriver.Chrome) -> None:
        self.driver = driver
        self.elements = RpaChallengeElements

    def start(self):
        self.driver.get('https://www.rpachallenge.com/')
        self.driver.find_element(By.XPATH, self.elements.start_button).click()
        
    def first_name(self,content:str):
        self.driver.find_element(By.XPATH, self.elements.first_name).send_keys(content)

    def last_name(self,content:str):
        self.driver.find_element(By.XPATH, self.elements.last_name).send_keys(content)
    
    def company_name(self,content:str):
        self.driver.find_element(By.XPATH, self.elements.company_name).send_keys(content)
    
    def role_in_company(self,content:str):
        self.driver.find_element(By.XPATH, self.elements.role_in_company).send_keys(content)
    
    def address(self,content:str):
        self.driver.find_element(By.XPATH, self.elements.address).send_keys(content)

    def email(self,content:str):
        self.driver.find_element(By.XPATH, self.elements.email).send_keys(content)
    
    def phone(self,content:str):
        self.driver.find_element(By.XPATH, self.elements.phone).send_keys(content)

    def submit_click(self):
        self.driver.find_element(By.XPATH, self.elements.submit).click()

    def get_result(self):
        return self.driver.find_element(By.XPATH, self.elements.result).text

    def inputs(self,
               value_first_name,
               value_last_name,
               value_company_name,
               value_role,
               value_address,
               value_email,
               value_phone):
        self.first_name(value_first_name)
        self.last_name(value_last_name)
        self.company_name(value_company_name)
        self.role_in_company(value_role)
        self.address(value_address)
        self.email(value_email)
        self.phone(value_phone)
        self.submit_click()

