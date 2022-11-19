#!/usr/bin/env python
# coding: utf-8

# **Title: Exploratory data analysis of the Energy Efficiency data set**

# **Summary of the data set**
# 
# The data set used in this exploratory data analysis is retrieved from "http://archive.ics.uci.edu/ml/datasets/Energy+efficiency#". It was contributed by Angeliki Xifara (angxifara '@' gmail.com, Civil/Structural Engineer) and was processed by Athanasios Tsanas (tsanasthanasis '@' gmail.com, Oxford Centre for Industrial and Applied Mathematics, University of Oxford, UK). It contains 768 instances and was donated at 2012-11-30. It has no missing values. It has a total of 10 variables, with 8 of them are attributes(features) and two responses. The authors suggested that the aim of this data set is to use the eight features to predict the two responses. These variables are shown in the table below:

# | Variable name in data set| Description |
# | --- | --- |
# | X1 | Relative Compactness |
# | X2 | Surface Area |
# | X3 | Wall Area |
# | X4 | Roof Area |
# | X5 | Overall Height |
# | X6 | Orientation |
# | X7 | Glazing Area |
# | X8 | Glazing Area Distribution |
# | y1 | Heating Load |
# | y2 | Cooling Load |

# **Partition the data set into training and test sub-data sets**
# 
# The whole data set were divided into train and test sets, with 70% train data and 30% test data. 

# | Number of cases| Sub data set |
# | --- | --- |
# | 537 | Train set |
# | 231 | Test set |

# **Exploratory data analysis with the train set**
# 
# The exploratory data analysis were conducted through the following steps:
# 1.load in the necessary packages and split the data into train and test sets, NaN were dropped;
# 2.do EDA on the train set. First to check the data types and see if there are missing values; we found out that there is no missing value. Then we proceed to see the data distribution through bar plots, value_counts, correlations. Through the EDA, we could identify that all the variables are numeric type, but Roof Area', 'Surface Area', 'Wall Area', 'Overall Height', 'Orientation', 'Glazing Area', and 'Glazing Area Distribution' are actually categorical.
# 3.From the above analysis, we may proceed to do a supervised machine learning model with data preprocessed by Standard Scaling and One Hot Encode on the numeric features with Heating Load and Cooling Load as the targets.

# In[1]:


# load the packages
import pandas as pd
import numpy as np
import altair as alt
alt.renderers.enable('mimetype')
from sklearn.model_selection import train_test_split


# In[2]:


# read in data set
# rename the attributes
# source:http://archive.ics.uci.edu/ml/datasets/Energy+efficiency#
energy_data = pd.read_csv('https://raw.githubusercontent.com/UBC-MDS/energy_efficiency_analysis/main/data/ENB2012data.csv').dropna()
energy_data = energy_data.rename(columns = {'X1':'Relative Compactness',
                                            'X2':'Surface Area',
                                            'X3':'Wall Area',
                                            'X4':'Roof Area',
                                            'X5':'Overall Height',
                                            'X6':'Orientation',
                                            'X7':'Glazing Area',
                                            'X8':'Glazing Area Distribution',
                                            'Y1':'Heating Load',
                                            'Y2':'Cooling Load'})
train_df, test_df = train_test_split(energy_data, test_size = 0.3, random_state = 4)


# In[3]:


# check the data types and see if there are missing values
train_df.info()
train_df.head()


# In[4]:


train_df.describe(include="number")


# In[5]:


train_df['Relative Compactness'].value_counts()


# In[6]:


train_df['Surface Area'].value_counts()


# In[7]:


train_df['Roof Area'].value_counts()


# In[8]:


train_df['Overall Height'].value_counts()


# In[9]:


train_df['Orientation'].value_counts()


# In[10]:


train_df['Glazing Area'].value_counts()


# In[11]:


train_df['Glazing Area Distribution'].value_counts()


# In[12]:


# check the distribution of all variables
column_list = train_df.columns.tolist()

distri_chart = alt.Chart(train_df, 
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

distri_chart


# **As shown above, although all variables are numeric type, from the results of the bar charts and the value_counts of each variable, 'Roof Area', 'Surface Area', 'Wall Area', 'Overall Height', 'Orientation', 'Glazing Area', and 'Glazing Area Distribution' are actually categorical.**

# In[13]:


# correlation matrix
energy_data.corr('spearman').style.background_gradient()


# In[14]:


# pairwsie scatter plots

scatters = alt.Chart(train_df,
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
# Show the plot
scatters


# **References**
# 
# A. Tsanas, A. Xifara: 'Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools', Energy and Buildings, Vol. 49, pp. 560-567, 2012 (the paper can be accessed from [Web Link])
# 
# For further details on the data analysis methodology:
# A. Tsanas, 'Accurate telemonitoring of Parkinsonâ€™s disease symptom severity using nonlinear speech signal processing and statistical machine learning', D.Phil. thesis, University of Oxford, 2012 (which can be accessed from [Web Link])

# In[ ]:




