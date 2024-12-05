#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df =pd.read_csv("Zomato data .csv")
df


# In[14]:


def handelRate(value):
    value = str(value).split('/')   # split 4.1 / 5 split it
    value = value[0];
    return float(value)
df['rate'] = df['rate'].apply(handelRate)
print(df.head())


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[5]:


df.describe()


# In[6]:


df.duplicated().sum()


# In[7]:


df.shape


# In[8]:


df.columns


# In[9]:


correlation_matrix = df[['rate', 'votes', 'approx_cost(for two people)']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)


# In[10]:


print("\nUnique Values in Categorical Columns:")
for col in ['online_order', 'book_table', 'listed_in(type)']:
    print(f"{col}: {df[col].unique()}")


# In[11]:


print("\nAverage Cost for Two People by Restaurant Type:")
print(df.groupby('listed_in(type)')['approx_cost(for two people)'].mean())


# In[12]:


sorted_df = df.sort_values(by='rate', ascending=False)
print("\nDataFrame Sorted by Rating:")
print(sorted_df)


# types of resturent

# In[13]:


df.head()


# In[15]:


sns.countplot(x= df['listed_in(type)'])
plt.xlabel("type of resturant")


# In[100]:


# majority of the resturan falls in dinning category


# In[16]:


grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of restaurant", c="black", size=10)
plt.ylabel("votes", c="black", size=10)

# dinning resurant recive has maximum votes
# In[17]:


plt.hist(df['rate'],bins = 5)
plt.title("rating distribution")
plt.show()


# In[103]:


# majority restorant 3.5 to 4 


# In[18]:


couple_data = df['approx_cost(for two people)']
sns.countplot(x = couple_data)


# In[105]:


# the majority of couple prefer resturant with an approxi


# In[ ]:





# In[19]:


plt.figure(figsize=(6,6))
sns.boxplot(x = 'online_order', y ='rate', data = df)
plt.show()


# In[20]:


df = pd.DataFrame({
    'name': ['Restaurant A', 'Restaurant B', 'Restaurant C', 'Restaurant D'],
    'online_order': ['Yes', 'No', 'Yes', 'No'],
    'book_table': ['No', 'Yes', 'No', 'Yes'],
    'rate': [4.1, 3.5, 4.3, 4.0],
    'votes': [120, 45, 230, 150],
    'approx_cost(for two people)': [500, 800, 600, 750],
    'listed_in(type)': ['Buffet', 'Casual Dining', 'Cafe', 'Fine Dining']
})


# In[21]:


online_order_counts = df['online_order'].value_counts()
plt.figure(figsize=(8, 5))
online_order_counts.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Distribution of Online Orders')
plt.xlabel('Online Order')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()


# In[22]:


book_table_counts = df['book_table'].value_counts()
plt.figure(figsize=(8, 5))
book_table_counts.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightgreen'], startangle=90)
plt.title('Booking Table Options')
plt.ylabel('')
plt.legend(labels=book_table_counts.index, loc="upper right")
plt.show()


# In[29]:


plt.figure(figsize=(7, 4))
plt.plot(df['votes'], df['approx_cost(for two people)'], marker='o', linestyle='-', color='blue', label='Cost vs Votes')
plt.title('Votes vs Approx Cost for Two People')
plt.xlabel('Votes')
plt.ylabel('Approx Cost (for two people)')
plt.legend()
plt.grid(True)
plt.show()


# In[32]:


listed_type_counts = df['listed_in(type)'].value_counts()
plt.figure(figsize=(4, 4))
listed_type_counts.plot(kind='bar', color='teal')
plt.title('Distribution of Restaurant Types')
plt.xlabel('Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[34]:


plt.figure(figsize=(5, 3))
plt.boxplot(df['approx_cost(for two people)'], vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
plt.title('Boxplot of Approx Cost for Two People')
plt.xlabel('Approx Cost (for two people)')
plt.show()


# In[35]:


from pandas.plotting import scatter_matrix
scatter_matrix(df[['rate', 'votes', 'approx_cost(for two people)']], figsize=(6, 5), diagonal='kde', color='purple')
plt.suptitle('Scatter Matrix of Numeric Features')
plt.show()


# In[36]:


plt.figure(figsize=(7, 5))
correlation = df[['rate', 'votes', 'approx_cost(for two people)']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


# In[37]:


stacked_data = df.groupby(['online_order', 'book_table']).size().unstack()
stacked_data.plot(kind='bar', stacked=True, figsize=(7, 4), color=['orange', 'green'])
plt.title('Stacked Bar Chart of Online Order vs Booking Table')
plt.xlabel('Online Order')
plt.ylabel('Count')
plt.legend(title='Book Table')
plt.xticks(rotation=0)
plt.show()


# In[ ]:





# In[ ]:




