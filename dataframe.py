"""Extracts dataset from HW2 and raises ValueError based on condition being or not"""
import pandas as pd
import hw2


def col_checker(url):
    """Checks if all columns match in the two datasets"""
    is_same_name = True
    if url is None:
        df_filt = hw2.base_data()
    else:
        df_filt = pd.read_csv(url)
    if (set(df_filt.columns) !=
            set(['Year', 'City', 'Sport', 'Event gender', 'Medal'])):
        is_same_name = False
    return is_same_name


def minonerow(url):
    """Checks if there is at least one row in the dataset being tested"""
    is_min_one_row = True
    if url is None:
        df_filt = hw2.base_data()
    else:
        df_filt = pd.read_csv(url)
    if df_filt.empty:
        is_min_one_row = False
    return is_min_one_row


if __name__ == "__main__":
    if col_checker():
        print("Dataframe has supported columns")
    else:
        raise ValueError('Dataframe does not have only the supported columns')
