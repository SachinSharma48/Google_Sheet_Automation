import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import time
import webbrowser
import numpy as np
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)
excel_file_path= "C:\\Users\\Desktop\\data.csv"
df = pd.read_csv(excel_file_path)
df = df.replace({np.nan: ""})
document_id = '3rt-sfdsdfdsfdsfdsfsdfsdfsdf'
worksheet_name = 'Sheet1'
gc = client
sh  = gc.open_by_key(document_id)
values = df.values.tolist()
sh.values_clear("Sheet!A2:an12000")
sh.values_append(worksheet_name, {'valueInputOption': 'USER_ENTERED'}, {'values': values})
linke = 'https://docs.google.com/spreadsheets/d/9X1m/'
webbrowser.open(linke)
time.sleep(10)
# >>>>>>>>>>>>>>>>
