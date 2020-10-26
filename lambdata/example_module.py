"""Lambdata - a collection of Data Science helper functions"""

# accessing libraries through pipenv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


FAVORITE_NUMBERS = [2.71, 101, 55, 12, 3.14]

# Implement your helper functions
def split(df, target):
    split_df = df.copy()
    y = split_df[target]
    X = split_df.drop(target, axis=1)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=42
    )
    print(
        "X_train: ",
        X_train.shape,
        "\nX_test: ",
        X_test.shape,
        "\ny_train: ",
        y_train.shape,
        "\ny_test: ",
        y_test.shape,
    )
    return X_train, X_test, y_train, y_test


def df_destroyer(df):
    for cols in df.columns:
        print(cols, " Nulls = ", df[cols].isnull().sum())
        print("df cleaned! No more nulls")
        df = df.dropna()
        return df


test_df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})

df_destroyer(test_df)