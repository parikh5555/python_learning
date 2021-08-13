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

