from behave import given, when, then
from pages.forecast_page import ForecastPage
from utils.appium_setup import get_driver

@given('the app is launched')
def step_launch_app(context):
    context.driver = get_driver()
    context.page = ForecastPage(context.driver)

@when('I open the 9-day forecast screen')
def step_open_forecast(context):
    context.page.navigate_to_forecast()

@then("I should see the 9th day's weather information")
def step_check_9th_day(context):
    forecast = context.page.get_ninth_day_forecast()
    assert forecast is not None and forecast != "", "Forecast data missing"
