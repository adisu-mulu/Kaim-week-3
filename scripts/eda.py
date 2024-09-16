import pandas as pd

class EDA:
    def __init__(self, path):
        self.path = path
    
    def fetch_data(self):
        data = pd.read_csv(self.path, sep="|", on_bad_lines='skip')
        return data