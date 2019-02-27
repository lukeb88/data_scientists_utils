import numpy as np
import matplotlib.pylab as plt

# Import dependencies
import plotly
import plotly.graph_objs as go

# Configure Plotly to be rendered inline in the notebook.
plotly.offline.init_notebook_mode()

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


def super_pca_visualization(principal_components, classes):
        '''

        Attributes:
                - principal_components          (np.array[]) : principal components
                - classes                       ([numeric])  : list of different classes to color the plot (same size of principal_components.shape[0])
        '''

        assert principal_components.shape[0] == classes.shape[0], 'The length of the classes need to be the same of principal_components.shape[0]

        # doing pca
        pc = principal_components

        pcs = dict()

        for single_class in classes.unique():
        i = 0
        actual_class_pc = []
        for c in classes:
                if c == single_class:
                actual_class_pc.append(pc[i])
                
                i += 1
                
        if len(actual_class_pc) > 0:
                pcs[single_class] = actual_class_pc
                
        traces = []        
                
        for key, value in pcs.items():
        pc_np = np.asarray(value)

        # Configure the trace.
        trace = go.Scatter3d(
                x=pc_np[:,0],  # <-- Put your data instead
                y=pc_np[:,1],  # <-- Put your data instead
                z=pc_np[:,2],  # <-- Put your data instead
                mode='markers',
                name=str(key),
                marker={
                'size': 2,
                'opacity': 0.8,
                }
        )

        traces.append(trace)

        # Configure the layout.
        layout = go.Layout(
        margin={'l': 0, 'r': 0, 'b': 0, 't': 0}
        )

        plot_figure = go.Figure(data=traces, layout=layout)

        # Render the plot.

        plotly.offline.iplot(plot_figure)

        return pcs