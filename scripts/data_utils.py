import pandas as pd

def read_data_in(file):
    "Finds header size, instructs pandas to skip appropriate number of rows and load data to DataFrame"
    with open(file) as f:
        skiprows = 0
        for i, line in enumerate(f.readlines()):
            if '/end_header' in line:
                skiprows = i+1
                break
    return pd.read_csv(file, skiprows=skiprows, delimiter='\t', header=0)