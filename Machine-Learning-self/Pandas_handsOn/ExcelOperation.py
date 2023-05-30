#!/usr/bin/env python
# coding: utf-8

# <div style = "  display : flex; justify-content: center; ">
#     <h1 style = " background-color: Black; color:white; display:flex; padding:10px"> Pandas Hands On</h1>
#  </div>

# In[1]:


import pandas as pd
import numpy as np
print(pd.__version__)
ds = pd.read_excel('ExcelFile/Pandas.xlsx')
ds


# In[2]:


ds.info()


# In[3]:


ds.head(1) # it is used to show number of rows from beginning.


# In[4]:


ds.tail(2) # it is to used to show number of rows from End .


# In[5]:


dss = ds.fillna(value= 0) # to set the Null value
dss


# ## Slicing

# In[6]:


ds1 = pd.read_excel('ExcelFile/2023_BATCH_PLACEMENT_CIVIL.xlsx')
zm = pd.read_csv('ExcelFile/zomato.csv')
zm


# In[7]:


#slicing 
display(zm[1:5])
display(zm.loc[[100,4,5,6]])
display(zm.iloc[1:10 , 0:3])  # This is for both row and column


# In[8]:


display(ds1)
ds2 = ds1.fillna(value = 0 )
display(ds2)


# <h3> describe() </h3>
# <p> It is basically use for <strong>Numerical value </strong> in sheet. It descirbe below methods for every numerical column.   </p>

# In[9]:


ds1.describe()


# In[10]:


ds1.info() # it gives 


# Above RangeIndex is : Number of Rows
#       Column is Number of Columns. 

# In[11]:


# It is used for get Name of the Columns in our sheets
ds1.columns
# ds1.rows is WRONG


# <div style = "display : flex; justify-content: center; ">
#     <h1 style = "background-color: yellow; color:black; display:flex; padding:10px"> ds1['column_Name'].unique() </h1>
#  </div>
#  <h4> It gives unique Element of particular particular Column_Name <h4>

# In[12]:


a = ds1['Unnamed: 32'].unique()
arr = np.array(a)


# In[13]:


print(arr.size)
arr


# <div style = "display : flex; justify-content: center; ">
#     <h1 style = "background-color: yellow; color:black; display:flex; padding:10px"> ds1['column_Name'].value_counts()</h1>
#  </div>
#  <h4> It gives Number of times the unique Element of particular  Column_Name have Occurs <h4>
#     <p style = "font-family : The Times Roman"> For Example</p>

# In[14]:


valuecounts = ds1['Unnamed: 33'].value_counts()


# In[15]:


valuecounts


# <div style = "  display : flex; justify-content: center; ">
#     <h1 style = " background-color: purple; color:white; display:flex; padding:10px"> DATA FRAME</h1>
#  </div>
#  

#  <p style = "font-size : 17px ; ">A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, <br>or a table with rows and columns.</p >
#  <p>For Example</p>

# In[16]:


import pandas as pd
data  = {
    'Names' : ['Vishal' , 'sneha' , 'souchit'],
    'BirthYear'  : [2000, 2001 , 2001]         
}
df3 = pd.DataFrame(data)
# df3.to_excel('small_df.xlsx')
df3


# ## Named Index

# With the index argument, you can name your own indexes

# In[17]:


df3 = pd.DataFrame(data , index = ["Name1" , "Name2" , "Name3"])
display(df3)


# Refrence for DataFrame  :
# 
# https://www.w3schools.com/python/pandas/pandas_dataframes.asp

# <div style = "  display : flex; justify-content: center; ">
#     <h1 style = " background-color: purple; color:white; display:flex; padding:10px"> 
#     Simple Filtering
#     </h1>
#  </div>

# In[18]:


series =df3['Names']
print("Type = ",type(series))
display(series)


# In[19]:


# In DataFrame Type
display(df3[['Names']])
print("Type = " , type(df3[['Names']]))


# In[20]:


df3[df3['Names']=='Vishal']


# In[21]:


df4 = df3[df3['Names']=='Vishal']['BirthYear']
display(df4)


# <div style = "  display : flex; justify-content: center; ">
#     <h1 style = " background-color: purple; color:white; display:flex; padding:10px"> 
#     Complex Filtering With Zomato DataSet
#     </h1>
#  </div>

# In[22]:


# http://localhost:8888/edit/Jupyter_Python_learning/Pandas_HandsON/ExcelFile/zomato.csv
zm = pd.read_csv("ExcelFile/zomato.csv" )


# In[ ]:





# In[23]:


OnlineOrder = zm[zm['online_order'] == 'Yes']   
OnlineOrder


# In[24]:


book_table = OnlineOrder[OnlineOrder['book_table'] == 'Yes']
book_table


# In[25]:


print(book_table.shape)
# There is another way to write the above complex filtering in one line 
zm[(zm['online_order'] == 'Yes') & (zm['book_table'] == 'Yes')]


# <div style = "  display : flex; justify-content: center; ">
#     <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
#     Add and Remove Columns 
#     </h1>
#    
#  </div>
#   <p> <br> To get Add Column  <b> zm['Column_Name'] = 'Column_Value' 
#     </b> //--> this will to give all the rows same value </p>

