
# Energy Efficiency Analysis

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


## EDA


**Partition the data set into training and test sub-data sets**

The data set was divided into train and test sets, with 70% train data and 30% test data.

**Exploratory data analysis with the train set**

The exploratory data analysis was conducted through the following steps:

1. Load the necessary packages and split the data into train and test sets. NaN data were dropped;

2. EDA was performed on the train set. We checked the data types and found no missing values. Then we checked the data distribution through bar plots, value_counts, correlations, and pairwise scatter plots. Through the EDA, we could identify that all the variables are numeric. We kept all the features for subsequent analysis.

3. Based on the above analysis, we aim to do a supervised machine learning model with ‘Heating Load’ as the target.


The results of the EDA can be found
[here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/results/eda/energy_efficiency_eda.ipynb).


## Report

The final report can be found
[here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/doc/energy_report_rmd.Rmd). An alternative ipynb file can be found [here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/doc/energy_efficiency_report.ipynb).


## Usage

To replicate the analysis, clone this GitHub repository to your local:
```
git clone https://github.com/UBC-MDS/energy_efficiency_analysis.git
```

Navigate to your local repository and prompt the command line and run:
```
conda env create --file energy_project.yaml
```
The new environment energy_project will be created in your conda environment, and we will use this as the main environment to run the analysis.

Activate the new environment by:
```
conda activate energy_project
```

To reset the repo to a clean state, with no intermediate or results files, run the following command at the command line/terminal from the root directory of this project:
```
make clean
```

To replicate all of the analysis, run the following command at the command line/terminal from the root directory of this project:
```
make all
```


## Dependencies

The Python and Python packages can be found
[here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/energy_project.yaml).

## License

**MIT License** Copyright (c) 2022 Mehwish Nabi, Yaou Hu, Nate
Puangpanbut

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation, the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the software, and to
allow those to whom the software is provided to do so, subject to
the following conditions:
The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the software.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT ANY EXPRESS OR IMPLIED WARRANTY.INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE

## References

[1] Harris, Charles R., K. Jarrod Millman, Stéfan J. van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, et al. 2020. “Array Programming with NumPy.” Nature 585 (7825): 357–62. https://doi.org/10.1038/s41586-020-2649-2.

[2] Pedregosa, F., G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, et al. 2011. “Scikit-Learn: Machine Learning in Python.” Journal of Machine Learning Research 12: 2825–30.

[3] The pandas development. 2020. Pandas-Dev/Pandas: Pandas (version latest). Zenodo. https://doi.org/10.5281/zenodo.3509134.

[4] Tsanas, Athanasios, and Angeliki Xifara. 2012. “Accurate Quantitative Estimation of Energy Performance of Residential Buildings Using Statistical Machine Learning Tools.” Energy and Buildings 49: 560–67.

[5] VanderPlas, Jacob, Brian Granger, Jeffrey Heer, Dominik Moritz, Kanit Wongsuphasawat, Arvind Satyanarayan, Eitan Lees, Ilia Timofeev, Ben Welsh, and Scott Sievert. 2018. “Altair: Interactive Statistical Visualizations for Python.” Journal of Open Source Software 3 (32): 1057.
<!-- #endregion -->

