Feature: 9-Day Weather Forecast

  Scenario: Check the 9th day's weather forecast
    Given the app is launched
    When I open the 9-day forecast screen
    Then I should see the 9th day's weather information

  Scenario: Get relative humidity from API
    Given I have the forecast API
    When I send the request for weather
    Then I should get the humidity for the day after tomorrow
