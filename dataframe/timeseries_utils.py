import pandas as pd

def get_train_and_test_from_timeseries(dataframe, train_size, outputs_col, verbose=0):
    '''
        Splits a dataset of a time series in its corrispective train and test parts.
        It keeps the order of the dataset.
        
        Attributes:
            - dataframe      (pandas.DataFrame) : 
            - train_size     (int)              : the percentage of the dataframe to keep in the training set (0 < train_size <= 1)
            - outputs        ([string])         : the outputs columns
            - verbose        (int)

        Returns:
            - (pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame): train_X, train_Y, test_X, test_Y
    '''

    assert type(dataframe) == pd.DataFrame
    assert train_size > 0 and train_size <= 1, 'The percentage of the train_size need to be greather than 0 and less or equal to 1.'
    assert outputs_col is not None and len(outputs_col) > 0

    nrow = round(train_size * dataframe.shape[0])

    train = series.iloc[:nrow, :]
    test = series.iloc[nrow:, :]

    train_X = train.drop(columns=output)
    test_X = test.drop(columns=output)

    train_Y = train[output]
    test_Y = test[output]

    if verbose == 1:
        print('Training set shape for X (inputs):')
        print(train_X.shape)
        print('Training set shape for Y (output):')
        print(train_Y.shape)
        print('Test set shape for X (inputs):')
        print(test_X.shape)
        print('Test set shape for Y (output):')
        print(test_Y.shape)
    
    return train_X, train_Y, test_X, test_Y

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