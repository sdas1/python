import numpy as np

def remove_outliers(data, m=3, replace=True):
    # implement task 1 here
    raise NotImplementedError

"""
def remove_outliers(an_array, m=3, replace=True):
    mean = np.mean(an_array)
    sigma = np.std(an_array)
    distance_from_mean = abs(an_array - mean)
    not_outlier = distance_from_mean < m * sigma
    if (replace) :
        return mean
    else:
        return an_array[not_outlier]
    
    
if __name__ == "__main__":
    # use this for your own testing!

    data = np.array([10, 10, 10, 17, 10, 10])
    print(remove_outliers(data, m=3, replace=False))
"""


