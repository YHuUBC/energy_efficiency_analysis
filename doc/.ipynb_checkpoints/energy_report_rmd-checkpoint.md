Analysis of the Energy Efficiency Project
================

- <a href="#summary-of-the-data-set"
  id="toc-summary-of-the-data-set">Summary of the data set</a>
- <a href="#download-data" id="toc-download-data">Download data</a>
- <a
  href="#data-pre-processing-partition-the-data-set-into-training-and-test-sub-data-sets"
  id="toc-data-pre-processing-partition-the-data-set-into-training-and-test-sub-data-sets">Data
  pre-processing: partition the data set into training and test sub-data
  sets</a>
- <a href="#packages-utilized-in-this-project"
  id="toc-packages-utilized-in-this-project">Packages utilized in this
  project</a>
- <a href="#exploratory-data-analysis-with-the-train-set"
  id="toc-exploratory-data-analysis-with-the-train-set">Exploratory data
  analysis with the train set</a>
- <a href="#modelling-and-analysis"
  id="toc-modelling-and-analysis">Modelling and Analysis</a>
- <a href="#limitations" id="toc-limitations">Limitations</a>
- <a href="#assumptions" id="toc-assumptions">Assumptions</a>
- <a href="#future-directions" id="toc-future-directions">Future
  directions</a>
- <a href="#references" id="toc-references">References</a>

## Summary of the data set

The data set used in this project is retrieved from (Tsanas and Xifara
2012). It was contributed by Angeliki Xifara (angxifara ‘@’ gmail.com,
Civil/Structural Engineer) and was processed by Athanasios Tsanas
(tsanasthanasis ‘@’ gmail.com, Oxford Centre for Industrial and Applied
Mathematics, University of Oxford, UK). It contains 768 instances and
was donated at 2012-11-30. It has no missing values. It has a total of
10 variables, with 8 of them are attributes(features) and two responses.
The authors suggested that the aim of this data set is to use the eight
features to predict the two responses. These variables are shown in the
table below:

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

Table 1. Variables in the data set

## Download data

**NOTE: Data download can be conducted using ‘download_data.py’ in the
energy_efficiency_analysis/src folder with the explanation below:**

‘This code is to download original raw file data from UCI ML databses
and convert it to csv file and finally save to provided destination
folder example : python src/download_data.py
–url=<http://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx>
–out_file=data/raw/ENB2012_data.csv’

## Data pre-processing: partition the data set into training and test sub-data sets

The whole data set were divided into train and test sets, with 70% train
data and 30% test data.

**NOTE: Data preprocessing can be conducted using ‘data_preprocess.py’
in the energy_efficiency_analysis/src folder with the explanation
below:**

‘This code is to csv data and performs data cleaning, pre-processingm,
then separating into train and test data sets, and finally save to
provided destination folder. example : python src/data_preprocess.py
data/processed/energy_effeciency_processed.csv
data/processed/train_df.csv data/processed/test_df.csv’

| cases | subdataset |
|------:|:-----------|
|   537 | Trainset   |
|   231 | Test set   |

Table 2. Partition of the data set

## Packages utilized in this project

Pandas(team 2020)

Numpy(Harris et al. 2020)

Altair(VanderPlas et al. 2018)

SKlearn(Pedregosa et al. 2011)

## Exploratory data analysis with the train set

The exploratory data analysis were conducted through the following
steps:

1.load in the necessary packages and split the data into train and test
sets, NaN were dropped;

2.do EDA on the train set. First to check the data types and see if
there are missing values; we found out that there is no missing value.
Then we proceed to see the data distribution through bar plots,
value_counts, correlations, and pairwise scatter plots. Through the EDA,
we could identify that all the variables are numeric type, but Roof
Area’, ‘Surface Area’, ‘Wall Area’, ‘Overall Height’, ‘Orientation’,
‘Glazing Area’, and ‘Glazing Area Distribution’ are actually
categorical.

3.From the above analysis, we may proceed to do a supervised machine
learning model with Heating Load and/or Cooling Load as the targets.

Isles: ![alt tag](../results/eda/eda_corr_table.png)

Isles: ![alt tag](../results/eda/eda_distribution_plot.png) Isles: ![alt
tag](../results/eda/eda_scatter1_plot.png)

