from Tools.connect_db import OperationSql
from Tools.operation_excel import OperationExcel
from Tools.operation_json import OperationJson
from Data import data_config


class GetData:

    def __init__(self, sheet_id):
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(self.sheet_id)

    # 去获取exce1行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取case_id
    def get_caseId(self, row):
        col = data_config.get_id()
        Id = self.opera_excel.get_cell_value(row, col)
        return Id

    # 获取是否执行
    def get_is_run(self, row):
        col = data_config.get_run()
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            return True
        else:
            return False

    # 是否携带header
    def is_header(self, row):
        col = data_config.get_header()
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = data_config.get_run_way()
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    # 获取ur1
    def get_request_url(self, row):
        col = data_config.get_url()
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = data_config.get_data()
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expect_data(self, row):
        col = data_config.get_expect()
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == "":
            return None
        return expect

    # 通过sq1获取预期结果
    def get_expcet_data_for_sql(self, row):
        op_sql = OperationSql()
        sql = self.get_expect_data(row)
        res = op_sql.search_one(sql)
        return res
        # return res.encode("unicode-escape').decode('string_escape')

    # 实际结果
    def write_result(self, row, value):
        col = data_config.get_result()
        return self.opera_excel.write_value(row, col, value)

    # 获取依赖数据的key
    def get_depend_key(self, row):
        col = data_config.get_data_depend()
        depent_key = self.opera_excel.get_cell_value(row, col)
        if depent_key == "":
            return None
        else:
            return depent_key

    # 判断是否有case依赖
    def is_depend(self, row):
        col = data_config.get_case_depend()
        depend_case_id = self.opera_excel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段
    def get_depend_field(self, row):
        col = data_config.get_field_depend()
        depend_field = self.opera_excel.get_cell_value(row, col)
        if depend_field == "":
            return None
        else:
            return depend_field
