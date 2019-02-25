from statsmodels.tsa.seasonal import seasonal_decompose

def plot_seasonal_decomposition(dataframe, feature, figsize=(30, 10)):
    '''
        Plots the seasonal decomposition of a time series

        Attributes:
            - dataframe: (pandas.DataFrame)
            - feature: (string) the column of the DF on which to perform decomposition

        Returns:
            - object : a object with seasonal, trend, and resid attributes

    '''

    decompositions = seasonal_decompose(dataframe[feature], model='additive')

    return decompositions