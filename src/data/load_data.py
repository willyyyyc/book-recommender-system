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
            df = pd.read_csv(filepath)
            dataframes.append(df)
    return dataframes