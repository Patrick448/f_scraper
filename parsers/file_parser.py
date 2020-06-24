class CSVParser:
    def __init__(self, file_path):
        parsed_list = []
        with open(file_path, 'r', encoding='utf-8-sig') as file:

            lines = [line.strip() for line in file.readlines() if line.strip()]
            self.parsed_list = [line.split("\t") for line in lines]

    def get_column(self, index):
        column = [line[index] for line in self.parsed_list]
        return column

