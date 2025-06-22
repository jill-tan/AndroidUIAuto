from behave import given, when, then
from api.hko_api import get_forecast_data, get_humidity_day_after_tomorrow

@given("I have the forecast API")
def step_have_api(context):
    context.api_data = None

@when("I send the request for weather")
def step_send_request(context):
    context.api_data = get_forecast_data()
    assert context.api_data is not None

@then("I should get the humidity for the day after tomorrow")
def step_get_humidity(context):
    humidity = get_humidity_day_after_tomorrow(context.api_data)
    print(f"Relative humidity: {humidity}")
    assert humidity is not None
