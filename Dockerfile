# Docker image for Energy efficiency analysis project
# Date: Dec 10, 2022

# FROM jupyter/scipy-notebook:85f615d5cafa

FROM continuumio/miniconda3

RUN conda install python=3.10.8
RUN conda scikit-learn
RUN conda requests

RUN conda install -c conda-forge xgboost
RUN conda install -c conda-forge lightgbm
RUN conda install -c conda-forge catboost

RUN pip install altair
RUN pip install altair-saver





