import xlrd
from xlutils.copy import copy
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(current_directory)


class OperationExcel:
    def __init__(self, sheet_id=None, file_name=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = root_path + '/Datapool/interface.xls'
            self.sheet_id = sheet_id
        self.data = self.get_data()

    # 获取哪张sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        return data.sheets()[self.sheet_id]

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某个单元格内容
    def get_cell_value(self, row, col):
        tables = self.data
        return tables.cell_value(row, col)

    '''
    写入excel数据
    row, col, value
    '''

    # 写入数据
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        # 指定写入哪张sheet下标从0开始
        sheet_data = write_data.get_sheet(self.sheet_id)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据对应的caseid找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        cols = self.get_cols_data()
        for col_data in cols:
            if case_id in col_data:
                return num
            num = num + 1

    # 根据行号，找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    opers = OperationExcel(0)
    print(opers.get_data())
    print(opers.get_lines())
    print(opers.get_cell_value(2, 3))
