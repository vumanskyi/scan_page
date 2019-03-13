class Response:

    def __init__(self, client):
        self.__client = client

    def get_status_code(self):
        return self.__client.status_code


