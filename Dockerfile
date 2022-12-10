# Docker image for Energy efficiency analysis project
# Date: Dec 10, 2022

FROM continuumio/miniconda3

RUN conda install python=3.10.8 -y

RUN conda install pandas=1.4.4 -y
RUN conda install scikit-learn=1.1.3 -y
RUN conda install matplotlib=3.6.2 -y
RUN conda install -c conda-forge altair vega_datasets
RUN conda install requests=2.28.1
RUN conda install python-graphviz
RUN conda install pandoc

RUN pip install xgboost==1.7.1
RUN pip install docopt
RUN pip install dataframe-image
RUN pip install openpyxl==3.0.10
RUN pip install ipython
RUN pip install altair-saver
RUN python -m pip install vl-convert-python

RUN apt-get update && apt-get install make

# install R
RUN apt-get install r-base r-base-dev -y

# install non R tidyverse dependencies
RUN apt-get update && apt-get install -y libcurl4-openssl-dev libssl-dev libxml2-dev

# install R packages 
RUN R -q -e 'install.packages("tidyverse")'
RUN R -q -e 'install.packages("rmarkdown")'

