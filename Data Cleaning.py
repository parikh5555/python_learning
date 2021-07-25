#Import the libraries

import pandas as pd
import numpy as np

#Read CSV / Excel / SQL

sf_permits = pd.read_csv("../input/building-permit-applications-data/Building_Permits.csv")

# set seed for reproducibility
np.random.seed(0)

#Analyze how data frame looks like - First five columns
sf_permits.head()

#Check missing value
missing_values_count = sf_permits.isnull().sum() 
missing_values_count[0:10]  ## See how missing values looks

# how many total missing values do we have?
total_cells = np.product(sf_permits.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)

# 1. Fill NaN by 0
sf_permits.fillna(0, ,inplace = True)

# 2. Fill NaN by Mean of individual columns
sf_permits.fillna(sf_permits.mean(),inplace = True)

