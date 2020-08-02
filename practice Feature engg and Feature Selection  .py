#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os
os.chdir("D:\data")
df=pd.read_csv("melb_data.csv")
df.head()


# In[3]:


df.isnull().sum()


# In[5]:


df


# In[5]:


import matplotlib.pyplot as plt
df["Distance"].hist(bins=50)


# In[6]:


df["BuildingArea"].hist(bins=50)


# In[8]:


import seaborn as sns
sns.boxplot(df["BuildingArea"])


# In[10]:


df["BuildingArea"].describe()


# In[11]:


##finding the max of the boxplot 
max_boxplot=174+(1.5*(174-93))
max_boxplot


# In[18]:


df["BuildingArea"][df["BuildingArea"]>max_boxplot]=max_boxplot


# In[19]:


sns.boxplot(df["BuildingArea"])


# In[20]:


df["BuildingArea"].hist(bins=50)


# In[21]:


df["BuildingArea"].isnull().sum()


# In[27]:


df["BuildingArea"].dropna().sample(df["BuildingArea"].isnull().sum(),random_state=0)


# In[28]:


def impute_nan(df,variable,median):
    df[variable+"_median"]=df[variable].fillna(median)
    df[variable+"_random"]=df[variable]
    ##It will have the random sample to fill the na
    random_sample=df[variable].dropna().sample(df[variable].isnull().sum(),random_state=0)
    ##pandas need to have same index in order to merge the dataset
    random_sample.index=df[df[variable].isnull()].index
    df.loc[df[variable].isnull(),variable+'_random']=random_sample


# In[30]:


median=df["BuildingArea"].median()
median


# In[31]:


impute_nan(df,"BuildingArea",median)


# In[32]:


df.head(50)


# In[33]:


sns.boxplot(df["BuildingArea_median"])


# In[34]:


sns.boxplot(df["BuildingArea_random"])


# In[36]:


fig = plt.figure()
ax = fig.add_subplot(111)
df['BuildingArea'].plot(kind='kde', ax=ax)
###df["BuildingArea_median"].plot(kind="kde", ax=ax, color="red")
df.BuildingArea_random.plot(kind='kde', ax=ax, color='green')
lines, labels = ax.get_legend_handles_labels()
ax.legend(lines, labels, loc='best')


# In[39]:


df["BuildingArea_random"].hist(bins=50)


# In[40]:


df["BuildingArea"].hist(bins=50)


# #### taking titanic data set 

# In[41]:


tita=pd.read_csv("train.csv")
tita.head()


# In[42]:


sns.boxplot(tita["Age"])


# In[44]:


tita["Age"].describe()


# In[45]:


x=38+(1.5*(38-20.125))
x


# In[46]:


tita["Age"][tita["Age"]>x]=x


# In[47]:


sns.boxplot(tita["Age"])


# In[48]:


tita["Age"].isnull().sum()


# In[49]:


tita["Age"].dropna().sample(tita["Age"].isnull().sum(),random_state=0)


# In[55]:


def impute_nan1(df,variable,median):
    df[variable+"_median"]=df[variable].fillna(median)
    df[variable+"_random"]=df[variable]
    ##It will have the random sample to fill the na
    random_sample=df[variable].dropna().sample(df[variable].isnull().sum(),random_state=0)
    ##pandas need to have same index in order to merge the dataset
    random_sample.index=df[df[variable].isnull()].index
    df.loc[df[variable].isnull(),variable+'_random']=random_sample


# In[56]:


median=tita["Age"].median()
median


# In[57]:


impute_nan1(tita,"Age",median)


# In[63]:


sns.boxplot(tita["Age_median"])


# In[60]:


tita["Age"].hist(bins=50)


# In[61]:


tita["Age"].isnull().sum()


# In[65]:


fig = plt.figure()
ax = fig.add_subplot(111)
tita['Age'].plot(kind='kde', ax=ax)
tita["Age_median"].plot(kind="kde", ax=ax, color="red")
tita.Age_random.plot(kind='kde', ax=ax, color='green')
lines, labels = ax.get_legend_handles_labels()
ax.legend(lines, labels, loc='best')


# In[68]:


sns.boxplot(tita["Age"])


# In[67]:


sns.boxplot(tita["Age_median"])


# In[69]:


sns.boxplot(tita["Age_random"])


# In[ ]:




