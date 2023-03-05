# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:52:18 2023

@author: Administrator
"""

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read csv files
df_aus = pd.read_csv("Australia_agriculture.csv")
print(df_aus.head())
df_uk = pd.read_csv("United Kingdon_agriculture.csv")
print(df_uk.head())
df_china = pd.read_csv("China_agriculture.csv")

# Question 01
# Create line chart function


def plot_linechart():
    """
    A function to create line chart Parameters
    one parameter: df_aus
    df_aus : Object
            Agriculture contribution for annual growth from 2007 to 2016 
            Agriculture contribution fo GDP 2007 to 2016 
    """
    # plot line chart
    plt.figure()
    plt.plot(df_aus["Year"], df_aus["Agriculture, value added (annual % growth)"],
             label="Annual growth (%)", marker="o", color="black")
    plt.plot(df_aus["Year"], df_aus["Agriculture, value added (% of GDP)"],
             label="Gross Domestic Product(GDP)(%)", marker="o", color="red")

    plt.xlabel("Year", fontweight="bold")
    plt.ylabel("Percentage(%)", fontweight="bold")
    plt.title("Contribution of Agriculture ", fontweight="bold")
    plt.legend()

    # Save Chart
    plt.savefig("line_chart.png")
    plt.show()


# call line chart function
plot_linechart()
# Question 02

# create bar chart function


def Bar_Chart_Plot():
    """
    A function to create Bar chart Parameters
    Three parameter: df_aus, df_china, df_uk
    df_aus : Object
            Agriculture contribution fo GDP from 2007 to 2016
    df_china : Object
            Agriculture contribution fo GDP from 2007 to 2016
    df_uk : Object
            Agriculture contribution fo GDP from 2007 to 2016

    """

    # plot bar chart
    plt.figure()

    plt.bar(df_aus["Country"],
            df_aus["Agriculture, value added (% of GDP)"], width=0.8, color="red")

    plt.bar(df_china["Country"],
            df_china["Agriculture, value added (% of GDP)"], width=0.8,  color="blue")

    plt.bar(df_uk["Country"],
            df_uk["Agriculture, value added (% of GDP)"], width=0.8,  color="green")

    plt.xlabel("Country", fontweight="bold")
    plt.ylabel("Percentage(%)", fontweight="bold")
    plt.title("The Percentage of Agriculture Contribution", fontweight="bold")
    plt.legend()

    # Save Chart
    plt.savefig("bar_chart.png")
    plt.show()


# call bar chart function
Bar_Chart_Plot()

# create scatter plot function


def Scatter_Plot():
    """
    A function to create scatter chart Parameters
    Two parameter: df_aus, df_china
    df_china : Object
            Agriculture contribution fo annual growth from 2007 to 2016
    df_aus : Object
            Agriculture contribution fo annual growth from  2007 to 2016

    """

    # plot scatter chart
    plt.figure()
    plt.scatter(df_china["Year"], df_china["Agriculture, value added (annual % growth)"],
                label='Annual growth', color='purple')
    plt.scatter(df_aus["Year"], df_aus["Agriculture, value added (% of GDP)"],
                label='Gross Domestic Product(GDP)', color='red')

    plt.xlabel("Year", fontweight="bold")
    plt.ylabel("Percentage(%)", fontweight="bold")
    plt.title("Agriculture Contribution", fontweight="bold")
    plt.legend()

    # Save scatter chart
    plt.savefig("scatter_plot.png")
    plt.show()


# Call scatter plot function
Scatter_Plot()

# create boc chart function


def Box_Chart_Plot():
    """
    A function to create Box chart Parameters
    Three parameter: df_aus, df_uk, df_china
    country : Object
            Australia, Uk, China
    df_china : Object
            Agriculture contribution fo annual growth from 2007 to 2016
    df_aus : Object
            Agriculture contribution fo annual growth from  2007 to 2016
    df_aus : Object
            Agriculture contribution fo annual growth from  2007 to 2016

    """

    # create dataframes for box chart
    country = ["Australia", "UK", "China"]
    category = [df_aus["Agriculture, value added (annual % growth)"], df_uk["Agriculture, value added (annual % growth)"],
                df_china["Agriculture, value added (annual % growth)"]]
    print(category)

    # plot box chart
    plt.figure()

    plt.boxplot(category, labels=country)

    plt.xlabel("Country", fontweight="bold")
    plt.ylabel("Percentage(%)", fontweight="bold")
    plt.title("Annual Growth of Agriculture", fontweight="bold")
    plt.legend()

    # Save boxplot
    plt.savefig("box_plot.png")
    plt.show()


# call boxplot function
Box_Chart_Plot()
