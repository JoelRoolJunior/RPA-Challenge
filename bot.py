from selenium import webdriver

from app.components.read_challenge import read_challenge_data
from app.components.Actions import RpachallengeActions

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    bot = RpachallengeActions(driver)
    data = read_challenge_data()

    bot.goto()
    bot.start()
    for content in data:
        bot.inputs(
            value_first_name=content['first_name'],
            value_last_name=content['last_name'],
            value_company_name=content['company_name'],
            value_role=content['role_in_company'],
            value_address=content['address'],
            value_email=content['email'],
            value_phone=content['phone_number']
        )
    
    driver.quit()

if __name__=='__main__':
    main()