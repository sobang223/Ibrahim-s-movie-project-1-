#!/usr/bin/env python
# coding: utf-8

# ![example](images/director_shot.jpeg)

# # Movie recomendations
# 
# **Authors:** Ibrahim Bangura
# ***

# ## Overview
# 
# This analysis will use the following data :-
# * Title basics :- gives us the studios and tiles of the movies.
# * Title ratings :- Gives us the ratings of each movie.
# * Movie gross :- gives us foreign and domestic gross of each movie.
# * Name basics :- Gives us the names of people in the movies.
# * Title principles : - Gives us the category of each person in the movie
# 
# The above datas will be used to provide three recomendations to microsoft to enter the movie industry. I will firstly read the necesarry data. Secondly, I will clean the data, before getting it ready for analysis. Finally, I will then use bar chart to visualize my results.

# ## Business Problem
# 
# Microsoft is looking to get in the movie business industry. As a new market player, they are looking for ways to get an edge of the market.
# 
# ***
# * Our focus  was how to increase revenue and the determing factors for achieving this result. 
# * As a result, we choose data that will show us the relationship between average rating and revenue.
# * Secondly, we will be looking at which studios that microsoft will partner with that will give them higher revenue
# * Thirdly, we will be looking at which actors that could be casted to increae the gross revenue of the movie. 
# ***

# In[1]:


# Import standard packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[137]:


# Read Data 
df1 = pd.read_csv('Downloads/zippedData/imdb.title.basics.csv.gz')
df2 = pd.read_csv('Downloads/zippedData/imdb.title.ratings.csv.gz')
df3 = pd.read_csv('Downloads/zippedData/bom.movie_gross.csv.gz')
df4 = pd.read_csv('Downloads/zippedData/imdb.name.basics.csv.gz')
df5 = pd.read_csv('Downloads/zippedData/imdb.title.principals.csv.gz')


# In[3]:


df1 = pd.read_csv('Downloads/zippedData/imdb.title.basics.csv.gz')


# In[4]:


df3 = pd.read_csv('Downloads/zippedData/bom.movie_gross.csv.gz')


# In[5]:


df4 = pd.read_csv('Downloads/zippedData/imdb.name.basics.csv.gz')


# In[6]:


df5 = pd.read_csv('Downloads/zippedData/imdb.title.principals.csv.gz')


# In[7]:


# Start by checking for duplicates for each imported data.
df1.duplicated().value_counts()


# In[8]:


df2.duplicated().value_counts()


# In[9]:


df3.duplicated().value_counts()


# In[10]:


df4.duplicated().value_counts()


# In[11]:


df5.duplicated().value_counts()


# Therefore, it can be confirmed that there are no duplicated data in the imported data. As all the output shows no "True" values for the duplicate checker function.

# Secondly, let us try to understand the imported data.

# In[126]:


# Checking the top rows of df1
df1.head()


# In[127]:


#Checking df1 info
df1.info()

# We will need to convert runtime_minutes from object to float data type to perform munerical operations. 
# This will be done in data preperation section


# In[128]:


# Checking the top rows of df2
df2.head()


# In[129]:


#Checking df2 info
df2.info()


# In[130]:


# Checking the top rows of df3
df3.head()

#In order to merge df1 and df3 using movie title, we will need to change the name of columns with the title to a common name.
#We will change the name of columns in df1 and df3 from "primary_title and 'title'" to "MOvies". This will be done in data cleaning section.


# In[131]:


#Checking df3 info
df3.info()

# We will need to convert foreign_gross from object to float data type to perform munerical operations. 
# This will be done in data preperation section


# In[132]:


# Checking the top rows of df4
df4.head()
# I will be dropping birth_year and death-year as they will not be useful in my analysis
# this will be done later.


# In[133]:


#Checking df info
df4.info()
# The columns births and death will be deleted as they are need in this analysis.
#This will be done later as well.


# In[134]:


# Checking the top rows of df5
df5.head()


# In[135]:


#Checking df info
df5.info()


# In[138]:


