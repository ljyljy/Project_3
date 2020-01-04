# Zillow Prize: Zillow’s Home Value Prediction (Zestimate)
## Can you improve the algorithm that changed the world of real estate?

## Data sources

From kaggle competition: https://www.kaggle.com/c/zillow-prize-1

## Data clean

1. Add different features based on existed data: feature_adding.ipynb
Potential features adding: 
life of property, Ratio of tax of property over parcel, Number of properties in the zip, 
error in calculation of the finished living area of home, proportion of living area calculated or real,
Amout of extra space, Total number of rooms, Average room size, Number of Extra rooms,
Ratio of the built structure value to land area, Does property have a garage, pool or hot tub and AC?
TotalTaxScore, polnomials of tax delinquency year, Length of time since unpaid taxes,
Number of properties in the city, Indicator whether it has AC or not, Indicator whether it has Heating or not, 
There's 25 different property uses - let's compress them down to 4 categories, polnomials of the variable,
Average structuretaxvaluedollarcnt by city, Deviation away from average

Select the important features by testing the model accuracy using light GBM
Four features are added finally: 'N-life', 'N-ValueRatio', 'N-zip_count', 'N-Avg-structuretaxvaluedollarcnt'

2. Missing value filling: Missing_value.ipnb
 * Using description to fill several missing value (missing values mean 0)

 * For geographical factors, using KNN with location information to fill in missing values

3. feature selection: feature_selection.ipynb
* Delete features having more than 95% missing value or having equal values.

* Using feature importance to decide whether features are necessary to delete by model accuracy using light GBM

* Using VIF to decide

* Using correlation to decide (if 2 features R2 are more than 0.5)

4. Using darksky to collect all location information to find the temperature in January and Auguest.
weather_collect.ipynb

5. merge and make submission. merge_data.ipynb and submission_making.ipynb

## Machine Learning models:

Light GBM, Xgboost, neural network, Catboost

Submit the results to kaggle to evaluate models

## Design a web to present.

## Use my personal computer to run