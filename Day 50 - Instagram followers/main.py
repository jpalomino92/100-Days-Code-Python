from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Instafollowers:
    def __init__(self):
        self.follower_list = None
        self.notifications_pop_up = None
        self.pop_up = None
        self.password = None
        self.user_name = None
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = 'https://www.instagram.com/accounts/login/'
        account_email = "*"
        account_password = "*"
        self.driver.get(url)
        time.sleep(4.2)

        # enter email

        self.user_name = self.driver.find_element(by=By.NAME, value="username")
        self.user_name.send_keys(account_email)

        # enter password

        self.password = self.driver.find_element(by=By.NAME, value="password")
        self.password.send_keys(account_password, Keys.ENTER)

        # Click "Not now" and ignore Save-login info prompt

        time.sleep(4.3)
        self.pop_up = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Ahora no')]")
        if self.pop_up:
            self.pop_up.click()

        # Click "Not now" and ignore Save-login info prompt

        time.sleep(3.7)
        self.notifications_pop_up = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Ahora no')]")
        if self.notifications_pop_up:
            self.notifications_pop_up.click()

    def find_followers(self):
        time.sleep(2)
        similar_account = "pildoras_de_programacion"
        self.driver.get(f"https://www.instagram.com/{similar_account}/followers/")
        time.sleep(6)
        self.follower_list = self.driver.find_elements(by=By.XPATH, value="//div[contains(text(), 'Seguir')]")

    def follow(self):
        print(len(self.follower_list))
        for follower in self.follower_list:
            follower.click()
            print("Follower added.")
            time.sleep(2)


bot = Instafollowers()
bot.login()
bot.find_followers()
bot.follow()
