import code
import test

#Shows the three variables we are gathering for the study
print('Wellcome to my ETL project.')
print('Below we will see three variables generated from calling the Weather API.')
print('These variables will be calculated from 5 years worth of data!')
print('Lets take a look at each of them:')
print(f'Mean Temp Method results = {code.Weather.mean_tempature_method(0)}')
print(f'Max Wind Method results = {code.Weather.max_wind_mph(0)}')
print(f'Sum Precipitation Method results = {code.Weather.sum_precipitation_in(0)}')
print()

#calls weather_db
print('This is the SQLite table showing all info added to a database table.')
print('This info will include the three variables plus several other hard coded data.')
print('Lets take a look:')
print(code.Weather_db_class.weather_db_method(0))
print()


#runs all tests from tests.py
print('Now lets run three tests from test.py to make sure the code can pass tests')
print(test.Tests.test_sum_precipitation(0))
print(test.Tests.test_max_wind(0))
print(test.Tests.test_mean_temp(0))