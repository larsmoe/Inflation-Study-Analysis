import numpy as np
import pandas as pd

path_new_be = 'Data/Filtered CSV Data/backend_data_only_passed_new.csv'
path_old_be = 'Data/Filtered CSV Data/backend_data_only_passed_old.csv'
path_otree = 'Data/Filtered CSV Data/oTree_data_filtered.csv'

df_new = pd.read_csv(path_new_be, sep=',')
df_old = pd.read_csv(path_old_be, sep=',')
df_otree = pd.read_csv(path_otree, sep=',')

df_new_only_submit = df_new[df_new['identifier']=='Submit']
player_id_new_submit = np.array(df_new_only_submit['player_id'])
u, c = np.unique(player_id_new_submit, return_counts=True)
all_user_with_multiple_submits_new = u[c>1]
df_new_multiple_submits = df_new_only_submit[df_new_only_submit['player_id'].isin(all_user_with_multiple_submits_new)]


df_old_only_submit = df_old[df_old['identifier']=='Submit']
player_id_old_submit = np.array(df_old_only_submit['player_id'])
u, c = np.unique(player_id_old_submit, return_counts=True)
all_user_with_multiple_submits_old = u[c>1]
df_old_multiple_submits = df_old_only_submit[df_old_only_submit['player_id'].isin(all_user_with_multiple_submits_old)]
print(len(all_user_with_multiple_submits_new), len(all_user_with_multiple_submits_old))
df_otree_multiple_submits_new = df_otree[df_otree['participant.unique_id'].isin(all_user_with_multiple_submits_new)]
df_otree_multiple_submits_old = df_otree[df_otree['participant.unique_id'].isin(all_user_with_multiple_submits_old)]

path_to_save_new = 'Data/Analysis/multiple_submits_new.csv'
path_to_save_old = 'Data/Analysis/multiple_submits_old.csv'
path_to_save_new_otree = 'Data/Analysis/multiple_submits_new_otree.csv'
path_to_save_old_otree = 'Data/Analysis/multiple_submits_old_otree.csv'
df_new_multiple_submits.to_csv(path_to_save_new, index=False, sep=',')
df_old_multiple_submits.to_csv(path_to_save_old, index=False, sep=',')
df_otree_multiple_submits_new.to_csv(path_to_save_new_otree, index=False, sep=',')
df_otree_multiple_submits_old.to_csv(path_to_save_old_otree, index=False, sep=',')

