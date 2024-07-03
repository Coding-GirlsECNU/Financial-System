import os

import yaml


def read_yaml(path):
    content = open(path, mode='r', encoding='utf-8')
    config = yaml.load(content, Loader=yaml.FullLoader)
    content.close()
    return config


def get_absolute_path(relative_path):
    return os.path.join(os.path.dirname(__file__), relative_path)

class GlobalObject(object):
    def __init__(self, path='./config.yaml'):
        self.config = read_yaml(get_absolute_path(path))


global_object = GlobalObject()
