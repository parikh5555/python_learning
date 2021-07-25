## Import and read


import pandas as pd
url / file path to variable  -- resuable
df = pd.read_csv(url / file path, headers)  --df will be pandas dataframe which will have all data of headers mentioned in URL/File path
read_csv can be read_jsom / read_excel/ read_sql

default header can be replaced by df. columns = headers   -- where header is list [a,b,c...]

to Export dataframe to file
path = 'File path'
df.to_csv(path)   --- Same way df to json/excel/sql

Printing data
df  -- Print dataframe
df.head(n)  -- top n rows
df.tail(n)  -- bottom n rows
df.dtypes -- data types of columns
df.describe -- Statistical summary of data  (with include="all") gives summary of all columns
df.info() -- Provides first and last 30 rows of dataframe
df["header"].max() -- Max value from argument "header"
df["header"].min() -- Min value from argument "header"
df["header"].mean() -- Mean value from argument "header"
df["header"].std() -- Standard deviation value from argument "header"
df["header"].value_count() -- return count of values present in header 

replace the "?" symbol with NaN   -- To remove all NaN object replace and remove
df=df1.dropna(subset=["price"], axis=0)

## Wrangling 
1. Remove or correct missing values  -- 0/NaN/?/ [blank]  -- Drop missing / replace data by average or most common like most frequent
   df.dropna(subset = ["column header"], axis = 0, inplace = True)  -- remove all NaN data from column having header column header, 0 for row and 1 for column, inplace = true 
   replace and update the dataframe without that nothing happens
   
   df.replace["column header"].replace(np.nan, mean = df["column header].mean) -- replace use to replace (values to be replaced, to updated values to replace)
2. Normalization / Formatting --  Ahmedabad/A'bad/Ahmadabad -- Same way as replace we can use 
   For Normalization 
   1. Scaling (Xold/Xmax)  -- df[""]=df[""]/df[""].max()   -- Max maximum value
   2. Min-Max (Xold-Xmin/Xmax-Xmin) 
   3. Z score (Xold - Mu / Sigma)  -- Mu is average and Sigma is Std.deviation 

3. Centering / Scaling
   df["Price in USD"]= df["Price in USD"]*78  -- USD to INR Applying calculation to entire column
   df.rename(columns={"USD","INR"},inplace=True)
4. Convert to correct data type
   df["Price in USD"] = df.["Price in USD"].asype("int")  -- Converts data type of column header "Price in USD" to integer  -- Useful if not integer

5. Binning
   bins = np.linespace(min(df["Price"]), max(df["Price"]), 4) -- converts 4 equal parts between max and min prices -- 4 parts so 3 bins
   group_names = ["low", "med, "high"]
   df["price_binned"] = pd.cut(df["price"], bins, lables = group_names, include_lowest=True) -- Cut and store sorted data values into bins

6. Categorial variable to Quantatitive variable 
   pd.get_dummies(df["fuel"]) -- Converts gas or diesel seperate row headers and assign 1 or 0 to each

7. Groupby
   df_test = df[["Param1", "Param2", "Param3"]] -- Will make new dataframe df_test and copy column name param1, param2 and 3 into it
   df_grp = df_test.groupby(['Param1','Param2'], as_index=False).mean()  -- Creates new dataframe named df_grp having param1 and param2 value grouped by and mean of param3
   
8. Pivot tables
   df_pivot = df_grp.pivot(index="param1", columns="param2") -- Will convert above group by params to show in different columns of param2 vs rows of param1

9. Date Parsing
   df['date_parsed'] = pd.to_datetime(df['date'], format="%m/%d/%y") -- If date is not date time format it needs to be parsed for better representation          
   
##Correlation
df.corr() -- Returns dataframe of correlation

##Access Column
df["column header"]   -- Returns column values of passed argument "column header"
df["column header"] + n   -- To add / subtract n value to all the elements of complete column "column header"
df.drop(['A'], axis = 1)  -- To remove A column from dataframe
new = df[['column1', 'column2']]  -- To copy column 1 and 2 to new dataframe from old

##Remove Ourliers
q_low = df["col"].quantile(0.01)
q_hi  = df["col"].quantile(0.99)
df_filtered = df[(df["col"] < q_hi) & (df["col"] > q_low)]

## .loc Access specific rows and columns by lables
df.loc[[row1,row2],[column1,column2]]  # Returns sub table of row1,row2,column1,column2
