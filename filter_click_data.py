import pandas as pd
import numpy as np
from datetime import datetime
pd.set_option('display.max_columns', None)

click_data_path = 'Data/backend_data.csv'
otree_data_path = 'Data/oTree_data.csv'

click_df = pd.read_csv(click_data_path, sep=',')
otree_df = pd.read_csv(otree_data_path, sep=',')

#filter all participants who passed the test (in the otree df)
otree_df_closing_passed = otree_df[otree_df['participant._current_page_name'] == 'Closing_passed']
otree_df_closing_passed = otree_df_closing_passed[otree_df_closing_passed['session.code'] == '7ymv81x6']
all_ids_passed = np.array(otree_df_closing_passed['participant.unique_id'])
#using the filter from above to filter all passing particapants in the backend df
click_df_passed = click_df.loc[click_df['player_id'].isin(all_ids_passed)]
#changing the time from utc to normal timestamp
created_at_ws = np.array(click_df_passed['created_at_ws'])
click_df_passed['created_at'] = click_df_passed['created_at'].map(lambda created_at: datetime.utcfromtimestamp(created_at).
                                                    strftime('%Y-%m-%d %H:%M:%S'))
click_df_passed['created_at_ws'] = click_df_passed['created_at_ws'].map(lambda created_at_ws: datetime.utcfromtimestamp(created_at_ws/1000).strftime('%Y-%m-%d %H:%M:%S'))
#creating one df for each version (old vs. new inflationrechner)
click_df_passed_old = click_df_passed[click_df_passed['version'] == 'old']
click_df_passed_new= click_df_passed[click_df_passed['version'] == 'new']

#summarizing the clicks on the increase and decrease button
simplify_dict = {'Begin': 'Begin', 'Submit': 'Submit', 'positiveFeedback': 'Feedback', 'decrease_1': 'Decrease',
                 'decrease_2': 'Decrease', 'decrease_3': 'Decrease', 'increase_1': 'Increase',
                 'increase_2': 'Increase', 'increase_3': 'Increase', 'input-field': 'Input'}
click_df_passed_new['identifier_simple'] = click_df_passed_new['identifier'].map(simplify_dict)

#saving the data
path_filtered_clicks = 'Data/backend_data_only_passed.csv'
path_filtered_clicks_old = 'Data/backend_data_only_passed_old.csv'
path_filtered_clicks_new = 'Data/backend_data_only_passed_new.csv'
click_df_passed.to_csv(path_filtered_clicks, sep=',', index=False)
click_df_passed_old.to_csv(path_filtered_clicks_old, sep=',', index=False)
click_df_passed_new.to_csv(path_filtered_clicks_new, sep=',', index=False)