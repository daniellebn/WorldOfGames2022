import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(url):
    my_driver = webdriver.Chrome()
    my_driver.get("http://localhost:5000")
    if 0 < int(my_driver.find_element(By.ID, "score").text) < 1001:
        return True
    else:
        return False


def main_function():
    if test_scores_service("http://localhost:5000"):
        return 0
    else:
        return -1