# In[26]:


zm['Column_Name'] = 'Column_Value'
zm


# ![image.png](attachment:image.png)

# ## To Remove (zm.drop)

# In[27]:


# Axis = 1 means Column wise
#  Axis = 0 menas row wise
zm.drop('Column_Name' , axis = 1)
# Here it is Not permanently Deleted. If you again print 'zm'.
# To Delete permanently we have to use "inplace" or
# '''  We can do
# zm = zm.drop('Column_Name' , axis = 1)  # This is over writing in exsisting variable
#         OR(use inplace)
# zm.drop('Column_Name' ,axis=1, inplace ="true")        
# '''


# In[28]:


zm


# In[29]:


zm


# In[30]:


zm.drop('Column_Name', axis=1, inplace = True)
zm


# In[31]:


zm


# <div style = "  display : flex; justify-content: center; ">
#     <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
#     Renaming And Reordering 
#     </h1>
#    
#  </div>
#   <p> <br>  </p>

# ## Rename
# Lets I want to rename Column_Name to Values
# .rename()   function 
# 
# Example

# In[32]:


zm['Column_Name'] = 'Column_value'


# In[ ]:





# In[33]:



#  to change it permanent 
zm.rename(columns = {
         'Column_Name' : 'Values'} , inplace = True )


# In[34]:


zm


# In[35]:


zm.columns


# ## Reordering

# In[36]:


# 'url', 'address', 'name', 'online_order', 'book_table', 'rate', 'votes','phone', 'location', 'rest_type', 'dish_liked', 'cuisines','approx_cost(for two people)', 'reviews_list', 'menu_item','listed_in(type)', 'listed_in(city)', 'Values'
zm = zm[['address', 'url', 'Values', 'online_order', 'book_table', 'rate', 'votes',
       'phone', 'location', 'rest_type', 'dish_liked', 'cuisines',
       'approx_cost(for two people)', 'reviews_list', 'menu_item',
       'listed_in(type)', 'listed_in(city)', 'name']]


# In[37]:


# Here is reordering is done
zm  


# <div style = "  display : flex; justify-content: center; ">
#     <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
#    Appending and Resetting Index
#     </h1>
#    
#  </div>
#   <p> </p>

# In[38]:


data = {
    'Names' : ['vishal', 'sneha' , 'souchit'],
     'Ages' : [22 , 21 , 21]
}
a1= pd.DataFrame(data) 
display(a1)
data2 = {
    'Names' : ['sabayasachi', 'Aditya' , 'sachine'],
     'Ages' : [21 , 20 , 21]
}
a2=pd.DataFrame(data2)
display(a2)


# In[39]:


# Now do Append between a1 and a2
a3 = a1.append(a2)
a3
# here Index is also  appending so we reset the Index


# In[40]:


con = pd.concat([a1 , a2])
display(con) #index problem here so
display(pd.concat([a1 , a2], ignore_index = True ,axis = 1))


# In[41]:


a3 = a3.reset_index()
a3


# In[42]:


# Now we can remove index coloum 0 1 2 0 1 2

a3 = a3.drop('index' , axis =1)
a3


# <div style = "  display : flex; justify-content: center; ">
#     <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
#     ILOC and LOC
#     </h1>
#    
#  </div>
#   <p>The loc() function is label based data selecting method which means that we have to pass the name of the row or column which we want to select.
#    <ul> Here End Index is Inclusive</ul> 
#     <br><br>
# The iloc() function is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column. 
#     <ul>Here End Index is Exclusive</ul>
# </p>

# In[43]:


import pandas as pd
 
# creating a sample dataframe
data = pd.DataFrame({'Brand': ['Maruti', 'Hyundai', 'Tata',
                               'Mahindra', 'Maruti', 'Hyundai',
                               'Renault', 'Tata', 'Maruti'],
                     'Year': [2012, 2014, 2011, 2015, 2012,
                              2016, 2014, 2018, 2019],
                     'Kms Driven': [50000, 30000, 60000,
                                    25000, 10000, 46000,
                                    31000, 15000, 12000],
                     'City': ['Gurgaon', 'Delhi', 'Mumbai',
                              'Delhi', 'Mumbai', 'Delhi',
                              'Mumbai', 'Chennai',  'Ghaziabad'],
                     'Mileage':  [28, 27, 25, 26, 28,
                                  29, 24, 21, 24]})
 
# displaying the DataFrame

display(data)


# In[44]:


display(data.iloc[1])
d1 = data.iloc[[1,2,8]]
display(d1)
display(data.iloc[1:5 ,  1:4]) # here 5 & 4 is excluded
# Means in iloc it work whole things in index wise
display(data.iloc[[1,4,8],[0,2,4]])
print('display(data.iloc[[1,4,8],[0,2,4]])')


# In[45]:


# loc
display(data.loc[data.Brand == 'Tata']) # ******
# display(data.loc[0:6, 2:3])       -> this will get an Error
display(data.loc[0:4]) # Here 4 is included
display(data.loc[0:4 , 'Year' : 'City'])
#  means in loc it work whole things in Name wise.


