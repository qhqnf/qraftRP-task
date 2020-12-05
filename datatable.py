import os
from utils import line_parser


class DataTable:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(os.path.join(os.getcwd(), path)):
            raise FileNotFoundError(f"File name {path} not found")

    def __iter__(self):
        return self

    def find_n(self, n, where={}):
        # find_n 로직은 여기에 완성해주세요. #
        result = []
        with open(self.path, "r") as f:
            column_name = f.readline().rstrip("\n").split(",")

            # looping until find n items
            while len(result) < n:
                row = line_parser(f.readline().strip("\n"))
                row_dict = dict(zip(column_name, row))
                condition = where.copy()
                for key in where.keys():
                    if row_dict[key] != condition.pop(key):
                        break
                    if len(condition) == 0:
                        result.append(list(row_dict.values()))
                if row == [""]:
                    break

        return result

