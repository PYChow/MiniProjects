import gspread
import pandas as pd
from google.oauth2 import service_account
import tkinter as tk

gc = gspread.service_account(
    filename="/Users/chow/assignments/Week2/Exercise3/excelentsheets-7f71669766da.json"
)

# Makes a new spreadsheet with desired name and shares to email entered.
def delsh(name):
    gc.del_spreadsheet(name)
    return


shname = input("Input sheet name here:")
delsh(shname)

