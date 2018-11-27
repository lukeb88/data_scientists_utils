from pandas.tools.plotting import autocorrelation_plot

def check_series_is_white_noise(df, feature):
    '''
    '''
    autocorrelation_plot(df[feature].fillna(0))