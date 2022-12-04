# energy efficiency analysis pipe
# author: Mehwish Nabi, Yaou Hu, Nate Puangpanbut
# date: 2022-11-30

all: data/raw/ENB2012_data.csv data/processed/train_df.csv data/processed/test_df.csv results/eda/eda_corr_table.png results/eda/eda_distribution_plot.png results/eda/eda_scatter1_plot.png results/energy_analysis/training_score.png results/energy_analysis/prediction.png doc/energy_report_rmd.Rmd

# download data
data/raw/ENB2012_data.csv: src/download.py
	python src/download.py http://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx data/raw/ENB2012_data.csv

# data pre-processing (e.g., specify column names and split into train & test)
data/processed/train_df.csv data/processed/test_df.csv: src/data_preprocess.py
	python src/data_preprocess.py data/raw/ENB2012_data.csv data/processed/train_df.csv data/processed/test_df.csv

# exploratory data analysis (visualize histogram, pairwise scatter plots, and correlation coefficient)
results/eda/eda_corr_table.png results/eda/eda_distribution_plot.png results/eda/eda_scatter1_plot.png: src/eda_script_plots_update.py
	python src/eda_script_plots_update.py data/processed/train_df.csv results/eda/eda_corr_table.png results/eda/eda_distribution_plot.png results/eda/eda_scatter1_plot.png

# model predict (evaluate multiple models, select the best model to perform prediction, and save results)
results/energy_analysis/training_score.png results/energy_analysis/prediction.png: src/model_predict.py
	python src/model_predict.py data/processed/train_df.csv data/processed/test_df.csv results/energy_analysis/training_score.png results/energy_analysis/prediction.png

# render report
doc/energy_report_rmd.Rmd: results/eda/eda_corr_table.png results/eda/eda_distribution_plot.png results/eda/eda_scatter1_plot.png results/energy_analysis/training_score.png results/energy_analysis/prediction.png
	Rscript -e "rmarkdown::render('doc/energy_report_rmd.Rmd', output_format = 'github_document')"


clean: 
	rm -rf data/raw/*.csv
	rm -rf data/processed/*.csv
	rm -rf results/eda/*.png
	rm -rf results/energy_analysis/*.png
	rm -rf doc/energy_report_rmd.md doc/energy_report_rmd.html

