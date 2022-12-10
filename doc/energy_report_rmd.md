Analysis of the Energy Efficiency Project
================
Mehwish Nabi, Yaou Hu, Nate Puangpanbut at the MDS program of University
of British Columbia

-   [Authors of this project](#authors-of-this-project)
-   [Background information and summary of data
    set](#background-information-and-summary-of-data-set)
-   [Research question](#research-question)
-   [Importance of the research
    question](#importance-of-the-research-question)
-   [Download data](#download-data)
-   [Data pre-processing: partition the data set into training and test
    sub-data
    sets](#data-pre-processing-partition-the-data-set-into-training-and-test-sub-data-sets)
-   [Packages utilized in this
    project](#packages-utilized-in-this-project)
-   [Exploratory data analysis with the train
    set](#exploratory-data-analysis-with-the-train-set)
-   [Modelling and Analysis](#modelling-and-analysis)
-   [Limitations](#limitations)
-   [Assumptions](#assumptions)
-   [Future directions](#future-directions)
-   [References](#references)

## Authors of this project

Mehwish Nabi, Yaou Hu, Nate Puangpanbut at the MDS program of University
of British Columbia

## Background information and summary of data set

The data set used in this project is retrieved from Tsanas and Xifara
(2012). It was contributed by Angeliki Xifara (Civil/Structural
Engineer) and was processed by Athanasios Tsanas (Oxford Centre for
Industrial and Applied Mathematics, University of Oxford, UK). It
contains 768 instances and was donated at 2012-11-30. It has no missing
values. It has a total of 10 variables, with 8 of them are
attributes(features) and two responses. The authors suggested that the
aim of this data set is to use the eight features to predict the two
responses. These variables are shown in the table below:

**Table 1. Variables in the data set**

| variable | description               |
|:---------|:--------------------------|
| X1       | Relative Compactness      |
| X2       | Surface Area              |
| X3       | Wall Area                 |
| X4       | Roof Area                 |
| X5       | Overall Height            |
| X6       | Orientation               |
| X7       | Glazing Area              |
| X8       | Glazing Area Distribution |
| y1       | Heating Load              |
| y2       | Cooling Load              |

## Research question

**Given building-related features such as Relative Compactness’,
‘Surface Area,’ ‘Wall Area,’ ‘Roof Area,’ ‘Overall Height,’
‘Orientation,’ ‘Glazing Area,’ and ‘Glazing Area Distribution,’ how
accurately can we predict the ‘Heating Load’ of the building?**

**What is the contribution level of each feature associated to the
‘Heating Load’ of the building?**

## Importance of the research question

There are growing concerns about energy waste and its detrimental
environmental impact. This project focuses on the energy performance of
residential buildings. Concentrating on eight building-related features
(i.e., Relative Compactness’, ‘Surface Area,’ ‘Wall Area,’ ‘Roof Area,’
‘Overall Height,’ ‘Orientation,’ ‘Glazing Area,’ and ‘Glazing Area
Distribution’), this project aims to predict the ‘Heating Load’ of the
building and examine the contribution level of each feature associated
to the ‘Heating Load’ of the building.

The answers to the above questions are important and meaningful to
residents, residential builders, and society. With the findings of our
project, home-owners and potential home buyers are provided with more
information regarding the energy efficiency of their residential options
to make wiser home choices; residential builders could build more
energy-efficient and environmentally friendly residential building,
which indirectly contribute to the whole society in terms of energy
preservation and environment protection.

## Download data

**NOTE: Data download can be conducted using ‘download.py’ in the
energy\_efficiency\_analysis/src folder with the explanation below:**

‘This code is to download original raw file data from UCI ML databses
and convert it to csv file and finally save to provided destination
folder example : python src/download.py
–url=<http://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx>
–out\_file=data/raw/ENB2012\_data.csv’

## Data pre-processing: partition the data set into training and test sub-data sets

The data set was divided into train and test sets, with 70% train data
and 30% test data.

**NOTE: Data preprocessing can be conducted using ‘data\_preprocess.py’
in the energy\_efficiency\_analysis/src folder with the explanation
below:**

‘This code is to csv data and performs data cleaning, pre-processingm,
then separating into train and test data sets, and finally save to
provided destination folder. example : python src/data\_preprocess.py
data/processed/energy\_effeciency\_processed.csv
data/processed/train\_df.csv data/processed/test\_df.csv’

**Table 2. Partition of the data set**

| cases | subdataset |
|------:|:-----------|
|   537 | Trainset   |
|   231 | Test set   |

## Packages utilized in this project

Pandas(The Pandas Development Team 2020)

Numpy(Harris et al. 2020)

Altair(VanderPlas et al. 2018)

SKlearn(Pedregosa et al. 2011)

## Exploratory data analysis with the train set

The exploratory data analysis was conducted through the following steps:

1.  Load the necessary packages and split the data into train and test
    sets. NaN data were dropped;

2.  EDA was performed on the train set. We checked the data types and
    found no missing values. Then we checked the data distribution
    through bar plots, value\_counts, correlations, and pairwise scatter
    plots. Through the EDA, we could identify that all the variables are
    numeric. We kept all the features for subsequent analysis.

3.  Based on the above analysis, we aim to do a supervised machine
    learning model with ‘Heating Load’ as the target.

**NOTE: Data preprocessing can be conducted using ‘data\_preprocess.py’
in the energy\_efficiency\_analysis/src folder**

**Figure 1. Correlations among the varibles in this study** ![alt
tag](../results/eda/eda_corr_table.png)

**Figure 2. Variable distribution chart** ![alt
tag](../results/eda/eda_distribution_plot.png)

**Figure 3. Scatter plot of variables of interest** ![alt
tag](../results/eda/eda_scatter1_plot.png)

**NOTE: The EDA can be conducted using ‘eda\_script\_plots\_update.py’
in the energy\_efficiency\_analysis/src folder:**

‘This code is to read the train data set and performs explanatory data
analysis and finally save to provided destination folder example :
python src/eda\_script\_plots\_update.py data/processed/train\_df.csv
results/eda/eda\_corr\_table.png results/eda/eda\_distribution\_plot.png
results/eda/eda\_scatter1\_plot.png results/eda/eda\_scatter2\_plot.png’

## Modelling and Analysis

In this analysis, the heat load is predicted using the features Relative
Compactness, Surface Area, Wall Area, Roof Area, Overall Height,
Orientation,Glazing Area, Glazing Area Distribution.

The steps involved are as :

-   loading the train\_df.csv and test\_df.csv dataset created by the
    data\_preprocess.py script

-   the train and test data sets are then splitting the data into
    X\_train and y\_train based on the feature to be predicted i.e ,
    heating load

-   the models are trained on the X\_train and y\_train

-   the models are saved using pickle.

-   Predictions are made on test data using the model that has highest
    cross validation score

The models used for the training and predictions of the data are :

-   KNN

-   Ridge

-   Decision Tree

-   Support Vector Machine

-   Random Forest

-   XG Boost

The training and cross validation scores of the models are in the below
table:

**Figure 4. The training and cross validation scores of the models**
![alt tag](../results/energy_analysis/training_score.png)

As per the cross validation scores the XGB has the highest cross
validation score of 0.998.

The score of Random Forest, Decision Tree and XGB do not have any big
variations and approximately the same.

The training and test scores do not have huge difference so the models
are not overfitting.

The graphical representation of the actual and predicted values in the
test data set by the XGBoost is as below. It can be observed that
predicted values by the model have little to no deviation from the
actual values.

**Figure 5. Comparison of prediction and actual value on test data**
![alt tag](../results/energy_analysis/prediction.png)

**NOTE: The above mentioned modelling and analysis can be conducted
using ‘model\_predict.py’ in the energy\_efficiency\_analysis/src
folder**

’This code is to read the train data set and performs model fitting with
various types of models, select the best model and performs prediction,
finally, saving figures of cv-score comparison and best prediction on
provided destination folder, also, save all models as pickle file to
result/model folder example :

python src/model\_predict.py data/processed/train\_df.csv
data/processed/test\_df.csv results/energy\_analysis/training\_score.png
results/energy\_analysis/prediction.png

## Limitations

This project has certain limitations:

First, the analysis methods utilized in this project are limited to the
authors’ current knowledge. More applicable analysis with a better fit
of this data set might exist.

Second, the data set used for this project was collected around 2012.
New changes may have been made to the energy performance of residential
buildings. Thus, the findings of this project might not be generalizable
to current real-world scenarios.

Third, to the authors’ best knowledge, we do not know where the data
were collected. Locations might be an important factor affecting the
energy performance of residential buildings. Thus, the findings should
be interpreted with caution.

Fourth, there might be other useful features not collected in this data
set, such as the latitude and longitude of the residential building, the
average temperature of where the residential building is located, and
the climate of where the residential building is located.

Fifth, this data set has 768 examples. It could be considered a
relatively large data set, and the authors split it into 70% train set
and 30% test set. However, what the authors did might not be the optimal
way of splitting data.

## Assumptions

This project is based on the assumption that data were collected as
representative of the population and without bias. If this assumption is
violated, the findings of this project might be interpreted with
caution.

## Future directions

Data for this project was collected in 2012. We call for future efforts
to collect recent data on the energy performance of residential
buildings with more features that are relevant to contemporary
residential buildings. We are open to suggestions on a more suitable
model for this project.

# References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-harris2020array" class="csl-entry">

Harris, Charles R., K. Jarrod Millman, Stéfan J. van der Walt, Ralf
Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, et al. 2020.
“Array Programming with NumPy.” *Nature* 585 (7825): 357–62.
<https://doi.org/10.1038/s41586-020-2649-2>.

</div>

<div id="ref-scikit-learn" class="csl-entry">

Pedregosa, F., G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O.
Grisel, M. Blondel, et al. 2011. “Scikit-Learn: Machine Learning in
Python.” *Journal of Machine Learning Research* 12: 2825–30.

</div>

<div id="ref-reback2020pandas" class="csl-entry">

The Pandas Development Team. 2020. *Pandas-Dev/Pandas: Pandas* (version
latest). Zenodo. <https://doi.org/10.5281/zenodo.3509134>.

</div>

<div id="ref-vanderplas2018altair" class="csl-entry">

VanderPlas, Jacob, Brian Granger, Jeffrey Heer, Dominik Moritz, Kanit
Wongsuphasawat, Arvind Satyanarayan, Eitan Lees, Ilia Timofeev, Ben
Welsh, and Scott Sievert. 2018. “Altair: Interactive Statistical
Visualizations for Python.” *Journal of Open Source Software* 3 (32):
1057.

</div>

</div>
