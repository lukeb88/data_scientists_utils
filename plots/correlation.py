import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_correlation_from_dataframe(dataframe):
    '''
        Plots the correlations between the columns of a dataframe
    '''

    colormap = plt.cm.RdBu_r
    plt.figure(figsize=(30,20), facecolor='white')
    plt.title(u'Correlation ', y=1.05, size=16)

    mask = np.zeros_like(dataframe.corr())
    mask[np.triu_indices_from(mask)] = True

    svm = sns.heatmap(dataframe.corr(), mask=mask, linewidths=0.1,vmax=1.0,square=True, center=0, cmap=colormap, linecolor='white', annot=True)