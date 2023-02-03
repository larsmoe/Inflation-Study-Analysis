import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu
import pandas as pd
pd.set_option('display.max_columns', None)

#load all necessary data
path_otree = 'Data/Filtered CSV Data/oTree_data_filtered.csv'
user_ids_new = np.load('Data/User_Ids/user_ids_new_version.npy', allow_pickle=True)
user_ids_old = np.load('Data/User_Ids/user_ids_old_version.npy', allow_pickle=True)
user_ids_decinc_btns = np.load('Data/User_Ids/user_ids_decinc_btns.npy', allow_pickle=True)
user_ids_no_decinc_btns = np.load('Data/User_Ids/user_ids_no_decinc_btns.npy', allow_pickle=True)
df_otree = pd.read_csv(path_otree, sep=',') #all users
df_otree_old = df_otree[df_otree['participant.unique_id'].isin(user_ids_old)] #all user old version
df_otree_new = df_otree[df_otree['participant.unique_id'].isin(user_ids_new)] #all user new version
df_otree_decinc_btns = df_otree[df_otree['participant.unique_id'].isin(user_ids_decinc_btns)] #all users (new versio) using the playing tool
df_otree_no_decinc_btns = df_otree[df_otree['participant.unique_id'].isin(user_ids_no_decinc_btns)] #all users (new version) not using the playing tool

#creating a list of all dataframes
list_of_df = [df_otree_old, df_otree_new, df_otree_no_decinc_btns, df_otree_decinc_btns]
#construct the row names
num_of_constructs = 5
versions = ['Old', 'New', 'New (no PT)', 'new (PT)']
stats = ['Mean', 'Std. Dev.', 'Median', 'Cronbachs Alpha']
row_names = []
for vers in versions:
    for stat in stats:
        row_names.append(f'{vers} {stat}')
row_names.append('p-Value (t-test) New vs. Old')
row_names.append('p-Value (t-test) (PT)  vs. Old')
row_names.append('p-Value (t-test) (PT) vs. New (no PT)')
row_names.append('p-Value (MWU) New vs. Old')
row_names.append('p-Value (MWU) (PT)  vs. Old')
row_names.append('p-Value (MWU) (PT) vs. New (no PT)')
row_names.append('statistic (PT) MWU')
#create the DatFrame everything is saved in
df_stat = pd.DataFrame(row_names, columns=['Discription'])

#creating an new column fo each construct
for i in range(num_of_constructs):
    num_of_ques = 3
    construct_cols = []
    construct_arrays = []
    constuct_array_non_flattened = []
    construct_eval_array = np.zeros(23) #array containing all values saved in the column
    if i == num_of_constructs - 1: #last question has five questons isntaed of three
        num_of_ques = 5
    for j in range(num_of_ques): #creating a list of all columns that need to be extracted from the raw dataframe
        construct_cols.append(f'survey_part_2.1.player.q{i*3 + j + 1}')
    for k in range(len(list_of_df)): #creating a list containing all raw answers from the corresponding construct
                                     #dependent on the version (and whether they used the PT). One list is flat and one
                                     #is seperate for each question (necessary for the cronbachs alpha)
        construct_arrays.append((np.array(list_of_df[k][construct_cols])).flatten())
        constuct_array_non_flattened.append((np.array(list_of_df[k][construct_cols])))
    for l in range(len(construct_arrays)): #calculating the mean, standard deviation and cronbachs alpha
                                           #for each version and adding it to the column array
        n = (constuct_array_non_flattened[l].shape)[1]
        construct_eval_array[4*l] = construct_arrays[l].mean()
        construct_eval_array[4*l+1] = construct_arrays[l].std()
        construct_eval_array[4*l+2] = np.median(construct_arrays[l])
        construct_eval_array[4*l+3] = n/(n-1) * (1 - np.sum(np.var(constuct_array_non_flattened[l], axis=0))/np.var(np.sum(constuct_array_non_flattened[l], axis=1)))
    arrays_to_test_against = [[1, 3, 3], [0, 0, 2]]
    for m in range(len(arrays_to_test_against[0])):
        arr1 = construct_arrays[arrays_to_test_against[0][m]]
        arr2 = construct_arrays[arrays_to_test_against[1][m]]
        teststat, p_val = ttest_ind(a=arr2, b=arr1, alternative='less', equal_var=False) #alternative='greater',
        stat_mwu, p_val_mwu = mannwhitneyu(x=arr2, y=arr1, alternative='less') #, alternative='greater'
        construct_eval_array[4*(len(construct_arrays))+m] = p_val
        construct_eval_array[4*(len(construct_arrays))+len(arrays_to_test_against[0])+m] = p_val_mwu
        if m == 0:
            construct_eval_array[len(construct_eval_array)-1] = stat_mwu
    df_stat = df_stat.assign(**{f'Konstrukt {i+1}':pd.Series(construct_eval_array).values})
print(df_stat[['Discription', 'Konstrukt 5']])
csv_path_save = 'Data/Analysis/significance_of_the_means_neq.csv'
df_stat.to_csv(csv_path_save, index=False, sep=',')

#construct1_new = (np.array(df_otree_no_decinc_btns[construct_cols])).flatten()
#print(construct1_new.mean(), construct1_old.mean())
#stat, p_val = ttest_ind(construct1_new, construct1_old, equal_var=False, alternative='greater')
#print(stat, p_val)
