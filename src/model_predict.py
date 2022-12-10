# author: Nate Puangpanbut, Mehwish Nabi
# date: 2022-11-26
# update: Yaou Hu, 2022-12-2
# This code is to read the train data set and performs model fitting with various types of models,
# select the best model and performs prediction,
# finally, saving figures of cv-score comparision and best prediction on privided destination folder,
# also, save all modles as pickle file to result/model folder
# example :
# python src/model_predict.py data/processed/train_df.csv data/processed/test_df.csv results/energy_analysis/training_score.png results/energy_analysis/prediction.png
"""Trains the various models.
Usage: src/model_predict.py <input1> <input2> <out1> <out2>

python src/model_predict.py data/processed/train_df.csv data/processed/test_df.csv results/energy_analysis/training_score.png results/energy_analysis/prediction.png

Options:
<input1>  the file and path of train dataset(must be in standard csv format)
<input2>   the file and path of test dataset(must be in standard csv format)
<out1>   the filename and path of score to be saved(must be in png format)
<out2>   the filename and path of prediction to be saved(must be in png format)
"""

from docopt import docopt
import pandas as pd
import numpy as np

from IPython.display import HTML, display

import pickle
from sklearn.model_selection import cross_validate 
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
import xgboost as xg
import dataframe_image as dfi
import altair as alt
from altair_saver import save
import vl_convert as vlc
alt.renderers.enable('mimetype')

opt = docopt(__doc__)

def main(input1, input2, out1, out2):
#    opt = docopt(__doc__)
#    print(opt)
    
    # read data
    train_df = pd.read_csv(input1)
    test_df =  pd.read_csv(input2)
    
    # separate X, y
    X_test , y_test = test_df.drop(columns=["Heating Load", "Cooling Load"]), test_df["Heating Load"]
    X_train , y_train = train_df.drop(columns=["Heating Load", "Cooling Load"]), train_df["Heating Load"]
    
    # construct interested models
    models = {
        "KNN_reg": KNeighborsRegressor(),
        "Ridge": Ridge(),
        "DecisionTree": DecisionTreeRegressor(),
        "SVR": SVR(),
        "RandomForest": RandomForestRegressor(),
        "XGB": xg.XGBRegressor()
        }

    # run all interested models
    scores ={}
    for modelname, model in models.items():
        pipe =  make_pipeline(StandardScaler(), model)
        scores[modelname] = pd.DataFrame(cross_validate(pipe, X_train,y_train, return_train_score= True, scoring = 'r2')).agg(['mean', 'std']).round(3).T

    result_df  = pd.concat(scores, axis=1)
    
    # best model XGB
    pipe_xgb =  make_pipeline(StandardScaler(), xg.XGBRegressor())
    pipe_xgb.fit(X_train,y_train)
    
    # prediction
    y_pred = pipe_xgb.predict(X_test)
    
    prediction_dict = {'response': list(y_pred)+list(y_test),
                      'type': ['Predicted']*len(y_pred)+['Actual']*len(y_pred),
                      'sample': list(range(1,len(y_pred)+1))+list(range(1,len(y_pred)+1))}
    prediction_df = pd.DataFrame(prediction_dict)
    
    # plot
    point = alt.Chart(prediction_df,
                    title = 'Comparison of Prediction and Actual value on test data').mark_point().encode(
        y = alt.Y('response',type = 'quantitative', scale = alt.Scale(zero = False), title='Heating load'),
        x = alt.X('sample', title='Sample / Observations'),
        color = 'type'
    ).properties(height=300,width=300)
    
    # cited from Joel Ostblom @UBC MDS
    def save_chart(chart, filename, scale_factor=1):
        '''
        Save an Altair chart using vl-convert
    
        Parameters
        ----------
        chart : altair.Chart
        Altair chart to save
        filename : str
        The path to save the chart to
        scale_factor: int or float
        The factor to scale the image resolution by.
        E.g. A value of `2` means two times the default resolution.
        '''
        if filename.split('.')[-1] == 'svg':
            with open(filename, "w") as f:
                f.write(vlc.vegalite_to_svg(chart.to_dict()))
        elif filename.split('.')[-1] == 'png':
            with open(filename, "wb") as f:
                f.write(vlc.vegalite_to_png(chart.to_dict(), scale=scale_factor))
        else:
            raise ValueError("Only svg and png formats are supported")
    
    # export score result
    # dfi.export(result_df, out1)
    
    # save predicted plot
    save_chart(point, out2, 2)
    
    # save the final model
    filename = 'results/model/final_model/final_model.sav'
    pickle.dump(pipe_xgb.fit(X_train,y_train), open(filename, 'wb'))
    
    # save KNN
    pipe_knn = make_pipeline(StandardScaler(), KNeighborsRegressor())
    filename = 'results/model/KNN/KNN_model.sav'
    pickle.dump(pipe_knn.fit(X_train,y_train), open(filename, 'wb'))
    
    # save Ridge
    pipe_ridge = make_pipeline(StandardScaler(), Ridge())
    filename = 'results/model/Ridge/Ridge_model.sav'
    pickle.dump(pipe_ridge.fit(X_train,y_train), open(filename, 'wb'))
    
    # save DT
    pipe_DT = make_pipeline(StandardScaler(), DecisionTreeRegressor())
    filename = 'results/model/DT/DecisionTree_model.sav'
    pickle.dump(pipe_DT.fit(X_train,y_train), open(filename, 'wb'))
    
    # save SVR
    pipe_svr = make_pipeline(StandardScaler(), SVR())
    filename = 'results/model/SVR/SVR_model.sav'
    pickle.dump(pipe_svr.fit(X_train,y_train), open(filename, 'wb'))
    
    # save RF
    pipe_rf = make_pipeline(StandardScaler(), RandomForestRegressor())
    filename = 'results/model/RF/RandomForest_model.sav'
    pickle.dump(pipe_rf.fit(X_train,y_train), open(filename, 'wb'))


if __name__ == "__main__":
    main(opt["<input1>"], opt["<input2>"], opt["<out1>"], opt["<out2>"])
