#Shree Ganeshay Namah#

#Below are the basic exploratory data analysis and data cleaning techniques that can be used 

# 1. Missing values understand
# To compare missing values in data

missing = train.isnull().sum()  ##train is pandas data frame 
missing = missing[missing > 0]
missing.sort_values(inplace=True)
missing.plot.bar()

# it's very important to understand the missing values parameter impact
# 


# 2. Dsitribution of Output paramter of training dataset

import scipy.stats as st
y = train['SalePrice']   ##Parameter to predict
plt.figure(1); plt.title('Johnson SU')
sns.distplot(y, kde=False, fit=st.johnsonsu)
plt.figure(2); plt.title('Normal')
sns.distplot(y, kde=False, fit=st.norm)
plt.figure(3); plt.title('Log Normal')
sns.distplot(y, kde=False, fit=st.lognorm)

# It'll give the idea how output parameter is distributed
# So one can get idea whether linear regression would be applicable or not