**NOTE: The EDA can be conducted using ‘eda_script_plots_update.py’ in
the energy_efficiency_analysis/src folder:**

‘This code is to read the train data set and performs explanatory data
analysis and finally save to provided destination folder example :
python src/eda_script_plots_update.py data/processed/train_df.csv
results/eda/eda_corr_table.png results/eda/eda_distribution_plot.png
results/eda/eda_scatter1_plot.png results/eda/eda_scatter2_plot.png’

## Modelling and Analysis

In this analysis, the heat load is predicted using the features Relative
Compactness, Surface Area, Wall Area, Roof Area, Overall Height,
Orientation,Glazing Area, Glazing Area Distribution.

The steps involved are as : - loading the train_df.csv and test_df.csv
dataset created by the data_preprocess.py script - the train and test
data sets are then splitting the data into X_train and y_train based on
the feature to be predicted i.e , heating load - the models are trained
on the X_train and y_train - the models are saved using pickle. -
Predictions are made on test data using the model that has highest cross
validation score

The models used for the training and predictions of the data are : -
KNN - Ridge - Decision Tree - Support Vector Machine - Random Forest -
XG Boost

The training and cross validation scores of the models are in the below
table:

Isles: ![alt tag](../results/energy_analysis/training_score.png)

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

Isles: ![alt tag](../results/energy_analysis/prediction.png)

**NOTE: The above mentioned modelling and analysis can be conducted
using ‘model_predict.py’ in the energy_efficiency_analysis/src folder**

‘This code is to read the train data set and performs model fitting with
various types of models, select the best model and performs prediction,
finally, saving figures of cv-score comparision and best prediction on
privided destination folder, also, save all modles as pickle file to
result/model folder example : python src/model_predict.py
–train_file=’data/processed/train_df.csv’
–test_file=‘data/processed/test_df.csv’
–out_file1=results/energy_analysis/training_score.png
–out_file2=results/energy_analysis/prediction.png’

## Limitations

This project has certain limitations:

First, the analysis methods utilized in this project are limited to the
authors’ current knowledge. More applicable analysis that with better
fit of this data set might exist.

Second, the data set used for this project was collected around the year
2012. New changes may have been made on the energy performance of
residential buildings. Thus, findings of this project might not be
generalizable to current real_world scenarios.

Third, to the authors’ best knowledge, we do not know where the data
were collected. Locations might be an important factor affecting the
energy performance of residential buildings. Thus, the findings should
be interpreted with caution. Fourth, there might be other useful
features but not collected in this data set such as latitude and
longitude of the residential building, the average temperature of where
the residential building is located, and the climate of where the
residential building is located.

Fifth, this data set has 768 examples. It could be considered as a
relatively large data set and the authors split the data set into 70%
train set and 30% test set. This might not be the optimal way of
splitting data.

## Assumptions

This project is based on the assumption that data were collected as
representative of the population and without bias. If this assumption is
violated, findings of this project might be interpreted with caution.

## Future directions

Data of this project was collected in 2012. We call for future efforts
to collect recent data on the energy performance of residential
buildings with more features that are relevant to contemporary
residential buildings. We are open to any suggestions on a more suitable
model of this project.

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

team, The pandas development. 2020. *Pandas-Dev/Pandas: Pandas* (version
latest). Zenodo. <https://doi.org/10.5281/zenodo.3509134>.

</div>

<div id="ref-tsanas2012accurate" class="csl-entry">

Tsanas, Athanasios, and Angeliki Xifara. 2012. “Accurate Quantitative
Estimation of Energy Performance of Residential Buildings Using
Statistical Machine Learning Tools.” *Energy and Buildings* 49: 560–67.

</div>

<div id="ref-vanderplas2018altair" class="csl-entry">

VanderPlas, Jacob, Brian Granger, Jeffrey Heer, Dominik Moritz, Kanit
Wongsuphasawat, Arvind Satyanarayan, Eitan Lees, Ilia Timofeev, Ben
Welsh, and Scott Sievert. 2018. “Altair: Interactive Statistical
Visualizations for Python.” *Journal of Open Source Software* 3 (32):
1057.

</div>

</div>
