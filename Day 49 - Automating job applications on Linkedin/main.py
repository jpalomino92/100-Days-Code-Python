from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://www.linkedin.com/jobs/search/?alertAction=viewjobs&currentJobId=3913551283&distance=25&f_AL=true&f_TPR=r2592000&f_WT=2&geoId=103644278&keywords=technical%20support%20engineer&location=Estados%20Unidos&origin=JOB_SEARCH_PAGE_JOB_FILTER&sortBy=R'
ACCOUNT_EMAIL = "*"
ACCOUNT_PASSWORD = "*"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)
time.sleep(5)

get_signin_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
get_signin_button.click()
time.sleep(3)

get_user_name_input = driver.find_element(by=By.ID, value="username")
get_user_name_input.send_keys(ACCOUNT_EMAIL)

get_pass_input = driver.find_element(by=By.ID, value="password")
get_pass_input.send_keys(ACCOUNT_PASSWORD, Keys.ENTER)

time.sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="ember43"]').click()

#driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button").click()

job_list = driver.find_elements(by=By.CSS_SELECTOR, value='.job-card-container--clickable')

for job in job_list:
    print("checking listing")
    job.click()
    time.sleep(2)




