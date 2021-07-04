import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 

df = pd.read_csv(url / file path, headers)  --df will be pandas dataframe which will have all data of headers mentioned in URL/File path
y = df["param1"]
x = df["param2"]

fig = plt.figure(figsize =(10, 7))  -- Size of figure 

# Create a dot on x,y position
plt.plot(x,y,'o')

# Creating plot
plt.boxplot(x)  -- Create box plot of x -- param2 
plt.scatter(x,y)  -- Create scatter plot of x vs y


plt.title("My title of the plot will come here")
plt.xlable("Label of X axis")
plt.ylable("Label of Y axis")

plt.show()  --show plot


#heatmap
plt.pcolor(df_pivot, cmap="RdBu")   -- Red blue
plt.colorbar()  

#Regression plot for model evaluation
sns.regpot( x = "parameter of x", y ="paramter for y", data = dataframe)

#Residual plot for error in prediction
sns.regpot( data1, data2)  -- Where data1 and data2 are parameters for which we're seeking relationship

#Distribution plot to evaluate the model work
ax1 = sns.distplot(df[prediction], label = "Actual value")
sns.distplot(Yhat, label = "Fitted values", ax=ax1)
