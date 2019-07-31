import copy


def delete_staring_period(data_dict, drop_num=120):
    """
    delete the starting period of every single trial, should be used after split_2_events
    :param data_dict:
    :param drop_num:
    :return:
    """
    deleted_dict = copy.deepcopy(data_dict)
    for key in deleted_dict.keys():
        deleted_dict[key] = [data[drop_num:] for data in data_dict[key]]
    return deleted_dict

def split_2_events(data_dict, interval=1320):
    """
    Split the points into individual events, still in dictionary format.
    :param data_dict:
    :param interval:
    :return:
    """
    splitted_dict = copy.deepcopy(data_dict)
    for key in splitted_dict.keys():
        splitted_dict[key] = [data_dict[key][i: i + interval] for i in range(0, len(data_dict[key]) - interval, interval)]
    return splitted_dict

