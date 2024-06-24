import requests
import statistics
import sqlite3



#Creates the Weather class, which gives us the needed variables, with which we store data gained from API calls.
class Weather:

    # Mean Temperature Method
    #Gets the nessesary mean tempature from our target API for years 2019 - 2023
    def mean_tempature_method(self):

        urls = ["https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2023-01-01&end_date=2023-12-31&daily=temperature_2m_mean&wind_speed_unit=mph&precipitation_unit=inch",
                "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2022-01-01&end_date=2022-12-31&daily=temperature_2m_mean&wind_speed_unit=mph&precipitation_unit=inch",
                "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&daily=temperature_2m_mean&wind_speed_unit=mph&precipitation_unit=inch",
                "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2020-01-01&end_date=2020-12-31&daily=temperature_2m_mean&wind_speed_unit=mph&precipitation_unit=inch",
                "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2019-01-01&end_date=2019-12-31&daily=temperature_2m_mean&wind_speed_unit=mph&precipitation_unit=inch"
                ]
        mean_temp = []
        for url in urls:
            response = requests.get(url)
            year = response.json()['daily']['temperature_2m_mean']
            year = statistics.mean(year)
            mean_temp.append(year)
        return statistics.mean(mean_temp)

    # Max wind speed in MPH Method
    # Gets the necessary max wind in mph from our target API for years 2019 - 2023
    def max_wind_mph(self):

        urls = [
            "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2023-01-01&end_date=2023-12-31&daily=wind_speed_10m_max&wind_speed_unit=mph&precipitation_unit=inch",
            "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2022-01-01&end_date=2022-12-31&daily=wind_speed_10m_max&wind_speed_unit=mph&precipitation_unit=inch",
            "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&daily=wind_speed_10m_max&wind_speed_unit=mph&precipitation_unit=inch",
            "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2020-01-01&end_date=2020-12-31&daily=wind_speed_10m_max&wind_speed_unit=mph&precipitation_unit=inch",
            "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2019-01-01&end_date=2019-12-31&daily=wind_speed_10m_max&wind_speed_unit=mph&precipitation_unit=inch"
            ]
        max_wind = []
        for url in urls:
            response = requests.get(url)
            year = response.json()['daily']['wind_speed_10m_max']
            year = max(year)
            max_wind.append(year)
        return max(max_wind)

    # Sum of Precipitation in inches Method
    # Gets the necessary sum of precipitation in inches our target API for years 2019 - 2023
    #This is the old version of the code I made, this is to showcase how I took a long code block
    #and transformed it into a for loop as shown above vs the old version which is shown below.
    def sum_precipitation_in(self):

        # Gets data from year 2023
        url = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2023-01-01&end_date=2023-12-31&daily=precipitation_sum&precipitation_unit=inch"
        response = requests.get(url)
        year2023 = response.json()['daily']['precipitation_sum']
        # Gets data from year 2022
        url1 = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2022-01-01&end_date=2022-12-31&daily=precipitation_sum&precipitation_unit=inch"
        response1 = requests.get(url1)
        year2022 =  response1.json()['daily']['precipitation_sum']
        # Gets data from year 2021
        url2 = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&daily=precipitation_sum&precipitation_unit=inch"
        response2 = requests.get(url2)
        year2021 =  response2.json()['daily']['precipitation_sum']
        # Gets data from year 2020
        url3 = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2020-01-01&end_date=2020-12-31&daily=precipitation_sum&precipitation_unit=inch"
        response3 = requests.get(url3)
        year2020 =  response3.json()['daily']['precipitation_sum']
        # Gets data from year 2019
        url4 = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2019-01-01&end_date=2019-12-31&daily=precipitation_sum&precipitation_unit=inch"
        response4 = requests.get(url4)
        year2019 =  response4.json()['daily']['precipitation_sum']
        # Combines all years to get the mean temp from all years
        sum_prec = year2023 + year2022 + year2021 + year2020 + year2019
        return sum(sum_prec)

# Creates SQL database and table, including all needed variables from weather API
class Weather_db_class:
    def weather_db_method(self):
        #establishes connection
        connection = sqlite3.connect('weather_db')
        cursor = connection.cursor()

        command1 = """CREATE TABLE IF NOT EXISTS weather_table_real(primary_k INT PRIMARY KEY, location_latitude_t INT, location_longitude_t INT, month_t INT, day_of_month_t INT, year_t INT, five_year_average_temperature_on_chosen_date_t INT,
                 five_year_minimum_temperature_on_chosen_date_t INT, five_year_maximum_temperature_on_chosen_date_t INT, five_year_average_wind_speed_on_chosen_date_t INT,
                 five_year_minimum_wind_speed_on_chosen_date_t INT, five_year_maximum_wind_speed_on_chosen_date_t INT, five_year_sum_precipitation_on_chosen_t INT,
                 five_year_minimum_precipitation_on_chosen_date_t INT,five_year_maximum_precipitation_on_chosen_date_t INT)"""
        cursor.execute(command1)

        #Gets nessesary data from Weather Class.
        max_temp = Weather.mean_tempature_method(0)
        max_wind = Weather.max_wind_mph(0)
        sum_prec = Weather.sum_precipitation_in(0)

        # inserts data into the table
        params = (1, 52.52, 13.41, 12, 25, 2023, max_temp,-14.9,35.5,8.496833,0,max_wind,sum_prec,0,1626)
        cursor.execute("INSERT INTO weather_table_real VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
        #calls the database to show the tables contents using a SELECT all statement
        cursor.execute("SELECT * FROM weather_table_real")

        results = cursor.fetchall()
        return results

