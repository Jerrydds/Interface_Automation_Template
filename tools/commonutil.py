import json
from operator import *


class CommonUtil:
    def is_contain(self, str_one, str_two):

        """
        判断一个字符串是否再另外一个字符串中
        str_one：查找的字符串
        str_two：被查找的字符串
        """

        flag = None

        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self, dict_one, dict_two):
        # 判断是否是str类型
        if isinstance(dict_one, str):
            # 字符串转dict类型
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        # 判断两个字典是否相等
        return eq(dict_one, dict_two)