# Removing unwanted columns
df4=df4.drop(['birth_year','death_year','primary_profession','known_for_titles'],axis=1)


# In[139]:


df5=df5.drop(['ordering','job','characters'],axis=1)


# In[142]:


# Dropping null values from the imported data
df1.dropna(inplace=True)
df2.dropna(inplace=True)
df3.dropna(inplace=True)
df4.dropna(inplace=True)
df5.dropna(inplace=True)


# In[148]:


# Renaming movie title column in df1 and df3 from title/ptimary_title to movies
df1.rename(columns={'primary_title': 'movies'}, inplace=True)
#df1=df1.rename(columns={'primary_title': 'movies'}, inplace=True)


# In[144]:


df3.rename(columns={'title': 'movies'}, inplace=True)
#df3=df3.rename(columns={'title': 'movies'}, inplace=True)


# In[145]:


# Converting the data type from object to float to perform artihmetic operations

df3['foreign_gross'] = pd.to_numeric(df3['foreign_gross'], errors='coerce')


# In[149]:


# Checking if the data cleaning is correctly done or not
# Note that the primary_title column has been renamed to "Movies"
df1.info()


# In[147]:


df2.info()


# In[150]:


df3.info()
#Note that the title colomn have been changed to movies.


# In[151]:


df4.info()
# As we can see below, we have removed unwated colomns 'birth_year','death_year','primary_profession' and'known_for_titles.


# In[152]:


df4.head()


# In[153]:


df5.info()


# In[154]:


# Merging df1 and df 3 on movies.
df6 = df1.merge(df3, on = 'movies', how = 'inner')


# In[155]:


df6 


# In[156]:


# Removing original_title and start_year from the dat
df6 = df6.drop(['original_title','start_year'],axis=1)


# In[157]:


df6


# In[158]:


df7 = df6.merge(df2, on = 'tconst',how = 'inner')


# In[159]:


df7


# In[160]:


df_actors= df4.merge(df5, on = 'nconst', how = 'inner')


# In[161]:


# I filtered the category sector to get just actors.
df_actors=df_actors.loc[df_actors['category'] == "actor"] 


# In[162]:


# we ran it after we filtered the actors 
df_actors.head()


# In[163]:


df9 = df7.merge(df_actors, on = 'tconst',how = 'inner')


# In[164]:


df9


# In[107]:


# Analysis one 
# In this analuysis, we will be showing the relationship between avaerage ratings and domestic gross. 

df_analysis1 = df7[['movies','domestic_gross', 'foreign_gross', 'averagerating']]
df_analysis1a=df_analysis1
df_analysis1a=df_analysis1a.sort_values(by='averagerating', ascending=False,ignore_index=True)
df_analysis1a.set_index("movies", inplace = True)


# In[108]:


# to understand the data i will call the top ten rows 
df_analysis1a.iloc[0:9,:]


# In[113]:


# plotting a bar chart to show the relationship between average ratings and domestic abd foreign gross. 
fig=plt.figure()
ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

width = 0.2

df_analysis1a['averagerating'].iloc[0:9].plot(kind='bar', color='red', ax=ax, width=width, position=2)
df_analysis1a['domestic_gross'].iloc[0:9].plot(kind='bar', color='blue', ax=ax2, width=width, position=0)
df_analysis1a['foreign_gross'].iloc[0:9].plot(kind='bar', color='green', ax=ax2, width=width, position=1)
ax.set_ylabel('Average Rating')
ax2.set_ylabel('Gross Revenue')
plt.title('Movies with highest rating and corresponding Domestic & Foreign Gross')
plt.show()


# In[66]:


# Analysis 2. 
# Studios with highest domestic and foreign gross. 
# Thi is groupby studios an and the mean, domestica nd foregn gross were determined and were sorted based on doemstic gross.  

df_analysis2=df7[['studio','domestic_gross', 'foreign_gross']]
df_analysis2a=df_analysis2
df_analysis2a=df_analysis2a.groupby('studio',as_index=False).agg({'domestic_gross':'mean','foreign_gross':'mean'}).sort_values(by='domestic_gross', ascending=False,ignore_index=True)
df_analysis2a.set_index("studio", inplace = True)


