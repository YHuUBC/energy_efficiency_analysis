# author: Yaou Hu
# date: 2022-11-26
# This code is to read the train data set and performs explanatory data analysis and finally save to provided destination folder
# example :
# python src/eda_script_plots_update.py data/processed/train_df.csv results/eda/eda_corr_table.png results/eda/eda_distribution_plot.png results/eda/eda_scatter1_plot.png
"""Reads train data set from the processed script and performs explanatory data analysis, 
It reads in the data, do exploratory data analysis and save the results as four png files.
It is supposed to work across systems.
Usage: src/data_processing.py <input_file> <output_file1> <output_file2> <output_file3>

Options:
<input_file>     Path (including filename) to data file
<output_file1>    Path (including filename) of where to locally write the file of the first correlation table as image file
<output_file2>    Path (including filename) of where to locally write the file of the second distribution plot as image file
<output_file3>    Path (including filename) of where to locally write the file of the third scatter plot with 'Heating Load' as y-axis as image file

"""

# load the packages
from docopt import docopt
import pandas as pd
import numpy as np
import altair as alt
from altair_saver import save
import dataframe_image as dfi
import vl_convert as vlc

alt.renderers.enable('mimetype')


opt = docopt(__doc__)

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
    
def main(input_file, output_file1, output_file2, output_file3):
    # read in data and test the data format
    if input_file.split('.')[-1] != 'csv':
        raise ValueError("Only csv format is supported")
    else:    
        train_df = pd.read_csv(input_file)
        # test the output format
        if type(train_df) != pd.DataFrame:
            raise ValueError("Only dataframe is supported")
            # correlation matrix
        else:
            corr = train_df.corr('spearman').style.background_gradient()

            # check the distribution of all variables
            column_list = train_df.columns.tolist()
            feats = ['Relative Compactness', 'Surface Area', 'Wall Area', 'Roof Area',
                'Overall Height', 'Orientation', 'Glazing Area', 'Glazing Area Distribution']

            distri = alt.Chart(train_df, 
                         title = 'Bar chart of variable distribution'
                        ).mark_bar(opacity = 0.5).encode(
            alt.X (alt.repeat(),
            type = 'quantitative',
            bin = alt.Bin(maxbins = 45)),
            alt.Y('count()', stack = None),
            tooltip = 'count()'
            ).properties(width = 300,
            height = 300).repeat(
            repeat = column_list,
            columns = 2)


            # pairwsie scatter plots

            scatter1 = alt.Chart(train_df,
                    title = 'Scatter plot of feature correlates with heating load'
                            ).mark_point(opacity = 0.2,
                                       size = 5).encode(
            alt.X (alt.repeat(),
               type = 'quantitative',
               scale = alt.Scale(zero = False)),
                alt.Y('Heating Load',
                scale = alt.Scale(zero = False))
                ).properties(
                width = 300,
               height = 300
              ).repeat(
              repeat = feats,
              columns = 2
            )
       
            # save charts and table
            dfi.export(corr, output_file1)
            save_chart(distri, output_file2, 2)
            save_chart(scatter1, output_file3, 2)

        
if __name__ == "__main__":
    main(opt["<input_file>"], opt["<output_file1>"], opt["<output_file2>"], opt["<output_file3>"])

