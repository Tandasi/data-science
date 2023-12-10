#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize']=[13,6]


# In[2]:


df=pd.read_csv("C:/Users/giftt/Desktop/hotel booking.csv")
df.head(10)


# In[3]:


df.shape


# In[4]:


df.info()


# In[5]:


df.nunique()


# In[6]:


df.columns


# In[7]:


df=df.drop(['repeated','P-C', 'P-not-C'],axis=1)
df.head()


# In[10]:


df.nunique()


# In[10]:


len(df.columns)


# In[11]:


df.select_dtypes(include=np.number).columns


# In[12]:


r=6
c=3
it=1
for i in df.select_dtypes(include=np.number).columns:
    plt.subplot(r,c,it)
    sns.kdeplot(df[i])
    plt.grid()
    it+=1
plt.tight_layout()
plt.show()


# In[13]:


sns.pairplot(df.select_dtypes(include=np.number))
plt.grid()
plt.show()


# In[18]:


plt.pie(x=df['booking status'].value_counts().values,labels=df['booking status'].unique(),autopct='%.0f%%')
plt.xlabel('booking status')
plt.title('booking status Class Distribution')
plt.show()


# In[20]:


df.head(10)


# In[28]:


table1=pd.crosstab(df['type of meal'],df['booking status'])
table2=pd.crosstab(df['room type'],df['booking status'])
table3=pd.crosstab(df['market segment type'],df['booking status'])
display(table1)
display(table2)
display(table3)


# In[25]:


import scipy.stats as st
_,p,dof,arr=st.chi2_contingency(table1)
print('table 1 p value: ',p)
_,p,dof,arr=st.chi2_contingency(table2)
print('table 2 p value: ',p)
_,p,dof,arr=st.chi2_contingency(table3)
print('table 3 p value: ',p)


# In[9]:


df = df.groupby(by = 'Bookind_ID').max()['lead time', 'avarage price']


# In[ ]:




