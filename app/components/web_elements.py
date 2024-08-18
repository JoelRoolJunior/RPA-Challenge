############################################################
#####              RPA Challenge elements              #####
############################################################
class RpaChallengeElements:
    start_button    = '//button[text()="Start"]'
    first_name      = '//input[contains(@ng-reflect-name,"FirstName")]'
    last_name       = '//input[contains(@ng-reflect-name,"LastName")]'
    company_name    = '//input[contains(@ng-reflect-name,"CompanyName")]'
    role_in_company = '//input[contains(@ng-reflect-name,"Role")]'
    address         = '//input[contains(@ng-reflect-name,"Address")]'
    email           = '//input[contains(@ng-reflect-name,"Email")]'
    phone           = '//input[contains(@ng-reflect-name,"Phone")]'
    submit          = '//input[@type="submit"]'