# In[46]:


data.loc[(data.Brand == 'Hyundai') | (data.Brand == 'Tata')&(data.Mileage > 25)]


# In[47]:


data.loc[(data.Brand == 'Hyundai') | (data.Brand == 'Tata')&(data.Mileage > 25)][['Mileage' , 'Year' , 'Kms Driven']]


# <div style = "  display : flex; justify-content: center; ">
#     <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
#     Dropping Duplicates and Group by Function
#     </h1>
#    
#  </div>
#   <p> 
# </p>

# drop_duplicates it contain two parameter:
# 
#     1. subset -> Subset takes a column or list of column label. It’s default value is none. After passing columns, it will 
#                  consider them only for duplicates. 
#     2. keep = keep is to control how to consider duplicate value. It has only three distinct value and default is `first` 
#               
#               false, first ,last 

# In[48]:



data.drop_duplicates() # It is now consider duplicates according to index


# In[49]:


data = {
    'Names' : ['vishal', 'sneha' , 'souchit'],
     'Ages' : [22 , 21 , 21]
}
a1= pd.DataFrame(data) 
display(a1)
data2 = {
    'Names' : ['vishal', 'Aditya' , 'sachine'],
     'Ages' : [22 , 20 , 21]
}
a2=pd.DataFrame(data2)
display(a2)
d1 = a1.append(a2)
display(d1)


# In[50]:


d1.drop_duplicates()


# In[51]:


import pandas as pd
  
data = {
    "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
    "B": [50, 40, 40, 30, 50],
    "C": [True, False, False, False, True]
}
  
df = pd.DataFrame(data)
display(df)
display(df.drop_duplicates())


# In[ ]:





# In[52]:


em = pd.read_csv('ExcelFile/Employees.csv')
display('Emlpoyees File',em)        


# In[53]:


# sorting by first name
em = em.sort_values("First Name")
display('Sorting By First Name',em)


# In[54]:


# To remove All Duplicates from file.
em.drop_duplicates(subset = "First Name" , inplace = True)
display('Duplicates only in First Name Column',em)  # here all dublicates in first Name have removed


# In[55]:


display('Remove ALL duplicates')
em.drop_duplicates(subset = "First Name" , keep = False ,inplace=True  )
display(em)


# In[56]:


group = em.groupby('Team')
display(pd.DataFrame(group))
for i in  group:
    display(i)


# In[57]:


display(group.get_group('Engineering'))
group.get_group('Engineering')['Salary']


# In[58]:


display(group.max())
group.max('Salary')


# In[59]:


em
g =em.groupby(['Team' , 'Gender'])['First Name'].count()
display(g)
g.to_csv('Team_Gender.csv')
g =pd.read_csv('Team_Gender.csv')
g # this is now convert into csv file.


# In[60]:



emm = em[em['Team'] == 'Engineering']
display(emm[['Salary']].max())
display(em[em['Salary'] == emm['Salary'].max()])
display(em['Salary'].max())
display(em[em['Salary'] == em['Salary'].max()])


# <div style = "  display : flex; justify-content: center; ">
#     <h1 style = " background-color: black; color:white; display:flex; padding:10px"> 
#            Merging Concept
#     </h1>
#    
#  </div>
#   <p> 
#     Pandas have options for high-performance in-memory merging and joining. When we need to combine very large DataFrames, joins serve as a powerful way to perform these operations swiftly. Joins can only be done on two DataFrames at a time, denoted as left and right tables. The key is the common column that the two DataFrames will be joined on. It’s a good practice to use keys which have unique values throughout the column to avoid unintended duplication of row values. Pandas provide a single function, merge(), as the entry point for all standard database join operations between DataFrame objects.
# </p>

# In[61]:


data1 = {'key': ['k0', 'k1', 'k2'],
         'Name':['Jai', 'Princi','Anuj'], 
        'Age':[27, 24, 22],} 
data2 = {
    'key' : ['k0' , 'k1' , 'k2', 'k3'] ,
    'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
    'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']   
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
display(df1, df2)
# using .merge() function. 
res = pd.merge(df1,df2 , on='key' )
print( "\n" , 'Merging')
display(res)


# In[62]:


# how is methodology and inner is default (analysis with above) ,            
display(pd.merge(df1 , df2 , on='key' , how='inner'))
display(pd.merge(df1 , df2 , on='key' , how='outer'))
display(pd.merge(df1 , df2 , on='key' , how='right'))
display(pd.merge(df1 , df2 , on='key' , how='left'))


# ![image.png](attachment:image.png)

# ## Transform Name(Mapping)

# In[63]:


df2


# In[64]:


#  I want to transform the address name in shortcut 
#  create Dictionary 
mapping = {'Nagppur':'NG' , 'Kanpur' : 'CNB'  , 'Allahabad' : 'PRG' ,'Kannuaj' :'KJN'}
df2['Address'].map(mapping)


# In[65]:


df2['Address'] = df2['Address'].map(mapping)
df2


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




