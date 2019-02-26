import numpy as np

def MAD(x, b=1.4826):
    '''
    '''
    if b == None:
        b = 1. / np.quantile((x-x.mean()) / x.std(), 0.75)
        
    m = np.median(x)
    
    return b*np.median(abs(x - m))