# In[121]:


df_analysis2a


# In[73]:


# The first bar chart shows the top ten studios base on domestic gross. Which means that, the studios with the highest domestic gross.

df_analysis2a.iloc[0:9,0].plot(kind="bar")
plt.xlabel('Studio')
plt.ylabel('Movie Revenue ($)')
plt.title('Top 10 Studio based on Domestic Gross')
#plt.ylim(0,1600000000)
#plt.gcf().set_size_inches(5, 2)
plt.show()


# In[70]:


# The second bar chart shows the top ten studios base on foreign gross. 
df_analysis2b=df_analysis2
df_analysis2b=df_analysis2.groupby('studio',as_index=False).agg({'domestic_gross':'mean','foreign_gross':'mean'}).sort_values(by='foreign_gross', ascending=False,ignore_index=True)
df_analysis2b.set_index("studio", inplace = True)


# In[125]:


df_analysis2b.iloc[0:9,1].plot(kind="bar")
plt.xlabel('Studio')
plt.ylabel('Movie Revenue ($)')
plt.title('Top 10 Studio based on Foreign Gross')

plt.show()


# In[86]:


# Analysis 3 
df9


# In[94]:


# We will group the actors nd finding the mean domestic gross of each actor and find the top ten actors with highest domestic gross.
df_analysis3=df9[['nconst','primary_name', 'domestic_gross','foreign_gross']]
df_analysis3a=df_analysis3
df_analysis3a=df_analysis3a.groupby('primary_name',as_index=False).agg({'domestic_gross':'mean'}).sort_values(by='domestic_gross', ascending=False,ignore_index=True)
df_analysis3a.set_index("primary_name", inplace = True)


# In[99]:


df_analysis3a


# In[100]:


# We will group the actors nd finding the mean foreign gross of each actor and find the top ten actors with highest foreign gross.
df_analysis3b=df_analysis3
df_analysis3b=df_analysis3b.groupby('primary_name',as_index=False).agg({'foreign_gross':'mean'}).sort_values(by='foreign_gross', ascending=False,ignore_index=True)
df_analysis3b.set_index("primary_name", inplace = True)


# In[101]:


df_analysis3b


# In[104]:


# plotting the bar chat of top ten actors with highest domestic gross.
df_analysis3a.iloc[0:9].plot(kind="bar")
plt.xlabel('Actors')
plt.ylabel('Movie Revenue ($)')
plt.title('Top 10 Actors based on Domestic Gross')

plt.show()


# In[105]:


# plotting the bar chat of top ten actors with highest foreign gross
df_analysis3b.iloc[0:9].plot(kind="bar")
plt.xlabel('Actors')
plt.ylabel('Movie Revenue ($)')
plt.title('Top 10 Actors based on Foreign Gross')

plt.show()


# ## Conclusions
# FRom the above analysis, we have arrived at three recomnedations that microsoft can adopt when entering the movie industry
# 
# ***
# 1. In the first analysis we tried to find out whether there is a positive relationship between average rating of movies and gross revenue. The result from the analysis shows that average rating is not a determining factor of higher revenue. As such, if Microsoft is looking for higher profit margins then average rating should not be the primary objective. 
# 
# 
# 2. In our second analysis, we tried to understand which studios produces movies with higher domestic and foreign gross. If Microsoft is aiming for a movie that performs well in the domestic market financially, the Microsoft may look into partnering with the studio named BV. If the aim is to create financially acclaimed movie in the international market, then Microsoft could asscoiate with the studio named HC.
# 
# 
# 3. In the third analysis, actors who were part of the movies with higher revenue were determined and the analysis were conducted based on the region of focus. Microsoft could cast the actor named Mark Hamill, if the objective is to improve the revenue in the domestic movie market. Or if the focus is improving the revenue in the international market, then the actor named Ed Ackermann could be made part of the movie.
# *** 

# In[ ]:




