from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class InternetSpeedTwitterBot():
    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(self.chrome_option)
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")

        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        time.sleep(5)

        # Dismiss the cookie consent banner if it appears
        try:
            accept_btn = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
            accept_btn.click()
            time.sleep(1)
        except NoSuchElementException:
            pass

        # Use a stable selector instead of a dynamic .css-... class name
        go_button = self.driver.find_element(By.CSS_SELECTOR, value="button[aria-label*='start speed test']")
        go_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
