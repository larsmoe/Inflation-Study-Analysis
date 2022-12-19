import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

path_filtered_clicks = 'Data/backend_data_only_passed.csv'
path_filtered_clicks_old = 'Data/backend_data_only_passed_old.csv'
path_filtered_clicks_new = 'Data/backend_data_only_passed_new.csv'

df_filtered_clicks = pd.read_csv(path_filtered_clicks, sep=',')
df_filtered_clicks_new = pd.read_csv(path_filtered_clicks_new, sep=',')
df_filtered_clicks_old = pd.read_csv(path_filtered_clicks_old, sep=',')

print(df_filtered_clicks_new)

num_of_unique_user = len(np.unique(np.array(df_filtered_clicks['player_id'])))
num_of_unique_user_new = len(np.unique(np.array(df_filtered_clicks_new['player_id'])))
num_of_unique_user_old = len(np.unique(np.array(df_filtered_clicks_old['player_id'])))

print(num_of_unique_user, num_of_unique_user_new, num_of_unique_user_old)
num_of_user_use_decinc_btns = len(np.unique(np.array(df_filtered_clicks_new[df_filtered_clicks_new['identifier_simple'].
                                                     isin(['Increase', 'Decrease'])]['player_id'])))
df_filtered_clicks_new['identifier_simple'].value_counts().plot(kind='bar')
print(num_of_user_use_decinc_btns)
plt.show()