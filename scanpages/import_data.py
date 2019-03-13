import json


class ImportData:

    def __init__(self, source):
        self.__source = source

    def get_source(self):
        return self.__source

    def readfile(self):
        with open(self.__source) as file:
            data = json.load(file)
        return data