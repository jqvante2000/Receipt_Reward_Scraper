import pytesseract
import cv2
from selenium import webdriver
from selenium.webdriver.common.by import By
from chipotle import get_chipotle_information
from panda_express import *
PATH = '/Users/jevanteqaiyim/Documents/Receipt_Reward_Scraper/chromedriver'
file_name_chipotle = '/Users/jevanteqaiyim/Documents/Receipt_Reward_Scraper/TEST_PHOTOS/IMG_4103.jpg'
file_name_panda = '/Users/jevanteqaiyim/Documents/Receipt_Reward_Scraper/TEST_PHOTOS/panda.jpg'
site = webdriver.Chrome(executable_path=PATH)

def get_image_text(file_name):
    image = cv2.imread(file_name,0)
    text=(pytesseract.image_to_string(image)).lower()
    split_text = text.split()
    return split_text

def get_restaurant(site, split_text):
    if 'chipotle' in split_text or 'Chipotle' in split_text:
        get_chipotle_information(site, split_text)
    
    elif 'panda' in split_text or 'express' in split_text:
        get_panda_express_information(site, split_text)
    

file_split_text = get_image_text(file_name_panda)
get_restaurant(site, file_split_text)