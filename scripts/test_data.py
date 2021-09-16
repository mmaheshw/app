#!/usr/bin/env python
# coding: utf-8




# importing the required libraries
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


# define the scope
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/manja/spreadsheetdemo/auth/creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("test").sheet1

data = sheet.get_all_values()
blanks = data.pop(0)
df = pd.DataFrame(data, columns=["Date", "Time", "Temperature", "Humidity"])

df['DateTime'] = df['Date'] + ' ' + df['Time']
print(df.head())

df[['temp-'+str(60)]] = df.Temperature.shift(60)
df[['humidity-'+str(60)]] = df.Humidity.shift(60)

# Create a new subsetted dataframe, removing Nans from first 12 rows
df_data = df[60:]
df_data.head()

df_data.to_csv('C:/Users/manja/spreadsheetdemo/app/data/df.csv')

