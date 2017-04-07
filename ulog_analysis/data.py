import pandas as pd
import pyulog


def read_ulog(log_path: str, message_list: list = None) -> dict:
    """
    Read a ulog and return a dictionary of pandas DataFrame
    :param log_path: path to log file
    :param message_list: list of messages to read, None means read all
    :return: dictionary with keys for each topic, each topic has a key
    for each multi_id, and each of those has a pandas dictionary
    """
    ulog = pyulog.ULog(file_name=log_path, message_name_filter_list=message_list)
    data = {}
    for topic in ulog.data_list:
        if topic.name not in data.keys():
            data[topic.name] = {}
        data[topic.name][topic.multi_id] = pd.DataFrame(topic.data)
    return data
