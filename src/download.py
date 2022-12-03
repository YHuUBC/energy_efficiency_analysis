# date: 2022-12-2
# This code is to download original excel data and transform to csv at the destination folder
# example :
# python src/download.py http://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx data/raw/ENB2012_data.csv
"""Reads data from the download script and performs data cleaning/pre-processing, 
transforming, and/or partionting that needs to happen before exploratory data analysis or modeling takes place.
It reads in the data, rename the columns, and split the data into train and test sub-sets.
Usage: src/download.py <input_file> <output_file1>

python src/download.py http://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx data/raw/ENB2012_data.csv

Options:
<input_file>     Path (including filename) to data file
<output_file1>    Path (including filename) of where to locally write the file of the train_df

"""

import pandas as pd
import numpy as np
from docopt import docopt

opt = docopt(__doc__)

def main(input_file, output_file1):
    # read in data
    data = pd.read_excel(input_file).dropna()
    # save data into csv
    data.to_csv(output_file1, index = False)
    
if __name__ == "__main__":
    main(opt["<input_file>"], opt["<output_file1>"])
