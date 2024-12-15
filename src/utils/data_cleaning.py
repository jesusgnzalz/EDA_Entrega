import pandas as pd

def clean_data(file_path):
    data = pd.read_csv(file_path)
    data['date'] = pd.to_datetime(data['date'])
    data = data.drop_duplicates()
    data = data.fillna(0)
    return data
