import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def plot_seasonal_decomposition(dataframe, feature, figsize=(30, 10)):
    '''
        Plots the seasonal decomposition of a time series

        Attributes:
            - dataframe: (pandas.DataFrame)
            - feature: (string) the column of the DF on which to perform decomposition
            - figsize: ((X_dim, Y_dim)) the dimension of the figure

    '''

    decompositions = seasonal_decompose(dataframe[feature], model='additive')

    plt.figure(figsize=figsize)
    plt.plot(decompositions.trend, label='trend')
    plt.plot(decompositions.seasonal, label='seasonal')
    plt.plot(decompositions.resid, label='residual')
    plt.plot(decompositions.observed, label='observed')
    plt.title('Seasonal decomposition for: ' + str(feature))
    plt.legend()
    plt.show()