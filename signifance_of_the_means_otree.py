import numpy as np
from scipy.stats import ttest_ind
import pandas as pd


path_otree = 'Data/Filtered CSV Data/oTree_data_filtered.csv'
user_ids_new = np.load('Data/User_Ids/user_ids_new_version.npy', allow_pickle=True)
user_ids_old = np.load('Data/User_Ids/user_ids_old_version.npy', allow_pickle=True)
user_ids_decinc_btns = np.load('Data/User_Ids/user_ids_decinc_btns.npy', allow_pickle=True)
user_ids_no_decinc_btns = np.load('Data/User_Ids/user_ids_no_decinc_btns.npy', allow_pickle=True)
df_otree = pd.read_csv(path_otree, sep=',')
df_otree_old = df_otree[df_otree['participant.unique_id'].isin(user_ids_old)]
df_otree_new = df_otree[df_otree['participant.unique_id'].isin(user_ids_new)]
df_otree_decinc_btns = df_otree[df_otree['participant.unique_id'].isin(user_ids_decinc_btns)]
df_otree_no_decinc_btns = df_otree[df_otree['participant.unique_id'].isin(user_ids_no_decinc_btns)]

num_of_constructs = 5
list_of_df = [df_otree_old, df_otree_new, df_otree_no_decinc_btns, df_otree_decinc_btns]
for i in range(num_of_constructs):
    num_of_ques = 3
    construct_cols = []
    construct_arrays = []
    if i == num_of_constructs - 1:
        num_of_ques = 5
    for j in range(num_of_ques):
        construct_cols.append(f'survey_part_2.1.player.q{i*3 + j + 1}')
    for k in range(len(list_of_df)):
        construct_arrays.append((np.array(list_of_df[k][construct_cols])).flatten())
    for l in range(len(construct_arrays)):
        print(construct_arrays[l].mean())
    break

#construct1_new = (np.array(df_otree_no_decinc_btns[construct_cols])).flatten()
#print(construct1_new.mean(), construct1_old.mean())
#stat, p_val = ttest_ind(construct1_new, construct1_old, equal_var=False, alternative='greater')
#print(stat, p_val)
