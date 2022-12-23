import pandas as pd
import numpy as np

path_otree = 'Data/Raw CSV Data/oTree_data.csv'
df_otree = pd.read_csv(path_otree)
columns = df_otree.columns
print(columns)
columns_to_keep = [6, 7, 8, 13, 15, 27, 28, 29, 30, 38, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                   61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
columns_to_drop = [columns[i] for i in range(len(columns)) if i not in columns_to_keep]
df_otree.drop(axis='columns', columns=columns_to_drop, inplace=True)
df_otree = df_otree[df_otree['session.code'] == '7ymv81x6']
df_otree = df_otree[df_otree['participant._current_page_name'] == 'Closing_passed']

path_to_save = 'Data/Filtered CSV Data/oTree_data_filtered.csv'
df_otree.to_csv(path_to_save, index=False, sep=',')