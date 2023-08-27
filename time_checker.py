import os
import os.path
import datetime

def get_file_last_access_modified_time_mb(file_path):
    if not os.path.isfile(file_path):
        return None
    stat = os.stat(file_path)
    last_access_time = stat.st_atime # python access the file don't change it
    last_modified_time = stat.st_mtime
    byte=stat.st_size
    mb=byte/1024/1024
    return datetime.datetime.fromtimestamp(last_access_time),datetime.datetime.fromtimestamp(last_modified_time),mb


def get_directory_last_access_modified_time(directory_path):
    files = []
    for root, _, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)

    if not files:
        return None

    latest_access_time = None
    latest_modified_time=None
    for file_path in files:
        access_time,modified_time,_ = get_file_last_access_modified_time_mb(file_path)
        if access_time and (latest_access_time is None or access_time > latest_access_time):
            latest_access_time = access_time
        if modified_time and (latest_modified_time is None or modified_time > latest_modified_time):
            latest_modified_time = modified_time

    return latest_access_time,latest_modified_time


r=get_directory_last_access_modified_time(r"D:\temp\old version")