README file.

This project had been designed to showcase my coding skills in python when it comes to working an ETL process.
The ETL I have designed uses SQLite as its database and the Weather API as its datasource.

The steps of the project are as follows:
    - Extract
        - I use three functions in the code.py file to extract 5 years of data from the Weather API.
    - Transform
        - I then crunch that information down into a single value within each function to return a 5-year
          result from the data.
    - Load
        - I finish by using SQLite to create a local database and then load the data the database.

Below is a description of what each section of code does from each file.

- main.py
    - print methods statements
        These statements prints all three methods from the code.Weather class and gives them each a description inside the f string.
    - print database statement
        This statement prints the weather_database and queries all rows, which results in all the weather data being displayed for the user to easily see.
    - print test statements
        These three print statements are used to run each of the three tests from the Tests class in test.py.

- code.py
    - Weather class
        This class contains the three methods to return the 5-year mean temperature, max wind speed, and sum of precipitation using the Weather API.
    - Weather_db_class
        This class creates the weather database, creates a table to store the data, then stores the data and prints it when the weather_db_method is called.

- test.py
    - Tests class
        This class is used to store the three test methods, which are: test_sum_precipitation method, test_max_wind method and test_mean_temp method.
