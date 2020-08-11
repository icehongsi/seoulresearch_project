import pandas as pd



class address_to_code:
    def __init__(self, df): #dataframe as a input value #file_dir = "C:\Users\Youngju Hong\Documents\projectfile", address_file_name = ""):
        self.df = pd.read_excel("동코드.xlsx")

    def find_row_number(self, keyword, category):

    def import_data(self):
        while True:
            try:
                file_dir_to_modify = input("Input a file name w/ directory...")
                file_type = input("input file type without dots... (e.g. csv, xlsx...)\n")

                if file_type == "csv":
                    function = pd.read_csv
                elif file_type in ("xlsx", "xls"):
                    function = pd.read_excel
                elif file_type == "csv":
                    function = pd.read_csv
                elif file_type == "txt":
                    function = pd.read_table
                temp_data = function(file_type)
                break
            except Exception as e:
                print(e)

        return temp_data



        return file_dir_to_modify


