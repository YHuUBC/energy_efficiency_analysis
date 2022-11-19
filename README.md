# Energy Efficiency Analysis

Contributors: 
  - Mehwish Nabi
  - Yaou Hu
  - Nate Puangpanbut

A project studying relationship among some interested features of buildings to it's heating and cooling load with various types of buildings.
This project is a group study according to DSCI 522 (Data Science workflows); a
course in the Master of Data Science program at the University of
British Columbia, Fall 2022.

## About

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
specifically [this file](http://archive.ics.uci.edu/ml/machine-learning-databases/00242).

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
?? update from Yaou

## Report

The final report can be found
[here](https://ttimbers.github.io/breast_cancer_predictor/doc/breast_cancer_predict_report.html).
?? need to change url

## Dependencies
?? need to update
 

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



