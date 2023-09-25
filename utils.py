import numpy as np

def min_max_scaling(data):
    flat_data = data.flatten()
    x_min = min(flat_data)
    x_max = max(flat_data)
    new_max = 1
    new_min = 0
    scaled_data = np.zeros(data.size)
    for i, x in enumerate(flat_data):
        scaled_data[i] = ((x-x_min) / (x_max-x_min)) * (new_max - new_min) + new_min
    scaled_data=scaled_data.reshape(data.shape)
    return scaled_data


def standart_scaling(data):
    flat_data = data.flatten()
    mean = np.nanmean(flat_data)
    std = np.nanstd(flat_data)
    scaled_data = np.zeros(data.size)
    for i, x in enumerate(flat_data):
        scaled_data[i] = (x-mean)/std
    scaled_data=scaled_data.reshape(data.shape)
    return scaled_data
