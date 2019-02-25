import pandas as pd
import numpy as np

def autocorr(x):
    '''
        Autocorrelation check

        Attributes:
            - x (numpy.array) : input array 

        Returns:
            - float : r
            - float : lag
    '''
    n = x.size
    norm = (x - np.mean(x))
    result = np.correlate(norm, norm, mode='same')
    acorr = result[n//2 + 1:] / (x.var() * np.arange(n-1, n//2, -1))
    lag = np.abs(acorr).argmax() + 1
    r = acorr[lag-1]        
    if np.abs(r) > 0.5:
      print('Appears to be autocorrelated with r = {}, lag = {}'. format(r, lag))
    else: 
      print('Appears to be not autocorrelated')
    return r, lag
    

def remove_correlated_columns(dataframe, threshold=0.95):
    '''
        Removes the columns of a dataframe that are correlated more that threshold

        Attrubutes:
            - dataframe: (pandas.DataFrame) the original dataframe
            - threshold: (float, default = 0.95) the lower threshold for the correlation

        Returns:
            - pandas.DataFrame : a copy of the original dataframe without the correlated columns
            - [string] : the columns dropped
    '''
    df = dataframe.copy()

    # Create correlation matrix
    corr_matrix = df.corr().abs()

    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

    # Find index of feature columns with correlation greater than threshold
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]

    # Drop features 
    df.drop(df.columns[to_drop], axis=1, inplace=True)

    return df, to_drop


## 


