import pandas as pd
import numpy as np

path_old = 'Data/Filtered CSV Data/oTree_data_filtered_old_version_strong_filter.csv'
df_old = pd.read_csv(path_old, sep=';')
df_old.to_csv(path_old, sep=',', index=False)
path_new = 'Data/Filtered CSV Data/oTree_data_filtered_new_version_strong_filter.csv'
df_new = pd.read_csv(path_new, sep=';')
df_new.to_csv(path_new, sep=',', index=False)