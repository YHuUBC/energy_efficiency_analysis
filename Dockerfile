# Docker image for Energy efficiency analysis project
# Date: Dec 10, 2022

# Base
FROM continuumio/miniconda3:4.12.0

# Install Python
RUN conda install -y python=3.10

# Add conda-forge channel 
RUN conda config --append channels conda-forge

# Conda Installs
RUN conda install -y\
    ipykernel \
    matplotlib>=3.2.2 \
    scikit-learn>=1.1.3 \
    requests>=2.24.0 \
    graphviz \
    python-graphviz \
    eli5 \
    shap \
    jinja2 \
    altair \
    altair_saver \
    selenium==4.3.0 \
    pandas<1.5 \
    imbalanced-learn \
    numpy \
    pandoc \

# install Pip   
RUN apt-get update && apt-get install -y pip

# pip Installs
RUN pip install \
    joblib==1.1.0 \
    mglearn \
    psutil>=5.7.2 \
    docopt \
    requests \
    vl-convert-python \
    dataframe-image \
    xgboost \
    ipython \
    openpyxl \

# install R
RUN apt-get install r-base r-base-dev -y

# install non R tidyverse dependencies??
RUN apt-get update && apt-get install -y libcurl4-openssl-dev libssl-dev libxml2-dev

# R packages 
RUN R -q -e 'install.packages("tidyverse")'
RUN R -q -e 'install.packages("rmarkdown")'

# install Make
RUN apt update && apt install -y make
