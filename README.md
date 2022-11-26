# Energy Efficiency Analysis

Contributors: 
  - Mehwish Nabi
  - Yaou Hu
  - Nate Puangpanbut

A project studying relationship among some interested features of buildings to it's heating and cooling load with various types of buildings.
This project is a group study according to DSCI 522 (Data Science workflows); a
course in the Master of Data Science program at the University of
British Columbia, Fall 2022.

## Project proposal

In this project, we attemp to find important parameters of building that affect to the heating and cooling load.
We plan to build a number of different regression models such as 
- Linear regression (Ridge, Lasso)
- Support vector machine
- Decision tree
- Xgboost
- etc ..
to predict heating and cooling load.

We then aim to find the relationship or contribution of each important features to the response
by extracting model's coeficients, feature importants, or using other explanatory methods
such as Local-interpretable-model-agnostic-explanations(LIME).

We aim to report both the best model accuracy and its explanation factors.
The matrix of interest now is Mean absolute error, MAE.

The data set that was used in this project was created by Angeliki Xifara (angxifara '@' gmail.com, Civil/Structural Engineer) 
and was processed by Athanasios Tsanas (tsanasthanasis '@' gmail.com, 
Oxford Centre for Industrial and Applied Mathematics, University of Oxford, UK), 
and is made available under the UCI Machine Learning Repository and can be found
[here](http://archive.ics.uci.edu/ml/datasets/Energy+efficiency#)
specifically [this file](http://archive.ics.uci.edu/ml/machine-learning-databases/00242/).

Each row in the data set represents interested features of building heating and cooling load 
from the afore-mentioned characteristics simulation (e.g., Relative Compactness, Surface Area, Wall Area, etc..),
including the response (e.g., Heating Load, Cooling Load).

Specifically:

X1 Relative Compactness

X2 Surface Area

X3 Wall Area

X4 Roof Area

X5 Overall Height

X6 Orientation

X7 Glazing Area

X8 Glazing Area Distribution

y1 Heating Load

y2 Cooling Load

## EDA
**Summary of the data set**

This data set contains 768 instances and was donated at 2012-11-30. It has no missing values. It has a total of 10 variables, with 8 of them are attributes(features) and two responses. The authors suggested that the aim of this data set is to use the eight features to predict the two responses. 

**Partition the data set into training and test sub-data sets**

The whole data set were divided into train and test sets, with 70% train data and 30% test data. 

**Exploratory data analysis with the train set**

The exploratory data analysis were conducted through the following steps:
1.load in the necessary packages and split the data into train and test sets, NaN were dropped;

2.do EDA on the train set. First to check the data types and see if there are missing values; we found out that there is no missing value. Then we proceed to see the data distribution through bar plots, value_counts, correlations, and pairwise scatter plots. Through the EDA, we could identify that all the variables are numeric type, but Roof Area', 'Surface Area', 'Wall Area', 'Overall Height', 'Orientation', 'Glazing Area', and 'Glazing Area Distribution' are actually categorical.

3.From the above analysis, we may proceed to do a supervised machine learning model with data preprocessed by Standard Scaling and One Hot Encode on the numeric features with Heating Load and Cooling Load as the targets.

The results of the EDA can be found [here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/src/energy_efficiency_eda.ipynb).

## Report

The final report can be found
[here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/doc/energy_efficiency_report.ipynb).

## Usage

To run this analysis, clone this project repository to your local,
prompt the command line and change directory to the project folder,
and run, 

    conda env create --file env-dsci-573.yaml

The new environment env-dsci-573 will be created in your conda environment,
and we will use this as the main environment to run the analysis.

## Dependencies

The Python and Python packages can be found
[here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/energy_env.yaml).

## License

**MIT License**
Copyright (c) 2022 Mehwish Nabi, Yaou Hu, Nate Puangpanbut

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# References

[1] A. Tsanas, A. Xifara: 'Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools', Energy and Buildings, Vol. 49, pp. 560-567, 2012
