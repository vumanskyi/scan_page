import requests
from scanpages.response import Response
from scanpages.import_data import ImportData
from scanpages.export import Export


class Scanpage:

    def __init__(self):
        self.__page = None
        self.__filepath = None

    def set_page(self, page):
        self.__page = page

    def get_page(self):
        return self.__page

    def scan(self):
        r = requests.get(self.__page)

        response = Response(r)

        return response.get_status_code()

    def scan_from_file(self, filepath):
        read = ImportData(filepath)

        data = read.readfile()
        from_file = {}
        for k, v in data.items():
            r = requests.get(v)

            response = Response(r)
            from_file[k] = response.get_status_code()

        return  from_file

    def set_filepath(self, filepath):
        self.__filepath = filepath

    def get_filepath(self):
        return self.__filepath

    def scan_import(self, filename):
        read = ImportData(self.get_filepath())

        data = read.readfile()
        from_file = {}
        for k, v in data.items():
            r = requests.get(v)

            response = Response(r)
            from_file[k] = response.get_status_code()

        imp_data = Export(filename, from_file)

        return imp_data.import_data()



