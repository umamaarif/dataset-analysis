#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
import plotly.io as pio


# In[5]:


umama_dataset = pd.read_csv('C:\\Users\DELL\Downloads\\BigBasket Products.csv', index_col=0)

  #  'C:\\Users\DELL\Downloads\\store.csv'


# In[8]:


umama_dataset.head(10)


# In[6]:


umama_dataset.sample(10)


# In[9]:


# Plot to see null values in our data
sns.heatmap(umama_dataset.isnull(), cbar=False)


# In[10]:


# Null Value Percentage Per column
percent_missing = umama_dataset.isnull().sum() * 100 / len(umama_dataset)
missing_value_umama_dataset = pd.DataFrame({'column_name': umama_dataset.columns,
                                 'percent_missing': percent_missing})
missing_value_umama_dataset


# In[11]:


# Print all unique catagories present in Dataset
for elem in umama_dataset['category'].unique():
    print(elem)


# In[12]:


# Print all unique sub_category present in Dataset
for elem in umama_dataset['sub_category'].unique():
    print(elem)


# In[13]:


percent_missing = umama_dataset.isnull().sum() * 100 / len(umama_dataset)
missing_value_umama_dataset = pd.DataFrame({'column_name': umama_dataset.columns,
                                 'percent_missing': percent_missing})
missing_value_umama_dataset


# In[25]:


data = umama_dataset
AVG_DF = data[['category','rating', 'market_price', 'sale_price']].groupby(['category']).mean().reset_index().sort_values('rating', ascending = False)


# In[15]:


AVG_DF


# In[16]:


AVG_RATING_df = AVG_DF.head(9).sort_values('rating', ascending = False)

fig = px.bar(AVG_RATING_df, x='category', y='rating', template = 'plotly_dark', title='Ranking of Catagories WRT Rating', color='rating', height=800)
fig.update_xaxes(tickangle=90, rangeselector_font_size=8)
fig.show()


# In[17]:


avg_market_price_df = AVG_DF.sort_values('market_price', ascending = True)

fig = px.bar(avg_market_price_df, x='market_price', y='category', template = 'plotly_dark', title='Ranking of Catagories WRT AVG Market Price', color='market_price', height=800)
fig.show()


# In[18]:


avg_sale_price_df = AVG_DF.sort_values('sale_price', ascending = True)

fig = px.bar(avg_sale_price_df, x='sale_price', y='category', template = 'plotly_dark', title='Ranking of Catagories WRT AVG Market Price', color='sale_price', height=800)
fig.show()


# In[19]:


fig = px.scatter(avg_sale_price_df, x="sale_price", y="market_price", color="sale_price",
                 size='sale_price', hover_data=['category', 'sale_price', 'market_price', 'rating'], template = 'plotly_dark', 
                 title='Scatter Plot of cross Market Price and Sale Price')
fig.show()


# In[21]:


umama_dataset.head(5)


# In[22]:


data = umama_dataset
AVG_SUB_DF = data[['sub_category','rating', 'market_price', 'sale_price']].groupby(['sub_category']).mean().reset_index().sort_values('rating', ascending = False)


# In[23]:


AVG_SUB_DF.head(5)


# In[24]:


fig = px.scatter(AVG_SUB_DF, x="sale_price", y="market_price", color="sale_price",
                 size='sale_price', hover_data=['sub_category', 'sale_price', 'market_price', 'rating'], template = 'plotly_dark', 
                 title='Scatter Plot of cross Market Price and Sale Price Per Sub Category')
fig.show()

