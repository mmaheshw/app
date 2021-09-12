#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the required libraries
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


# In[2]:


# define the scope
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


# In[3]:


creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/manja/spreadsheetdemo/auth/creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("test")
# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)


# In[4]:


sheet_instance


# In[5]:


# get the total number of columns
sheet_instance.col_count
## >> 26


# get the value at the specific cell
sheet_instance.cell(col=3,row=2)
## >> <Cell R2C3 '63881'>


# In[6]:


# get all the records of the data
records_data = sheet_instance.get_all_records()

# view the data
# records_data


# In[7]:


# convert the json to dataframe
records_df = pd.DataFrame.from_dict(records_data)

# view the top records
records_df.head()


# In[8]:


records_df.info()


# In[9]:


col_Names=["Date", "Time", "Temperature", "Humidity"]


# In[10]:


data=pd.DataFrame(records_df.values, columns = col_Names)


# In[11]:


data.head()


# In[12]:


df = pd.DataFrame()


# In[13]:


df['Date'] =data.Date.values
df['Time']= data.Time.values
df['Temp']= data.Temperature.values
df['Humidity']= data.Humidity.values


# In[14]:


df.head()


# In[15]:



df[['temp-'+str(60)]] = data.Temperature.shift(60)
df[['humidity-'+str(60)]] = data.Humidity.shift(60)


# In[16]:


df.head()


# In[17]:


# Create a new subsetted dataframe, removing Nans from first 12 rows
df_data = df[60:]
print(df_data)


# In[18]:


df_data.to_csv('C:/Users/manja/spreadsheetdemo/app/data/df.csv')

