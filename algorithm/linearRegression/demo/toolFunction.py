def normalize(data,lam=0.5):
    '''
    normalize data of non normal distribution
    '''
    import numpy as np
    import pandas as pd
    data=data+1e-9
    if lam== 0:
        transformed_data = np.log(data)
    else:
        transformed_data = (data**lam- 1) /lam

    return transformed_data.astype(int)

def z_normal(data):
    
    '''
     data must be pandas dataframe
     return mean, std,z_normal
    '''
    return data.mean(), data.std(),(data - data.mean()) / data.std()
