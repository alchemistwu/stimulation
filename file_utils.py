import os

def cvt_file2dict(file_path):
    """
    read a txt data file, and transfer it into a continuous data dictionary.
    :param file_path: full path to raw data file
    :return:
    """
    start_index = None
    data_dict = {}
    cat_len = []

    if not os.path.isfile(file_path):
        raise ValueError("Error in file path.")
    with open(file_path, 'r') as f:
        lines = f.readlines()


    for line_index in range(len(lines)):
        line = lines[line_index]
        candidate = line.strip().split('\t')
        if is_data_list(candidate):
            if start_index is None:
                start_index = line_index
                cat_len = len(candidate)
                data_list = [[] for i in range(cat_len)]

        if start_index is not  None:
            for i in range(cat_len):
                data_list[i].append(int(candidate[i]))
    header = lines[start_index - 1].strip().split('\t')
    for key_index in range(len(header)):
        data_dict[header[key_index]] = data_list[key_index]
    print("Data is already loaded.")
    return data_dict


def is_data_list(list):
    """
    Whether ths splitted line is a data line or not.
    :param list:
    :return:
    """
    if len(list) >= 1:
        for item in list:
            if not item.isdigit():
                return False
        else:
            return True

