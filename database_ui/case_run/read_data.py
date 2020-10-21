import json


class ReadData(object):

    def read(self, path):
        with open(path, 'r', encoding='utf8')as file:
            data = json.load(file)
        return data
