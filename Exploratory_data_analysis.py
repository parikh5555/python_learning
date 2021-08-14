#Shree Ganeshay Namah#

train = pd.read_csv('../input/train.csv')  ## Import CSV
test = pd.read_csv('../input/train.csv')  

quantitative = [f for f in train.columns if train.dtypes[f] != 'object']  ## Quantitative variables
quantitative.remove('SalePrice')
quantitative.remove('Id')
qualitative = [f for f in train.columns if train.dtypes[f] == 'object']  ## Categorial variables

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

# 3. Distribution of quantitative variables

f = pd.melt(train, value_vars=quantitative)
g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False)
g = g.map(sns.distplot, "value")

# Add missing as value for missing values in categorial 

for c in qualitative:
    train[c] = train[c].astype('category')
    if train[c].isnull().any():
        train[c] = train[c].cat.add_categories(['MISSING'])
        train[c] = train[c].fillna('MISSING')

        
## Box plot of categorial variables with respect to price to understand which varibles to select
def boxplot(x, y, **kwargs):
    sns.boxplot(x=x, y=y)
    x=plt.xticks(rotation=90)
f = pd.melt(train, id_vars=['SalePrice'], value_vars=qualitative)
g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
g = g.map(boxplot, "value", "SalePrice")

## Checking correlation of categorial variable with Anova
def anova(frame):
    anv = pd.DataFrame()
    anv['feature'] = qualitative
    pvals = []
    for c in qualitative:
        samples = []
        for cls in frame[c].unique():
            s = frame[frame[c] == cls]['SalePrice'].values
            samples.append(s)
        pval = stats.f_oneway(*samples)[1]
        pvals.append(pval)
    anv['pval'] = pvals
    return anv.sort_values('pval')

a = anova(train)
a['disparity'] = np.log(1./a['pval'].values)
sns.barplot(data=a, x='feature', y='disparity')
x=plt.xticks(rotation=90)

## Encoding all categorial variables 

def encode(frame, feature):
    ordering = pd.DataFrame()
    ordering['val'] = frame[feature].unique()  ## ALl unique values of categorial variables
    ordering.index = ordering.val
    ordering['spmean'] = frame[[feature, 'SalePrice']].groupby(feature).mean()['SalePrice']  ## Group feature by mean sale price
    ordering = ordering.sort_values('spmean')  ## Sort feature by mean saleprice
    ordering['ordering'] = range(1, ordering.shape[0]+1)
    ordering = ordering['ordering'].to_dict()
    
    for cat, o in ordering.items():
        frame.loc[frame[feature] == cat, feature+'_E'] = o

qual_encoded = []
for q in qualitative:  
    encode(train, q)
    qual_encoded.append(q+'_E')
print(qual_encoded)

#Correlation

def spearman(frame, features):
    spr = pd.DataFrame()
    spr['feature'] = features
    spr['spearman'] = [frame[f].corr(frame['SalePrice'], 'spearman') for f in features]  #Correlation of all features with Price
    spr = spr.sort_values('spearman')
    plt.figure(figsize=(6, 0.25*len(features)))
    sns.barplot(data=spr, y='feature', x='spearman', orient='h')  ## Horizontal bar plot of comparison of all correlation
    
features = quantitative + qual_encoded
spearman(train, features)

# Heat map correlation

plt.figure(1)
corr = train[quantitative+['SalePrice']].corr()  # Correlation of numberical
sns.heatmap(corr)
plt.figure(2)
corr = train[qual_encoded+['SalePrice']].corr()  # Correlation of categorial 
sns.heatmap(corr)
plt.figure(3)
corr = pd.DataFrame(np.zeros([len(quantitative)+1, len(qual_encoded)+1]), index=quantitative+['SalePrice'], columns=qual_encoded+['SalePrice'])
for q1 in quantitative+['SalePrice']:
    for q2 in qual_encoded+['SalePrice']:
        corr.loc[q1, q2] = train[q1].corr(train[q2])
sns.heatmap(corr)

