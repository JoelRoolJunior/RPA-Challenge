from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .web_elements import DontPadElements

class DontPadActions:
    def __init__(self,driver:webdriver.Chrome) -> None:
        self.driver = driver
        self.elements = DontPadElements
    
    def goto(self):
        self.driver.switch_to.new_window('tab')
        self.driver.get('https://dontpad.com/result_RPAChallenge')
        sleep(3)

    
    def await_text_area(self):
        text_area = self.driver.find_element(By.XPATH, self.elements.textarea)
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.visibility_of(text_area))
    
    def pgdown(self):  
        ActionChains(self.driver)\
            .key_down(Keys.PAGE_DOWN)\
            .perform()
    
    def save_dontpad(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.elements.saved)))

    def insert_text(self,text:str):
        self.await_text_area()
        self.pgdown()
        ActionChains(self.driver)\
            .send_keys('\n')\
            .send_keys(text)\
            .send_keys('\n')\
            .perform()
        self.save_dontpad()
        
        
        

    
