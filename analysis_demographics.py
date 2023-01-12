import numpy as np
import pandas as pd
from scipy.stats import ttest_ind, mannwhitneyu

otree_path = 'Data/Filtered CSV Data/oTree_data_filtered.csv'
df_otree = pd.read_csv(otree_path, sep=',')
user_ids_new = np.load('Data/User_Ids/user_ids_new_version.npy')
user_ids_old = np.load('Data/User_Ids/user_ids_old_version.npy')
df_otree_old = df_otree[df_otree['participant.unique_id'].isin(user_ids_old)]
df_otree_new = df_otree[df_otree['participant.unique_id'].isin(user_ids_new)]

gender = np.array(df_otree['survey_part_1_cw.1.player.gender'])
gender_new = np.array(df_otree_new['survey_part_1_cw.1.player.gender'])
gender_old = np.array(df_otree_old['survey_part_1_cw.1.player.gender'])
num_of_gen_arr, num_of_gen_arr_new, num_of_gen_arr_old = np.zeros(4), np.zeros(4), np.zeros(4)

for i in [1,2,3,4]:
    num_of_gen_arr[i-1] = (gender==i).sum()
    num_of_gen_arr_new[i - 1] = (gender_new == i).sum()
    num_of_gen_arr_old[i - 1] = (gender_old == i).sum()
print(num_of_gen_arr, num_of_gen_arr_new, num_of_gen_arr_old)
print(ttest_ind(num_of_gen_arr_new, num_of_gen_arr_old, equal_var=False))

age = np.array(df_otree['survey_part_1_cw.1.player.age_category'])
age_new = np.array(df_otree_new['survey_part_1_cw.1.player.age_category'])
age_old = np.array(df_otree_old['survey_part_1_cw.1.player.age_category'])
num_of_age_arr, num_of_age_arr_new, num_of_age_arr_old = np.zeros(7), np.zeros(7), np.zeros(7)

for i in [1,2,3,4,5,6,7]:
    num_of_age_arr[i-1] = (age==i).sum()
    num_of_age_arr_new[i - 1] = (age_new == i).sum()
    num_of_age_arr_old[i - 1] = (age_old == i).sum()

print(num_of_age_arr, num_of_age_arr_new, num_of_age_arr_old)
print(ttest_ind(num_of_age_arr_new, num_of_age_arr_old, equal_var=False))

pers_exp = np.array(df_otree['survey_part_1_cw.1.player.personal_experience'])
pers_exp_new = np.array(df_otree_new['survey_part_1_cw.1.player.personal_experience'])
pers_exp_old = np.array(df_otree_old['survey_part_1_cw.1.player.personal_experience'])
num_of_pers_exp_arr, num_of_pers_exp_arr_new, num_of_pers_exp_arr_old = np.zeros(3), np.zeros(3), np.zeros(3)

for i in [1,2,3]:
    num_of_pers_exp_arr[i-1] = (pers_exp==i).sum()
    num_of_pers_exp_arr_new[i - 1] = (pers_exp_new == i).sum()
    num_of_pers_exp_arr_old[i - 1] = (pers_exp_old == i).sum()

print(num_of_pers_exp_arr, num_of_pers_exp_arr_new, num_of_pers_exp_arr_old)
print(ttest_ind(num_of_pers_exp_arr_new, num_of_pers_exp_arr_old, equal_var=False))

tool_exp = np.array(df_otree['survey_part_1_cw.1.player.tool_experience'])
tool_exp_new = np.array(df_otree_new['survey_part_1_cw.1.player.tool_experience'])
tool_exp_old = np.array(df_otree_old['survey_part_1_cw.1.player.tool_experience'])
num_of_tool_exp_arr, num_of_tool_exp_arr_new, num_of_tool_exp_arr_old = np.zeros(3), np.zeros(3), np.zeros(3)

for i in [1,2,3]:
    num_of_tool_exp_arr[i-1] = (tool_exp==i).sum()
    num_of_tool_exp_arr_new[i - 1] = (tool_exp_new == i).sum()
    num_of_tool_exp_arr_old[i - 1] = (tool_exp_old == i).sum()

print(num_of_tool_exp_arr, num_of_tool_exp_arr_new, num_of_tool_exp_arr_old)
print(ttest_ind(num_of_tool_exp_arr_new, num_of_tool_exp_arr_old, equal_var=False))