#TODO: Import the module that will allow you to use Selenium
from selenium import webdriver
#TODO: Import the module that will allow you to use the up, down, left, and right keys on your keyboard
from selenium.webdriver.common.keys import Keys

def play2048( times ):
    #TODO: write code in this function that:
    # 1. opens a game of 2048 from the URL: https://gabrielecirulli.github.io/2048/
    # 2. uses the parameter 'times' to determine how many times your code will try to play the game
    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT
    # 4. print the final score after all tries to the screen 
    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')

    htmlElem = browser.find_element_by_tag_name('html')

    for i in range(times):
        htmlElem.send.keys(Keys.UP)
        htmlElem.send.keys(Keys.RIGHT)
        htmlElem.send.keys(Keys.DOWN)
        htmlElem.send.keys(Keys.LEFT)

    finalScore = browser.find_element_by_class_name('score-container').text
    print('Alpha2048 scored ' + finalScore.split('\n')[0] + '.')