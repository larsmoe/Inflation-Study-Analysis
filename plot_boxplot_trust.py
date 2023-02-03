import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

trust_questions_col_names = ['survey_part_2.1.player.q13','survey_part_2.1.player.q14','survey_part_2.1.player.q15',
                             'survey_part_2.1.player.q16','survey_part_2.1.player.q17']
path_old = 'Data/Filtered CSV Data/oTree_data_filtered_old_version.csv'
df_old = pd.read_csv(path_old, sep=',')
df_old_trust = df_old[trust_questions_col_names]
trust_old_arr = df_old_trust.to_numpy().flatten()
path_new = 'Data/Filtered CSV Data/oTree_data_filtered_new_version.csv'
df_new = pd.read_csv(path_new, sep=',')
df_new_trust = df_new[trust_questions_col_names]
trust_new_arr = df_new_trust.to_numpy().flatten()
plt.boxplot([trust_new_arr, trust_old_arr], showmeans=True)
plt.show()