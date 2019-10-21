import os, sys

current_directory = os.path.dirname(__file__)
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from base.runmethod import RunMethod
from data.dependent_data import DependentData
from data.get_data import GetData
from tools.commonutil import CommonUtil
import json


class RunTest:

    def __init__(self, sheet_id):
        self.sheet_id = sheet_id
        self.run_method = RunMethod()
        # 传递 sheet_id
        self.data = GetData(self.sheet_id)
        self.com_util = CommonUtil()

        '''
        # 获取excel行数,也就是case条数
        self.rows_count = self.data.get_case_lines()
        '''

    # 程序执行的
    def go_on_run(self, i):
        pass_count = []
        fail_count = []

        # 改成手动单个单个去执行每行
        is_run = self.data.get_is_run(i)
        if is_run:
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            header = self.data.is_header(i)
            request_data = self.data.get_data_for_json(i)
            expect = self.data.get_expect_data(i)
            # expect = self.data.get_expcet_data_for_sql(i)
            # 获取依赖case_id
            depend_case = self.data.is_depend(i)

            if depend_case != None:
                # 传case_id的值
                self.depend_data = DependentData(depend_case, self.sheet_id)
                # 获取的依赖响应数据
                depend_response_data = self.depend_data.get_data_for_key(i)
                # 获取依赖的key字段
                depend_key = self.data.get_depend_field(i)
                request_data[depend_key] = depend_response_data

            res = self.run_method.run_main(method, url, request_data, header)
            # 转str类型打印
            jres = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)

            if self.com_util.is_contain(expect, jres):
                self.data.write_result(i, 'PASS')
                pass_count.append(i)

            else:
                self.data.write_result(i, jres)
                fail_count.append(i)
                
            return expect, jres
