"""Collection of function to test the unit test cases"""
from dataframe import col_checker
from dataframe import minonerow


def test_expected_cols():
    """Testing for matching columns"""
    assert col_checker('http://www-bcf.usc.edu/~gareth/ISL/Auto.csv')


def test_atleast_one_row():
    """Testing for min one row"""
    assert minonerow('http://www-bcf.usc.edu/~gareth/ISL/Auto.csv')

# For running the unit tests
# test_expected_cols()
# test_atleast_one_row()
