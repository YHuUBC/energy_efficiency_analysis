"""Reads train data set from the processed script and performs explanatory data analysis, 
It reads in the data, do exploratory data analysis and save the results as three png files.
Usage: src/data_processing.py <input_file> <output_file1> <output_file2> <output_file3>

Options:
<input_file>     Path (including filename) to data file
<output_file1>    Path (including filename) of where to locally write the file of the first correlation table as image file
<output_file2>    Path (including filename) of where to locally write the file of the second distribution plot as image file
<output_file3>    Path (including filename) of where to locally write the file of the third scatter plot as image file

"""

# load the packages
from docopt import docopt
import pandas as pd
import numpy as np
import altair as alt
from altair_saver import save
import dataframe_image as dfi
alt.renderers.enable('mimetype')


opt = docopt(__doc__)

def main(input_file, output_file1, output_file2, output_file3):
    # read in data
    train_df = pd.read_csv(input_file)

    # correlation matrix
    output_file1 = train_df.corr('spearman').style.background_gradient()

    # check the distribution of all variables
    column_list = train_df.columns.tolist()

    output_file2 = alt.Chart(train_df, 
                         title = 'Bar chart of variable distribution'
                        ).mark_bar(opacity = 0.5).encode(
    alt.X (alt.repeat(),
           type = 'quantitative',
          bin = alt.Bin(maxbins = 45)),
    alt.Y('count()', stack = None),
    tooltip = 'count()'
    ).properties(width = 150,
            height = 150).repeat(
    repeat = column_list,
    columns = 2)


    # pairwsie scatter plots

    output_file3 = alt.Chart(train_df,
                    title = 'Pairwise correlations').mark_point(opacity = 0.2,
                                       size = 5).encode(
    alt.X (alt.repeat("row"),
           type = 'quantitative',
           scale = alt.Scale(zero = False)),
    alt.Y(alt.repeat("column"),
          type = 'quantitative',
          scale = alt.Scale(zero = False))
    ).properties(
    width = 120,
    height = 120
    ).repeat(
    column = column_list,
    row = column_list
    )

    # save charts and table
    dfi.export(output_file1, 'output_file1.png')
    output_file2.save('output_file2.png')
    output_file3.save('output_file3.png')

if __name__ == "__main__":
    main(opt["<input_file>"], opt["<output_file1>"], opt["<output_file2>"], opt["<output_file3>"])

