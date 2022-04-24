""" Extract the knowledge from the .xlsx files. """
from os.path import expanduser, exists


class FileNotFound(Exception):

    def __init__(self):
        super(FileNotFound, self).__init__("File not found.")

    def __init__(self, file_path: str):
        super(FileNotFound, self).__init__(f"File not fount at {expanduser(file_path)}.")


def from_excel_file(file_path: str):
    from pandas import read_excel

    if not exists(expanduser(file_path)):
        raise FileNotFound(file_path)
        return
    else:
        data = list()
        raw_data = read_excel(expanduser(file_path), header=None, index_col=None, sheet_name=[0])

        for key in raw_data:
            for qa in raw_data[key].values:
                temp = list()
                ans = [str(list(qa)[1]).lower()]
                temp.append(list(qa)[0].lower())
                temp.append(ans)
                data.append(temp)
        return data


if __name__ == '__main__':
    print(from_excel_file("./References/Knowledgebase.xlsx"))
