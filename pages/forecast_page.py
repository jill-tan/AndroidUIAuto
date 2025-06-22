from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

class ForecastPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_forecast(self):
        forecast_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "9-day Forecast")
        forecast_button.click()
        sleep(2)

    def get_ninth_day_forecast(self):
        elements = self.driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc,'forecast-day')]")
        if len(elements) >= 9:
            return elements[8].text
        return None
