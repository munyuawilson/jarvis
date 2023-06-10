import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--disable-dev-shm-usage')




url="https://bard.google.com/"

def bardTextOutput(url,text):
    
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        search = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "mat-mdc-input-element cdk-textarea-autosize ng-tns-c3522981110-2 ng-pristine ng-valid gmat-mdc-input mat-mdc-form-field-textarea-control mat-mdc-form-field-input-control mdc-text-field__input cdk-text-field-autofill-monitored ng-touched")))
        search.send_keys(text)
        search.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)

        text_output=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//*[@class='model-response-text ng-tns-c1133503624-5 ng-star-inserted']" )))
        
        time.sleep(10)
        print(text_output)
        driver.quit()


bardTextOutput(url,"hello")
        
