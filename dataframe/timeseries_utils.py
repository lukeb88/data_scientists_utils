import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

def create_window_multivariate(data, window_size_backward=1, window_size_forward=None, full_forward=True):    
    '''
        Starting from a pandas.DataFrame it create a windowed version, 
         with values from the past and from the future. 
        
        Attributes:
            - data                  : (pandas.DataFrame)   original dataframe
            - window_size_backward  : (int)                window size (in the past)
            - window_size_forward   : (int, default None)  window size (in the future). If None, only past values are going to be aggregated
            - full_forward          : (bool, default True) when window_size_forward != 0 indicates if all the values, from the actual to the window_size_forwardth must been kept
            
        Return:
            - pandas.DataFrame      : the windowed version of the original dataframe:
                                        - the columns in the past have the same name of the originals followed by a -1
                                        - the columns in the future have the same name of the originals followed by a +1
    '''
    
    # it has to be greater than 0
    assert type(window_size_backward) == int and window_size_backward > 0
    
    res = []
    for c in data.columns:

        sub_df = data[[c]].copy()
        data_s = sub_df.copy()
        col_name = [c]
        for i in range(window_size_backward):
            col_name.append(c + '-' + str(i))
            sub_df = pd.concat([sub_df, data_s.shift((i + 1))], axis = 1)
        
        # if not none it has to be greater than 0
        if window_size_forward is not None and type(window_size_forward == int) and window_size_forward > 0:
            column_to_delete = []
            for i in range(1, window_size_forward + 1):
                
                if full_forward == False:
                    if i != window_size_forward:
                        column_to_delete.append(c + '+' + str(i))
                
                col_name.append(c + '+' + str(i))
                sub_df = pd.concat([sub_df, data_s.shift((-i))], axis = 1)
            
        sub_df.dropna(axis=0, inplace=True)
        sub_df.columns = col_name
        
        if full_forward == False and len(column_to_delete) > 0:
            sub_df.drop(columns=column_to_delete, inplace=True)


        res.append(sub_df)

    final_df = pd.concat(res, axis=1)
    
    return final_df

def seasonal_decompose(dataframe, feature):    
    '''
        Returns the seasonal decomposition of a time-series

        Attributes:
            - dataframe: (pandas.DataFrame)
            - feature: (string) the column of the DF on which to perform decomposition

        Returns: 
            - decomposition (trend, seasonal, observed, resid)
    '''

    return seasonal_decompose(dataframe[feature], model='additive')