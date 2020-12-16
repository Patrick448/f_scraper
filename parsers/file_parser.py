from typing import List, Dict
import xlrd

class CSVParser:
    def __init__(self, file_path):
        self.parsed_list = []
        with open(file_path, 'r', encoding='utf-8-sig') as file:

            lines = [line.strip() for line in file.readlines() if line.strip()]
            self.parsed_list = [line.split("\t") for line in lines]

    def get_column(self, index: int) -> List:
        column = [line[index] for line in self.parsed_list]
        return column
    

class ExcelParser:
    def __init__(self, file_path):
        self.file_path = file_path
    
    @property
    def get_file_as_dict_list(self) -> List[Dict]:
        workbook = xlrd.open_workbook(self.file_path)
        sheet = workbook.sheet_by_index(1)
        word_lists_by_date = []
        dates = []

        for i in range(1, sheet.nrows):
            table_row = sheet.row_values(i)
            
            if table_row[0] != '':
                word_lists_by_date.append({'date':'', 'words':[]})
                date = xlrd.xldate_as_datetime(float(table_row[0]), workbook.datemode)
                dates.append(date.strftime("%d/%m/%Y"))
                word_lists_by_date[-1]['date'] = date.strftime("%d/%m/%Y")

            word_lists_by_date[-1]['words'].append(table_row[1:])
        
        return word_lists_by_date


    def teste_func(self):
        path = 'C:/Users/patri/OneDrive/Desktop/Patrick/Vocab/VocabList-Mandarin.xlsx'
        workbook = xlrd.open_workbook(path)
        sheet = workbook.sheet_by_index(1)
        word_lists_by_date = []
        dates = []
        for i in range(1, sheet.nrows):
            table_row = sheet.row_values(i)
            
            if table_row[0] != '':
                word_lists_by_date.append({'date':'', 'words':[]})
                date = xlrd.xldate_as_datetime(float(table_row[0]), workbook.datemode)
                dates.append(date.strftime("%d/%m/%Y"))
                word_lists_by_date[-1]['date'] = date.strftime("%d/%m/%Y")

            word_lists_by_date[-1]['words'].append(table_row[1:])
        
        print(word_lists_by_date)
        print(dates)


if __name__ == "__main__":
    e = ExcelParser("")
    e.teste_func()

        
