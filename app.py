from selenium import webdriver
from multiprocessing import Process
import time


class Locators:
    enter_pin = 'input[id="game-input"]'
    enter_name = 'input[name="nickname"]'
    enter_button = 'button[type="submit"]'

class Bot:
    def __init__(self, browser):
        self.browser = browser

    def enter_pin(self, pin):
        box_element = self.browser.find_element_by_css_selector(Locators.enter_pin)
        box_element.click()
        box_element.send_keys(pin)
        enter_button = self.browser.find_element_by_css_selector(Locators.enter_button)
        enter_button.click()

    def enter_name(self, name):
        box_element = self.browser.find_element_by_css_selector(Locators.enter_name)
        box_element.click()
        box_element.send_keys(name)
        enter_button = self.browser.find_element_by_css_selector(Locators.enter_button)
        enter_button.click()

pin = '9175072'

def main(num):
    for player in range(10):
        if num == 1:
            name = 'Player{}'.format(player)
        else:
            name = 'Player{}'.format(num*10+player)
        chrome = webdriver.Chrome(executable_path='chromedriver79.exe')
        bot = Bot(chrome)
        chrome.get('https://kahoot.it/')
        #pin = input('Enter pin: ')
        bot.enter_pin(pin)
        time.sleep(2)
        #name = input('Enter name:')
        bot.enter_name(name)

if __name__== '__main__':
    p1 = Process(target=main, args=(1,))
    p2 = Process(target=main, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
