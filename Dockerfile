# Docker image for Energy efficiency analysis project
# Date: Dec 10, 2022

# FROM jupyter/scipy-notebook:85f615d5cafa

FROM continuumio/miniconda3

RUN conda install python=3.10.8
RUN pip install -U scikit-learn
RUN conda install requests

RUN conda install -c conda-forge xgboost
RUN conda install -c conda-forge lightgbm
RUN conda install -c conda-forge catboost

RUN conda install -c conda-forge eli5
RUN pip install shap

RUN pip install altair
RUN pip install altair-saver

RUN pip install pandas
RUN pip install numpy
RUN conda install pandoc
RUN pip install docopt
RUN pip install openpyxl
RUN pip install dataframe-image
RUN pip install vl-convert-python==0.4.0
RUN pip install joblib==1.1.0




