import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

path_old = 'Data/Filtered CSV Data/backend_data_only_passed_old.csv'
path_new = 'Data/Filtered CSV Data/backend_data_only_passed_new.csv'

df_old = pd.read_csv(path_old, sep=',')
df_new = pd.read_csv(path_new, sep=',')
df_incdec_btns = df_new[df_new['identifier_simple'].isin(['Decrease', 'Increase'])]

user_ids_to_remove = ['1055255a-e78b-4c71-9d79-a9d29ddcd59d', '61a5a061-61b5-4f44-b07b-73843bfc6d3f'] #user ids used to test
user_ids_old = np.unique(np.array(df_old['player_id']))
user_ids_old = np.array([id for id in user_ids_old if id not in user_ids_to_remove])
user_ids_new = np.unique(np.array(df_new['player_id']))
user_ids_new = np.array([id for id in user_ids_new if id not in user_ids_to_remove])
user_ids_incdec_btns = np.unique(np.array(df_incdec_btns['player_id']))
user_ids_incdec_btns = np.array([id for id in user_ids_incdec_btns if id not in user_ids_to_remove])
user_ids_no_incdec_btns = np.array([id for id in user_ids_new if id not in user_ids_incdec_btns])
user_ids_no_incdec_btns = np.array([id for id in user_ids_no_incdec_btns if id not in user_ids_to_remove])
path_user_old = 'Data/User_Ids/user_ids_old_version.npy'
path_user_new = 'Data/User_Ids/user_ids_new_version.npy'
path_user_decinc_btns = 'Data/User_Ids/user_ids_decinc_btns.npy'
path_user_no_decinc_btns = 'Data/User_Ids/user_ids_no_decinc_btns.npy'
np.save(path_user_old, user_ids_old)
np.save(path_user_new, user_ids_new)
np.save(path_user_decinc_btns, user_ids_incdec_btns)
np.save(path_user_no_decinc_btns, user_ids_no_incdec_btns)