import json


class CarService:
    def __init__(self, filename: str):
        with open(filename) as json_file:
            try:
                self.data = json.load(json_file)
            except Exception as e:
                print(e)

    @staticmethod
    def _validate_data(data_to_validate):
        pass

    def __str__(self):
        return self.data

    def print_file(self):
        return self.data
