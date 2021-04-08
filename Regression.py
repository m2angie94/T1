# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 04:53:15 2021

@author: m2ang
"""


#a. import the necessary libraries and read csv file
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.pyplot as plt


# To import the data from csv to pandas package
avocado = pd.read_csv('avocado.csv')
#avocado=avocado.dropna()

# To display the list of variables in the dataframe from the imported data
print(list(avocado.columns))

# To display the first five rows of the data
print("\nThe first five rows of the data ")
print(avocado.head())
# To check the structure of the data
avocado.info()


 # To get some statistics about the data
avocado.describe()
#B.Draw scatter plots to show the relationship between average price and total volume and that between average price and total bags. Does the relationship look positive or negative? (15pts) 
# Scatter plot between average price and total volume
# Draw a scatter plot

avocado.plot.scatter(x='AveragePrice', y='Total Volume',
                   title= "Scatter plot between Average Price and Total Volume", color='pink')

plt.show

# The scatter plot between average price and total bags
avocado.plot.scatter(x='AveragePrice', y='Total Bags',
                   title= "\nScatter plot between Average Price and Total Bags", color='green')

plt.show

#The relationship between average price and Total volume is negative and the relationship between Average PRice and total bags is positive
#C. Build a simple regression model (OLS). Use average price as the dependent variable. Include total volume, total bags, type, and year as independent variables. What can you tell from the OLS results?
# import this package to be able to run Ordinary least Square technique
import statsmodels.api as sm

y=avocado[['Total Volume']]
x=avocado[['AveragePrice']]
estimation=sm.OLS(y,x).fit()
print("\n --------OLS between Average Volume and Total Bags--------")
print(estimation.summary())

# To apply OLS between Average Price and Total Bags
# 
y1=avocado[['Total Bags']]
x1=avocado[['AveragePrice']]
estimation=sm.OLS(y1,x1).fit()
print("\n ---------- OLS between Average Price and Total Bags--------")
print(estimation.summary())
#From the Ols ths best fit is when the slope and intercept values minimize the sum of the squared distances, because the relation between Averrage Price
#and total bags is positive, it indicates that the value of the independent variable increase, the mean of the dependent variable will increase as well, vice versa
#for Average price and Total Volume since negative




