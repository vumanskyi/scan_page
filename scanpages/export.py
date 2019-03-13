import os

class Export:

    def __init__(self, filename, data):
        self.__filename = filename
        self.__data = data

    def get_filename(self):
        return self.__filename

    def get_data(self):
        return self.__data

    def import_data(self):
        f = open(os.path.abspath('export') + "/" +  self.__filename, "a")
        for k, v in self.__data.items():
            f.write(str(k) + ": " + str(v) + "\n")

        return 'ok'

