# +
# author: Tiffany Timbers
# date: 2019-12-18
## code to download
# python src/download_data.py --url='http://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx' 
#--out_file=data/raw/ENB2012_data.xlsx
"""Downloads data excel data from the web to a local filepath in excel file format.
Usage: src/down_data.py  --url=<url> --out_file=<out_file>
Options:

--url=<url>              URL from where to download the data (must be in standard csv format)
--out_file=<out_file>    Path (including filename) of where to locally write the file
"""
  
from docopt import docopt
import requests
import os
import pandas as pd

opt = docopt(__doc__)

def main(url, out_file):
  try: 
    request = requests.get(url)
    request.status_code == 200
  except Exception as req:
    print("Website at the provided url does not exist.")
    print(req)
    
  data = pd.read_excel(url, header=0)
  
  try:
      data.to_excel(out_file, index = False)
  except:
      os.makedirs(os.path.dirname(out_file))
      data.to_excel(out_file, index = False)

if __name__ == "__main__":
  main( opt["--url"], opt["--out_file"])
