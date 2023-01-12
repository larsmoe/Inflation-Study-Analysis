import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta

path_new = 'Data/Filtered CSV Data/backend_data_only_passed_new.csv'
path_old = 'Data/Filtered CSV Data/backend_data_only_passed_old.csv'

df_new = pd.read_csv(path_new, sep=',')
df_old = pd.read_csv(path_old, sep=',')

all_ids_old = np.unique(np.array(df_old['player_id']))
seconds_on_the_site_old = []
for id in all_ids_old:
    df_old_id = df_old[df_old['player_id']==id]
    time_arr = np.array(df_old_id['created_at_ws'])
    if len(time_arr) > 1:
        begin = datetime.strptime(np.min(time_arr), '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime(np.max(time_arr), '%Y-%m-%d %H:%M:%S')
        seconds_on_the_site_old.append((end-begin).total_seconds())

all_ids_new = np.unique(np.array(df_new['player_id']))
seconds_on_the_site_new = []
for id in all_ids_new:
    df_new_id = df_new[df_new['player_id']==id]
    time_arr = np.array(df_new_id['created_at_ws'])
    if len(time_arr) > 1:
        begin = datetime.strptime(np.min(time_arr), '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime(np.max(time_arr), '%Y-%m-%d %H:%M:%S')
        seconds_on_the_site_new.append((end-begin).total_seconds())

print(np.mean(np.sort(seconds_on_the_site_old)[:-1]), np.mean(np.sort(seconds_on_the_site_new)[:-1]), np.median(seconds_on_the_site_old), np.median(seconds_on_the_site_new))
print(np.sort(seconds_on_the_site_old)[-5:], np.sort(seconds_on_the_site_new)[-5:])