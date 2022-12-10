# Docker image for Energy efficiency analysis project
# Date: Dec 10, 2022

# FROM jupyter/scipy-notebook:85f615d5cafa

FROM continuumio/miniconda3

RUN conda install python=3.10.8
RUN conda scikit-learn>=1.1.3
RUN conda requests>=2.24.0

RUN pip install altair-saver
RUN pip install altair-saver



