import pandas as pd
import numpy as np
from datetime import datetime
pd.set_option('display.max_columns', None)

click_data_path = 'Data/backend_data.csv'
otree_data_path = 'Data/oTree_data.csv'

click_df = pd.read_csv(click_data_path, sep=',')
otree_df = pd.read_csv(otree_data_path, sep=',')

otree_df_closing_passed = otree_df[otree_df['participant._current_page_name'] == 'Closing_passed']

all_ids_passed = np.array(otree_df_closing_passed['participant.unique_id'])

click_df_passed = click_df.loc[click_df['player_id'].isin(all_ids_passed)]
click_df_passed['created_at'] = click_df_passed['created_at'].map(lambda created_at: datetime.utcfromtimestamp(created_at).
                                                    strftime('%Y-%m-%d %H:%M:%S'))
click_df_passed_old = click_df_passed[click_df_passed['identifier'] == 'old']
click_df_passed_new= click_df_passed[click_df_passed['identifier'] == 'new']

path_filtered_clicks = 'Data/backend_data_only_passed.csv'
path_filtered_clicks_old = 'Data/backend_data_only_passed_old.csv'
path_filtered_clicks_new = 'Data/backend_data_only_passed_new.csv'
click_df_passed.to_csv(path_filtered_clicks, sep=',', index=False)
click_df_passed_old.to_csv(path_filtered_clicks_old, sep=',', index=False)
click_df_passed_new.to_csv(path_filtered_clicks_new, sep=',', index=False)