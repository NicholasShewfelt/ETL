import code
import unittest

class Tests(unittest.TestCase):

    #Creates a test for the sum_precipitation_in funciton
    def test_sum_precipitation(self):
        result = code.Weather.sum_precipitation_in(0)
        assert result == 120.1790000000002
        if result == 120.1790000000002:
            return "Test 1 Passes"
        else:
            return "Test 1 Does Not Pass"

    # Creates a test for the max_wind_mph function
    def test_max_wind(self):
        result = code.Weather.max_wind_mph(0)
        assert result == 30.9
        if result == 30.9:
            return "Test 2 Passes"
        else:
            return "Test 2 Does Not Pass"

  #Creates a test for the mean_tempature_method function
    def test_mean_temp(self):
        result = code.Weather.mean_tempature_method(0)
        assert result == 10.988584474885846
        if result == 10.988584474885846:
            return "Test 3 Passes"
        else:
            return "Test 3 Does Not Pass"
