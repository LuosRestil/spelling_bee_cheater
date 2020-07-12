from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

magic = 'l'
letters = 'befinxl'
results = []

with open('valid.txt', 'r') as infile:
    for line in infile:
        word = line[:-1]
        valid = True
        if magic not in word:
            valid = False
            continue
        for letter in word:
            if letter not in letters:
                valid = False
                break
        if valid:
            results.append(word)

print(results)
print(len(results))

# TODO Set up bot to enter results into game with Selenium
# class BeeBot:
#     def __init__(self):
#         self.bot = webdriver.Firefox()
#
#     def game_setup: