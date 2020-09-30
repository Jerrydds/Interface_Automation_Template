import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(current_directory)


class OperationJson:

    def __init__(self):
        self.data = self.read_data()

    # 获取json文件
    def read_data(self):
        with open(root_path + '/Datapool/user.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)
            return self.data

    # 根据关键字获取数据
    def get_data(self, name1):
        return self.data[name1]


if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data("login"))
