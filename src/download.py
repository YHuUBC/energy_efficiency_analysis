#author : Mehwish Nabi
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
import requests

opt = docopt(__doc__)

def main(url, output_file1):
  """ Downloads the file in csv format from the provided link
  at the given path 
  parameters :
        url : the link for the data 
        out_file : the path and name of the file for the file to be saved
  """
  try: 
    request = requests.get(url)
    request.status_code == 200
  except Exception as req:
    print("Website at the provided url does not exist.")
    print(req)
    
  data = pd.read_excel(url, header=0)
  try:
      data.to_csv(output_file1, index = False)
  except:
      os.makedirs(os.path.dirname(output_file1))
      data.to_csv(output_file1, index = False)

if __name__ == "__main__":
    main(opt["<input_file>"], opt["<output_file1>"])
