# Docker image for Energy efficiency analysis project
# Date: Dec 10, 2022

FROM continuumio/miniconda3

RUN conda install python=3.10.8 -y
# RUN conda create -n evergy_project python=3.10.8 -y
# RUN conda activate evergy_project

RUN conda install pandas=1.4.4 -y
RUN conda install scikit-learn=1.1.3 -y
RUN conda install matplotlib=3.6.2 -y
RUN conda install altair=4.2.0 -y
RUN conda install altair_saver=0.1.0 -y
RUN conda install requests=2.28.1 -y
RUN conda install python-graphviz -y
RUN conda install pandoc -y

RUN pip install xgboost==1.7.1
RUN pip install docopt
RUN pip install vl-convert-python==0.5.0
RUN pip install dataframe-image==0.1.3
RUN pip install openpyxl==3.0.10
RUN pip install ipython

RUN apt-get update && apt-get install make









# ---------------------------
# FROM continuumio/miniconda3

# # USER root

# RUN pip install docopt-ng \
#     && pip install vl-convert-python==0.5.0
# RUN conda install -c conda-forge -y pandoc
# RUN pip install joblib --quiet

# RUN conda update -n base -c conda-forge -y conda

# RUN apt-get update
# RUN apt-get -y --no-install-recommends install

# RUN conda install python-graphviz -y
# RUN conda install requests[version='>=2.24.0'] -y
# RUN conda install scikit-learn[version='>=1.1.3'] -y
# RUN conda install selenium[version='<4.3.0'] -y
# RUN conda install pip -y
# RUN conda install jinja2 -y
# RUN conda install ipykernel -y
# RUN conda install jsonschema=4.16 -y
# RUN conda install -c conda-forge altair_saver -y
# RUN conda install pandas[version='<1.5'] -y
# RUN conda install matplotlib[version='>=3.2.2'] -y
# RUN conda install -c conda-forge eli5 -y
# RUN conda install -c conda-forge shap -y
# RUN conda install -c conda-forge xgboost -y
    
# RUN pip install openpyxl
# RUN pip install dataframe-image==0.1.3
# RUN pip install altair

# RUN conda search graphviz --channel conda-forge
# RUN conda install pandoc

# RUN apt-get install make

# dependencies:
#   - graphviz
#   - selenium<4.3.0
#   - imbalanced-learn
#   - numpy

#   - pip:
#     - mglearn
#     - psutil>=5.7.2
#     - ipython


# ---------------------------
# FROM continuumio/miniconda3

# RUN conda install ipykernel -y
# RUN pip install ipython==8.7.0
# RUN conda install python-graphviz
# # RUN conda install -c anaconda graphviz=0.20.1
# # RUN conda search graphviz --channel conda-forge
# # RUN apt install chromium-chromedriver
# RUN pip install chromedriver-binary
# RUN conda install jinja2

# RUN conda install python=3.10.8
# RUN pip install -U scikit-learn==1.1.3
# RUN conda install requests

# RUN conda install -c conda-forge xgboost
# RUN conda install -c conda-forge lightgbm
# RUN conda install -c conda-forge catboost

# RUN conda install -c conda-forge eli5
# RUN pip install shap

# RUN pip install altair
# RUN pip install altair-saver

# RUN pip install pandas==1.4.4
# RUN pip install numpy==1.23.5
# RUN conda install pandoc
# RUN pip install docopt
# RUN pip install openpyxl
# RUN pip install dataframe-image==0.1.3
# RUN pip install vl-convert-python==0.4.0
# RUN pip install joblib==1.1.0

# RUN apt-get update && apt-get install make


