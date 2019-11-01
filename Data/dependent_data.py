from Data.get_data import GetData
from Tools.operation_excel import OperationExcel
from Base.runmethod import RunMethod
from jsonpath_rw import *


class DependentData:

    def __init__(self, case_id, sheet_id):
        self.sheet_id = sheet_id
        self.case_id = case_id
        self.opera_excel = OperationExcel(self.sheet_id)
        self.data = GetData(self.sheet_id)

    # 通过case_id去获取关联前置case_id的整行数据
    def get_case_line_data(self, case_id):
        rows_data = self.opera_excel.get_rows_data(case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data, header)
        return res

    # 根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]


if __name__ == '__main__':
    order = {

        "code": 200,
        "data": {
            "data": [],
            "errorCode": 1006,
            "errorDesc": "token error",
            "status": 1,
            "timestamp": 1569152844632
        }
    }

    res = "data.errorDesc"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print([math.value for math in madle][0])
