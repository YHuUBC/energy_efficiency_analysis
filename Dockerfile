# Docker image for Energy efficiency analysis project
# Date: Dec 10, 2022

# Base
FROM continuumio/miniconda3:4.12.0

# Install Python
RUN conda install -y python=3.10

# Add conda-forge channel 
RUN conda config --append channels conda-forge

# Conda Installs
RUN conda install -y ipykernel
RUN conda install -y matplotlib>=3.2.2
RUN conda install -y scikit-learn>=1.1.3
RUN conda install -y requests>=2.24.0
RUN conda install -y graphviz
RUN conda install -y python-graphviz
RUN conda install -y eli5
RUN conda install -y shap
RUN conda install -y jinja2
RUN conda install -y altair
RUN conda install -y altair_saver
RUN conda install -y selenium==4.3.0
RUN conda install -y pandas
RUN conda install -y imbalanced-learn
RUN conda install -y numpy
RUN conda install -y pandoc

# install Pip   
RUN apt-get update && apt-get install -y pip

# pip 
RUN pip install joblib==1.1.0
RUN pip install mglearn
RUN pip install psutil>=5.7.2
RUN pip install docopt
RUN pip install requests
RUN pip install vl-convert-python
RUN pip install dataframe-image
RUN pip install xgboost
RUN pip install ipython
RUN pip install openpyxl
RUN pip install portpicker

# install R
RUN apt-get install r-base r-base-dev -y

# install non R tidyverse dependencies??
RUN apt-get update && apt-get install -y libcurl4-openssl-dev libssl-dev libxml2-dev

# R packages 
RUN R -q -e 'install.packages("tidyverse")'
RUN R -q -e 'install.packages("rmarkdown")'

# install Make
RUN apt update && apt install -y make

# # Docker image for Energy efficiency analysis project
# # Date: Dec 10, 2022

# FROM continuumio/miniconda3

# RUN conda install python=3.10.8 -y

# RUN conda install pandas=1.4.4 -y
# RUN conda install scikit-learn=1.1.3 -y
# RUN conda install matplotlib=3.6.2 -y
# RUN conda install -c conda-forge altair vega_datasets
# RUN conda install requests=2.28.1
# RUN conda install python-graphviz
# RUN conda install pandoc

# RUN pip install xgboost==1.7.1
# RUN pip install docopt
# RUN pip install dataframe-image
# RUN pip install openpyxl==3.0.10
# RUN pip install ipython
# RUN pip install altair-saver
# RUN python -m pip install vl-convert-python

# RUN apt-get update && apt-get install make

# # install R
# RUN apt-get install r-base r-base-dev -y

# # install non R tidyverse dependencies
# RUN apt-get update && apt-get install -y libcurl4-openssl-dev libssl-dev libxml2-dev

# # install R packages 
# RUN R -q -e 'install.packages("tidyverse")'
# RUN R -q -e 'install.packages("rmarkdown")'

