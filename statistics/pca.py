import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def do_pca(dataframe, columns):
    '''
        Pca on some columns of a dataframe

        Attributes:
            - dataframe     (pandas.DataFrame)
            - columns       ([string]) : list of columns 

        Returns:
            - pca
    '''
    assert type(dataframe) == pd.DataFrame
    assert columns is not None and len(columns) > 0


    cp = dataframe.copy()
    cp = dataframe.replace([np.inf, -np.inf], np.nan).fillna(value=0, inplace=False)
    x = cp[columns].values

    # Standardizing the features
    x = StandardScaler().fit_transform(x)
    # fitting
    pca = PCA().fit(x)
    
    return pca.transform(x)