
# Energy Efficiency Analysis

Contributors: 

- Mehwish Nabi 
- Yaou Hu 
- Nate Puangpanbut

A project studying relationship among some interested features of
buildings to it's heating load with various types of
buildings. This project is a group study according to DSCI 522 (Data
Science workflows); a course in the Master of Data Science program at
the University of British Columbia, Fall 2022.

## Project proposal

Building towers or any building structure nowadays is not difficult if you can afford it,
but building it to be the most memorable and efficient building is another story.
Considering building new towers or skyscapper buildings, it will great if we know exactly what building parameters relate to its energy efficiency.
We therefore could be able to design not only the magnificent building to remember but an energy efficient building to be renowned.

In this project, we gather simulating data of building heating load versus multiple building features created by Angeliki
Xifara (angxifara '\@' gmail.com, Civil/Structural Engineer) and was
processed by Athanasios Tsanas (tsanasthanasis '\@' gmail.com, Oxford
Centre for Industrial and Applied Mathematics, University of Oxford,
UK), and is made available under the UCI Machine Learning Repository and
can be found
[here](http://archive.ics.uci.edu/ml/datasets/Energy+efficiency#)
specifically [this
file](http://archive.ics.uci.edu/ml/machine-learning-databases/00242/).

The data set contains 12 different building shapes simulated in Ecotect. The buildings differ with respect to the glazing area, the glazing area distribution, and the orientation, amongst other parameters. Simulated various settings as functions of the afore-mentioned characteristics to obtain 768 building shapes. The dataset comprises 768 samples and 8 features, aiming to predict two real valued responses.

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


As a data scientist, we aim to find the relationship or contribution factors of each important
features corresponding to the heating load. We plan to run multiple machine learning model such as,

- KNN

- Ridge

- Decision Tree

- Support Vector Machine

- Random Forest

- XG Boost

then, selecting the best performed model and analyse for the relationship by either extracting model's coeficients, feature
importances, or using other explanatory methods such as
Local-interpretable-model-agnostic-explanations(LIME).

We aim to report both the best model accuracy and its explanation
factors. The matrix of interest now is R2.


## EDA

**Summary of the data set**

This data set contains 768 instances and was donated at 2012-11-30. It
has no missing values. It has a total of 10 variables, with 8 of them
are attributes(features) and two responses. The authors suggested that
the aim of this data set is to use the eight features to predict the two
responses.

**Partition the data set into training and test sub-data sets**

The whole data set were divided into train and test sets, with 70% train
data and 30% test data.

**Exploratory data analysis with the train set**

The exploratory data analysis were conducted through the following
steps: 1.load in the necessary packages and split the data into train
and test sets, NaN were dropped;

2.do EDA on the train set. First to check the data types and see if
there are missing values; we found out that there is no missing value.
Then we proceed to see the data distribution through bar plots,
value_counts, correlations, and pairwise scatter plots. Through the EDA,
we could identify that all the variables are numeric type, but Roof
Area', 'Surface Area', 'Wall Area', 'Overall Height', 'Orientation',
'Glazing Area', and 'Glazing Area Distribution' are actually
categorical.

3.From the above analysis, we may proceed to do a supervised machine
learning model with data preprocessed by Standard Scaling and One Hot
Encode on the numeric features with Heating Load and Cooling Load as the
targets.

The results of the EDA can be found
[here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/src/energy_efficiency_eda.ipynb).

## Report

The final report can be found
[here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/doc/energy_efficiency_report.ipynb).

## Usage

To run this analysis,

1.  Clone this project repository to your local.

```{=html}
    git clone https://github.com/UBC-MDS/energy_efficiency_analysis.git
```

2.  Navigate to your local repository and prompt the command line and
    run,
```
    conda env create --file energy_env.yaml
```

The new environment energy_env will be created in your conda environment, 
and we will use this as the main environment to run the analysis.

3.  Running download data script to download data and convert it to csv file.
```
    python src/download_data.py --url=http://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx --out_file=data/raw/ENB2012_data.csv
```

4.  Running data pre-processing script to perform data pre-processing and saving split train and test data set.
```
    python src/data_preprocess.py data/processed/energy_effeciency_processed.csv data/processed/train_df.csv data/processed/test_df.csv
```

5.  Running EDA script to generate EDA result from train data set.
```
    python src/eda_script_plots_update.py data/processed/train_df.csv results/eda/eda_corr_table.png results/eda/eda_distribution_plot.png results/eda/eda_scatter1_plot.png results/eda/eda_scatter2_plot.png
```

6.  Running model fitting and prediction script to fit model, generate prediction, and save all models as pickle file.
```
    python src/model_predict.py --train_file='data/processed/train_df.csv' --test_file='data/processed/test_df.csv' --out_file1=results/energy_analysis/training_score.png --out_file2=results/energy_analysis/prediction.png
```

7.  Running analysis report script
```
    Rscript -e "rmarkdown::render('doc/energy_report_rmd.Rmd', output_format = 'github_document')"
```

## Dependencies

The Python and Python packages can be found
[here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/energy_env.yaml).

## License

**MIT License** Copyright (c) 2022 Mehwish Nabi, Yaou Hu, Nate
Puangpanbut

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# References

[1] A. Tsanas, A. Xifara: 'Accurate quantitative estimation of energy
performance of residential buildings using statistical machine learning
tools', Energy and Buildings, Vol. 49, pp. 560-567, 2012

[2] Harris, Charles R., K. Jarrod Millman, Stéfan J. van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, et al. 2020. “Array Programming with NumPy.” Nature 585 (7825): 357–62. https://doi.org/10.1038/s41586-020-2649-2.

[3] Pedregosa, F., G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, et al. 2011. “Scikit-Learn: Machine Learning in Python.” Journal of Machine Learning Research 12: 2825–30.

[4] The pandas development. 2020. Pandas-Dev/Pandas: Pandas (version latest). Zenodo. https://doi.org/10.5281/zenodo.3509134.

[5] Tsanas, Athanasios, and Angeliki Xifara. 2012. “Accurate Quantitative Estimation of Energy Performance of Residential Buildings Using Statistical Machine Learning Tools.” Energy and Buildings 49: 560–67.

[6] VanderPlas, Jacob, Brian Granger, Jeffrey Heer, Dominik Moritz, Kanit Wongsuphasawat, Arvind Satyanarayan, Eitan Lees, Ilia Timofeev, Ben Welsh, and Scott Sievert. 2018. “Altair: Interactive Statistical Visualizations for Python.” Journal of Open Source Software 3 (32): 1057.
