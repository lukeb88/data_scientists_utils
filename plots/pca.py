import numpy as np
import matplotlib.pylab as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def pca_two_vs_three_visualization(dataframe, columns, classes=None):
    '''
        PCA visualization in 3 dim and 2 dim.

        Attributes:
            - dataframe: (pandas.DataFrame) 
            - columns: (array[string]) columns to use for PCA
            - classes: (array[string] OR array[int]) array of colors or array of values for auto-colorize
    '''

    # Estraggo features basandomi sulle colonne
    cp = dataframe.copy()
    # Replace -inf and inf with zeros
    cp = dataframe.replace([np.inf, -np.inf], np.nan).fillna(value=0, inplace=False)
    x = cp[columns].values
    # Standardizing the features
    x = StandardScaler().fit_transform(x)    
    pca = PCA(n_components=3)
    principalComponents = pca.fit_transform(x)

    fig = plt.figure(figsize=(20,10))
    # First 2 components
    ax1 = fig.add_subplot(121)
    ax1.scatter(principalComponents[:,0], principalComponents[:,1], c=classes, cmap=plt.cm.Spectral, alpha=0.4)
    # First 3 components
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    ax2.scatter(principalComponents[:,0], principalComponents[:,1], principalComponents[:,2], c=classes, cmap=plt.cm.Spectral, alpha=0.4)      
    ax2.w_xaxis.set_ticklabels([])
    ax2.w_yaxis.set_ticklabels([])
    ax2.w_zaxis.set_ticklabels([])

    ax1.set_title('PCA - first 2 components')
    ax2.set_title('PCA - first 3 components')