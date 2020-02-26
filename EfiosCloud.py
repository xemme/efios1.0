# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:35:13 2020

@author: xemme
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('efios_schedule').sheet1

def writeto(gridloc, string):
    sheet.update_acell(gridloc, string)
    
def retVal(A, i):
    cell = A+""+i
    return sheet.acell(cell)