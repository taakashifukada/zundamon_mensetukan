class TextFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_strings(self):
        with open(self.file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
