import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_correlation_from_dataframe(dataframe, columns=None, annot=True):
    '''
        Plots the correlations between the columns of a dataframe

        Attributes:
            - dataframe     (pandas.DataFrame) : the dataframe
            - columns       ([string])         : the columns to analyze, if None or []: all the columns 
            - values        (bool)             : whether or not show the correlation values in the plot
    '''

    if columns is None or len(columns) == 0:
        df = dataframe
    else:
        df = dataframe[columns].copy()

    colormap = plt.cm.RdBu_r
    plt.figure(figsize=(30,20), facecolor='white')
    plt.title(u'Correlation ', y=1.05, size=16)

    mask = np.zeros_like(df.corr())
    mask[np.triu_indices_from(mask)] = True

    svm = sns.heatmap(df.corr(), mask=mask, linewidths=0.1,vmax=1.0,square=True, center=0, cmap=colormap, linecolor='white', annot=annot)