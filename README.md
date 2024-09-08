# Honey-Prediction
**Project Overview**

This project aims to predict future trends in honey production in the United States based on historical data. Using a regression model,   honey production is projected to 2050, which shows a noticeable decline over the years.

**Dataset**
The dataset used in this project is historical honey production data in the USA, spanning from the late 1998s up to 2012. The data includes features like:

state: The state where the data was collected.
numcol: The number of colonies producing honey.
yieldpercol: The average yield of honey per colony.
totalprod: The total honey production (in pounds).
stocks: Stocks of honey held by producers (in pounds).
priceperlb: Average price received per pound of honey.
prodvalue: The total value of honey produced.
year: The year of data collection.

**Modeling Approach**
Linear Regression Model: This model is used to predict the total honey production over the years.
Feature Selection: "year" is the main predictor for total honey production.
Prediction: The model projects honey production until 2050 based on the historical trend observed in the dataset.

**Dependencies:**
Python 3.x
Libraries used: pandas, numpy, matplotlib, scikit-learn

Key Results
The model predicts a steady decline in honey production up to 2050. This aligns with concerns about decreasing bee populations and environmental factors impacting honey production.

Current Trend: The model shows a significant downward trend from 1998 to 2012.
Future Prediction: The production is predicted to drop further by 2050.
