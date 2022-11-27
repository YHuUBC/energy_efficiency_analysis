
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

Building towers or any building structure nowadays is not difficult if you can afford it,
But building it to be the most memorable and efficient is another story.
When considering building new towers or skyscraper buildings, it will be great if we know exactly what building parameters relate to their energy efficiency.As a result, we would be able to design not only a magnificent building to remember, but also a renowned energy-efficient building. 

In this project, we gather simulating data of building heating load versus multiple building features created by Angeliki
Xifara (angxifara '\@' gmail.com, Civil/Structural Engineer) and was
processed by Athanasios Tsanas (tsanasthanasis '\@' gmail.com, Oxford
Centre for Industrial and Applied Mathematics, University of Oxford,
UK), and is made available under the UCI Machine Learning Repository and
can be found
[here](http://archive.ics.uci.edu/ml/datasets/Energy+efficiency#)
specifically [this
file](http://archive.ics.uci.edu/ml/machine-learning-databases/00242/).

The data set contains 12 different building shapes simulated in Ecotect. The buildings differ in the glazing area, the glazing area distribution, and the orientation, amongst other parameters. Various settings were simulated as functions of the aforementioned characteristics to obtain 768 building shapes. The  data set comprises 768 samples and eight features, aiming to predict two real-valued responses.

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


**Research question**

Given building-related features such as Relative Compactness', 'Surface Area', 'Wall Area', 'Roof Area', 'Overall Height', 'Orientation', 'Glazing Area', and 'Glazing Area Distribution', how accurately can we predict the 'Heating Load' of the building? What contribution level of each feature to the 'Heating Load' of the building?

<!-- #region -->
## EDA


**Partition the data set into training and test sub-data sets**

The data set was divided into train and test sets, with 70% train data and 30% test data.

**Exploratory data analysis with the train set**

The exploratory data analysis was conducted through the following steps:

1. Load in the necessary packages and split the data into train and test sets. NaNs data were dropped;

2. Do EDA on the train set. First, we checked the data types to see if there were any missing values, and there were none. Then we see the data distribution through bar plots, value_counts, correlations, and pairwise scatter plots. Through the EDA, we could identify that all the variables are numeric.

3. From the above analysis, we may proceed to do a supervised machine learning model with data preprocessed by Standard Scaling as the numeric features with Heating Load as target.

The results of the EDA can be found
[here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/results/eda/energy_efficiency_eda.ipynb).

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
[here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/doc/energy_report_rmd.Rmd). An alternative ipynb file can be found [here](https://github.com/UBC-MDS/energy_efficiency_analysis/blob/main/doc/energy_efficiency_report.ipynb).

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

In your conda environment, a new environment called energy_env will be created.
and we will use this as the main environment to run the analysis.

3.  Running download data script to download data and convert it to csv file.
```
    python src/download_data.py --url=http://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx --out_file=data/raw/ENB2012_data.csv
```

4.  Running data pre-processing script to perform data pre-processing and save split train and test data sets.
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

# References

[1] A. Tsanas, A. Xifara: 'Accurate quantitative estimation of energy
performance of residential buildings using statistical machine learning
tools', Energy and Buildings, Vol. 49, pp. 560-567, 2012

[2] Harris, Charles R., K. Jarrod Millman, Stéfan J. van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, et al. 2020. “Array Programming with NumPy.” Nature 585 (7825): 357–62. https://doi.org/10.1038/s41586-020-2649-2.

[3] Pedregosa, F., G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, et al. 2011. “Scikit-Learn: Machine Learning in Python.” Journal of Machine Learning Research 12: 2825–30.

[4] The pandas development. 2020. Pandas-Dev/Pandas: Pandas (version latest). Zenodo. https://doi.org/10.5281/zenodo.3509134.

[5] Tsanas, Athanasios, and Angeliki Xifara. 2012. “Accurate Quantitative Estimation of Energy Performance of Residential Buildings Using Statistical Machine Learning Tools.” Energy and Buildings 49: 560–67.

[6] VanderPlas, Jacob, Brian Granger, Jeffrey Heer, Dominik Moritz, Kanit Wongsuphasawat, Arvind Satyanarayan, Eitan Lees, Ilia Timofeev, Ben Welsh, and Scott Sievert. 2018. “Altair: Interactive Statistical Visualizations for Python.” Journal of Open Source Software 3 (32): 1057.
<!-- #endregion -->

```python

```
