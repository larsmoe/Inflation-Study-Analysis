import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

path_filtered_clicks = 'Data/backend_data_only_passed.csv'
path_filtered_clicks_old = 'Data/backend_data_only_passed_old.csv'
path_filtered_clicks_new = 'Data/backend_data_only_passed_new.csv'
path_otree = 'Data/oTree_data.csv'

df_filtered_clicks = pd.read_csv(path_filtered_clicks, sep=',')
df_filtered_clicks_new = pd.read_csv(path_filtered_clicks_new, sep=',')
df_filtered_clicks_old = pd.read_csv(path_filtered_clicks_old, sep=',')
df_otree = pd.read_csv(path_otree, sep=',')
df_otree_passed = df_otree[df_otree['participant._current_page_name']=='Closing_passed']
df_otree_passed = df_otree_passed[df_otree_passed['session.code'] == '7ymv81x6']
print(df_otree_passed.shape)

num_of_unique_user = len(np.unique(np.array(df_filtered_clicks['player_id'])))
num_of_unique_user_new = len(np.unique(np.array(df_filtered_clicks_new['player_id'])))
num_of_unique_user_old = len(np.unique(np.array(df_filtered_clicks_old['player_id'])))

print(num_of_unique_user, num_of_unique_user_new, num_of_unique_user_old)
userids_use_decinc_btns = np.unique(np.array(df_filtered_clicks_new[df_filtered_clicks_new['identifier_simple'].
                                                     isin(['Increase', 'Decrease'])]['player_id']))
num_of_user_use_decinc_btns = len(userids_use_decinc_btns)
df_filtered_clicks_new['identifier_simple'].value_counts().plot(kind='bar')
print(num_of_user_use_decinc_btns)
#plt.show()
num_of_user_submitting_new = len(np.unique(np.array(df_filtered_clicks_new[df_filtered_clicks_new['identifier'].
                                                     isin(['Submit'])]['player_id'])))
num_of_user_submitting_old = len(np.unique(np.array(df_filtered_clicks_old.loc[df_filtered_clicks_old['identifier']=='Submit']['player_id'])))
num_of_users_submitting_total = len(np.unique(np.array(df_filtered_clicks.loc[df_filtered_clicks['identifier'] == 'Submit']['player_id'])))
# = df_filtered_clicks.loc[df_filtered_clicks['identifier'] == 'Submit']# == 'Submit']#['player_id']
print(num_of_user_submitting_old, num_of_user_submitting_new, num_of_users_submitting_total)

df_otree_user_decins_btns = df_otree[df_otree['inflation_calculator.1.player.unique_id'].isin(userids_use_decinc_btns)]
df_otree_user_no_decins_btns = df_otree[~df_otree['inflation_calculator.1.player.unique_id'].isin(userids_use_decinc_btns)]
print(df_otree_user_no_decins_btns.shape)
path_to_save_otree_filtered = 'Data/oTree_data_only_users_decinc_btns.csv'
path_to_save_otree_filtered_ii = 'Data/oTree_data_only_users_no_decinc_btns.csv'
df_otree_user_decins_btns.to_csv(path_to_save_otree_filtered, index=False, sep=',')
df_otree_user_no_decins_btns.to_csv(path_to_save_otree_filtered_ii, index=False, sep=',')