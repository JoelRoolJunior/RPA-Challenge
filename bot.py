from selenium import webdriver
from datetime import datetime

from app.components.read_challenge import read_challenge_data
from app.components.RpaChallenge import RpachallengeActions
from app.components.DontPad import DontPadActions

def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    bot_challenge = RpachallengeActions(driver)
    bot_register = DontPadActions(driver)
    data = read_challenge_data()

    bot_challenge.start()
    for content in data:
        bot_challenge.inputs(
            value_first_name=content['first_name'],
            value_last_name=content['last_name'],
            value_company_name=content['company_name'],
            value_role=content['role_in_company'],
            value_address=content['address'],
            value_email=content['email'],
            value_phone=content['phone_number']
        )

    result = bot_challenge.get_result()
    result_size = len(result)
    now = datetime.now().strftime('%Y-%m-%d')
    message = f'{now} -- {result}'

    bot_register.goto()
    bot_register.insert_text(message)
    
    driver.quit()

if __name__=='__main__':
    main()