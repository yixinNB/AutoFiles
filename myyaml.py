# from yaml import *
import yaml
def load(file_path):
    with open(file_path, 'r') as file:
        data=yaml.load(file.read(),Loader=yaml.Loader)
    return data

def save(data,file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)