import numpy as np
from scipy.stats import ttest_ind
import pandas as pd

path_otree = 'Data/oTree_data_filtered.csv'
df_otree = pd.read_csv(path_otree, sep=',')
print(df_otree)

