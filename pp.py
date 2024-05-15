print("Hello World")
def validate_json_file(self,Menu.json):
        '''
        Ensure a given JSON file is valid.
        :param filename: full file path
        :return:
        '''
        self.log.info(f"Validating JSON file {filename}")
        with open(filename, encoding="utf-8") as data_file:
            file = filename.replace(self.filename, '')
            try:
                json.load(data_file)
            except ValueError as error:
                print("eroor") 
