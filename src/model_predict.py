# +
## code to train models 
# python src/model_predict.py --train_file='data/processed/train_df.csv'  --test_file='data/processed/test_df.csv' --out_file=src/training_score.png 
#
"""Downloads data excel data from the web to a local filepath in excel file format.
Usage: src/down_data.py  --train_file=<filepath> --test_file=<filepath> --out_file=<out_file>
Options:

--train_file=<filepath>           the file and path of train dataset(must be in standard csv format)
--test_file=<filepath>           the file and path of test dataset(must be in standard csv format)
--out_file=<out_file>             the filename and path of the output file to be saved(must be in png format)
"""
from docopt import docopt
import requests
import os
import pandas as pd
import numpy as np

from IPython.display import HTML, display

from sklearn.model_selection import cross_validate 
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import dataframe_image as dfi

# +

opt = docopt(__doc__)

def main(train_file, test_file, out_file):
       
    train_df = pd.read_csv(train_file)
    test_df =  pd.read_csv(test_file)
    models = {
    "DecisionTree": DecisionTreeRegressor(),
    "KNN_reg": KNeighborsRegressor(),
    "Ridge": Ridge(),
    "SVC": SVR(),
    "RandomForest" :RandomForestRegressor()
        }

    scores ={}
    # results_dict={}
    for  modelname,model in models.items(): 
        pipe =  make_pipeline(StandardScaler(), model)
        scores[modelname] = pd.DataFrame(cross_validate(pipe, X_train,y_train, return_train_score= True, scoring = 'r2')).agg(['mean', 'std']).round(3).T
        pd.concat(scores, axis=1)

    result  = pd.concat(scores, axis=1)
    result
    
    dfi.export(result, out_file)
    
    
    
    
    
    
    
    
    
    
    
# -

if __name__ == "__main__":
  main( opt["--train_file"],opt["--test_file"] , opt["--out_file"])


