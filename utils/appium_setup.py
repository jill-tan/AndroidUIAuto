from appium.options.android import UiAutomator2Options
from appium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

def get_driver():
    options = UiAutomator2Options()
    options.platform_name = os.getenv("PLATFORM_NAME")
    options.device_name = os.getenv("DEVICE_NAME")
    options.app_package = os.getenv("APP_PACKAGE")
    options.app_activity = os.getenv("APP_ACTIVITY")
    
    driver = webdriver.Remote("http://localhost:4723", options=options)
    return driver
