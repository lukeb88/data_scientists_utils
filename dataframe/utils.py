from sklearn.preprocessing import LabelEncoder

def encode_categorical_column(dataframe, columns, suffix='_enc'):
    '''
        Encodes a column of the dataframe

        Attributes:
            - dataframe: (pandas.DataFrame)
            - column: (list[string]) name/s of the column/s to encode
            - suffix: (string, default='_enc') suffix to add at the name of the original column for the encoded one
    '''

    encoder = LabelEncoder()

    for col in columns:
        dataframe[col + suffix] = encoder.fit_transform(dataframe[col])

    return dataframe
    