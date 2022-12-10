# Research Proposal of Energy Efficiency Analysis

Contributors: 

- Mehwish Nabi 
- Yaou Hu 
- Nate Puangpanbut

A project to predict the heating load of various types of
buildings and to investigate the role of features in heating load prediction. This project is a group study according to DSCI 522 (Data
Science workflows); a course in the Master of Data Science program at
the University of British Columbia, Fall 2022.

## Project proposal

Building towers or any building structure nowadays is not difficult if you can afford it, but building it to be the most memorable and efficient is another story. When considering building new towers or skyscraper buildings, it will be great if we know exactly what building parameters relate to their energy efficiency. As a result, we would be able to design not only a magnificent building to remember but also a renowned energy-efficient building. 

In this project, we gather simulating data of building heating load versus multiple building features created by Angeliki
Xifara (angxifara@gmail.com, Civil/Structural Engineer) and was
processed by Athanasios Tsanas (tsanasthanasis@gmail.com, Oxford
Centre for Industrial and Applied Mathematics, University of Oxford,
UK), and is made available under the UCI Machine Learning Repository and
can be found
[here](http://archive.ics.uci.edu/ml/datasets/Energy+efficiency#)
specifically [this
file](http://archive.ics.uci.edu/ml/machine-learning-databases/00242/).

The data set contains 12 different building shapes simulated in Ecotect. The buildings differ in the glazing area, the glazing area distribution, and the orientation, amongst other parameters. Various settings were simulated as functions of the aforementioned characteristics to obtain 768 building shapes. The  data set comprises 768 samples and eight features.

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


## Research question

Given building-related features such as Relative Compactness', 'Surface Area', 'Wall Area', 'Roof Area', 'Overall Height', 'Orientation', 'Glazing Area', and 'Glazing Area Distribution', how accurately can we predict the 'Heating Load' of the building? And to check contribution level of each feature to the 'Heating Load' of the building.

<!-- #region -->
## Analysis

We split the data set into train and test data sets with 70:30 ratio. An EDA is performed to reveal the distribution and relationship among the features to the response. The result of EDA and its correlation coefficient map is analyzed to reduce some unnecessary features. The modeling fitting is performed with various types of models such as
- KNN
- Ridge
- Decision Tree
- Support Vector Machine
- Random Forest
- XG Boost

Each model is fitted with the same transformation and pipeline and is reported as the mean and standard deviation of the cross-validation score. The best cross-validation score model is selected to be the final model to perform prediction on test data to see how it fits and performs. Finally, all the models are saved as pickled files.


## Report

The final report can be found
[here](doc/energy_report_rmd.md).