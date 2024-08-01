import pandas as pd
import os

def load_csv_files(directory):
    """Load CSV files from 'directory'
    
    return pandas dataframe
    """
    dataframes = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath, sep=';',
                                       on_bad_lines='skip',
                                       encoding='latin-1',
                                       dtype='object')
            dataframes.append(df)
    return dataframes

if __name__ == "__main__":
    load_csv_files('data/raw/')
    print('Successful loading of data.')