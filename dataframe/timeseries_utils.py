import pandas as pd

def create_window(df, window_size=1):    
    '''
        Starting from a dataset (pandas.DataFrame) on a timeseries, 
        consisting of a single column with the index in the format pandas.DatetimeIndex, 
        aggregates the previous values

        Attributes:
            - df: (pandas.DataFrame) 
            - window_size: (int) elements to aggregate

        Returns: 
            - pandas.DataFrame: the dataframe with the aggregated values
    '''

    df_s = df.copy()
    cols_name = []
    for i in range(window_size):
        cols_name.append('val_t_minus_' + str(i+1))
        df = pd.concat([df, df_s.shift((i + 1))], axis = 1)

    df.dropna(axis=0, inplace=True)
    
    df.columns = ['val'] + cols_name
    
    return df