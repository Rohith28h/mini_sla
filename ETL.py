import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('minmini.csv')

# print(df.head())
# print("Shape of Dataset:", df.shape)
# print("Columns:", df.columns)
# print(df.dtypes)
# print(df.info())
# Data Quality Check
print("null values",df.isnull().sum())
print("Statistical Summary",df.describe())
print("Duplicate Rows:", df.duplicated().sum())