# author: Yaou Hu
# date: 2022-11-26
# This code is to csv data and performs data cleaning, pre-processingm, then
# separating into train and test data sets, and finally save to the provided destination folder.
# example :
# python src/data_preprocess.py data/raw/ENB2012_data.csv data/processed/train_df.csv data/processed/test_df.csv
"""Reads data from the download script and performs data cleaning/pre-processing, 
transforming, and/or partionting that needs to happen before exploratory data analysis or modeling takes place.
It reads in the data, rename the columns, and split the data into train and test sub-sets.
Usage: src/data_processing.py <input_file> <output_file1> <output_file2>

python src/data_preprocess.py data/raw/ENB2012_data.csv data/processed/train_df.csv data/processed/test_df.csv

Options:
<input_file>     Path (including filename) to data file
<output_file1>    Path (including filename) of where to locally write the file of the train_df
<output_file2>    Path (including filename) of where to locally write the file of the test_df

"""

import pandas as pd
import numpy as np
from docopt import docopt
from sklearn.model_selection import train_test_split



opt = docopt(__doc__)

def main(input_file, output_file1, output_file2):
    # read in data
    data = pd.read_csv(input_file).dropna()
    # rename data
    data = data.rename(columns = {'X1':'Relative Compactness',
                                            'X2':'Surface Area',
                                            'X3':'Wall Area',
                                            'X4':'Roof Area',
                                            'X5':'Overall Height',
                                            'X6':'Orientation',
                                            'X7':'Glazing Area',
                                            'X8':'Glazing Area Distribution',
                                            'Y1':'Heating Load',
                                            'Y2':'Cooling Load'})
    # split data into train and test sub-sets with 30% as test data
    train_df, test_df = train_test_split(data, test_size = 0.3, random_state = 4)
    # save train subset into a new set
    train_df.to_csv(output_file1, index = False)
    test_df.to_csv(output_file2, index = False)
    
if __name__ == "__main__":
    main(opt["<input_file>"], opt["<output_file1>"], opt["<output_file2>"])





