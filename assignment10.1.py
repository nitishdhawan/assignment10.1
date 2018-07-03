
# coding: utf-8

# In[5]:


import pandas as pd

#Load the data set
baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
baby_names.info()


# In[4]:


baby_names.head()


# In[6]:


# Problem : 1. Delete unnamed columns
del baby_names['Unnamed: 0']
del baby_names['Id']
baby_names.head()


# In[7]:


baby_names['Gender'].value_counts()


# In[8]:


# Problem : 3. Show the top 5 most preferred names

# del baby_names["Year"]
# group the data
names = baby_names.groupby("Name").sum()

# print the first 5 observations
names.head()

# print the size of the dataset
print("Size :", names.shape)

# sort it from the biggest value to the smallest one
names.sort_values("Count", ascending = 0).head()


# In[9]:


# Problem : 4. What is the median name occurence in the dataset
names[names.Count == names.Count.median()]


# In[10]:


# Problem : 5. Distribution of male and female born count by states

baby_names.head()
baby_names.groupby(['Gender','State']).sum()

