#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Testing|')


# In[2]:


#Visual Analysis of Imputational Technique
'''Use a dataset with missing value.Apply mean,median and mode imputaion to handle the missing data. Then create pair plots
using Seaborn, before and after the imputation. How do the relationhipsfeatures change after each imputational method?'''


# In[4]:


import pandas as pd
data=pd.read_csv('Diabetes Missing Data.csv')
data


# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[6]:


print(data.head())
print(data.isnull().sum())


# In[7]:


# Pair plot before imputation
sns.pairplot(data)
plt.title("Pair Plot Before Imputation")
plt.show()


# In[8]:


# Pair plot before imputation
sns.pairplot(data)
plt.title("Pair Plot Before Imputation")
plt.show()


# In[9]:


mean_imputed_data = data.copy()
# Impute missing values with mean
for column in ['Glucose', 'Diastolic_BP', 'Skin_Fold', 'Serum_Insulin', 'BMI', 'Diabetes_Pedigree', 'Age']:
    mean_imputed_data[column].fillna(mean_imputed_data[column].mean(), inplace=True)

# Pair plot after mean imputation
sns.pairplot(mean_imputed_data)
plt.title("Pair Plot After Mean Imputation")
plt.show()


# In[10]:


median_imputed_data = data.copy()
# Impute missing values with median
for column in ['Glucose', 'Diastolic_BP', 'Skin_Fold', 'Serum_Insulin', 'BMI', 'Diabetes_Pedigree', 'Age']:
    median_imputed_data[column].fillna(median_imputed_data[column].median(), inplace=True)

# Pair plot after median imputation
sns.pairplot(median_imputed_data)
plt.title("Pair Plot After Median Imputation")
plt.show()


# In[11]:


mode_imputed_data = data.copy()
# Impute missing values in the Class column with mode
mode_imputed_data['Class'].fillna(mode_imputed_data['Class'].mode()[0], inplace=True)

# Pair plot after mode imputation
sns.pairplot(mode_imputed_data)
plt.title("Pair Plot After Mode Imputation")
plt.show()


# In[ ]:




