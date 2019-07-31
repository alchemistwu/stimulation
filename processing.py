import numpy as np

def average_2d_list(data_list):
    """
    average the data list by column
    :param data_list:
    :return:
    """
    data_array = np.asarray(data_list)
    result = np.average(data_array, axis=0)
    return result

def normalize_2d_list(data_list, base_num=600):
    """
    Normalize the data by the average of baseline points
    :param data_list:
    :param base_num:
    :return:
    """
    normalized_list = []
    for line in data_list:
        baseline = np.mean(np.asarray(line[0: base_num]))
        normalized_list.append(np.asarray(line)/baseline)
    return normalized_list



