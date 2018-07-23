# Divvy Chicago Bicycle Sharing project

## Goal: Predict the daily need of bikes for each divvy station and search for new locations to open a new Divvy Bicycle station.

## Workflow
- Data collection
  - Collect divvy bike sharing data from [divvy website](https://www.divvybikes.com/system-data).
  - Collect weather of Chicago data [wunderground](/https://www.wunderground.com/).
  - Collect other related data in Chicago from https://data.cityofchicago.org/
    - public safety
    - transportation 
      - daily traffic
      - bike lanes availablity
      - bus/train stops
      
- Exploratory Data Analysis
  - Visualize divvy bikes used over different time periods
    - week of day
    - month
    - season
  - Analyze data of each trip
    - Customer Gender
    - Customer Age
    - Trip duration
    - Trip direct distance
  - Investigate geospatial information
    - crime occurance near a bike station
    - bus/train stop availabilty
    - nearby bike lanes
  - Study the correlation between bike usage and weather of that day
    - humidity
    - temperature
    - wind speed

- Feature Engineering
  - Merge bike station data with trip data and group the merged data by different dates and stations
  - Add daily weather features including humidity, temperature, wind speed and etc.
  - Add crime data for each station, for example number of crime within 1 mile from the bike station over last week
  - Add public transportation data, for example the distance between the divvy bike station to the closest bus stop.
  
- Machine learning model
  - Build regression models using random forest, gradient boost and neural network
  - Compare performance of different models
  - Predict the daily need of bike using our model
  
