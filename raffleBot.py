import sys

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    EXTENSION_PATH = './10.8.1_0.crx'
    opt = webdriver.ChromeOptions()
    opt.add_extension(EXTENSION_PATH)
    return webdriver.Chrome(ChromeDriverManager().install(), options=opt)
