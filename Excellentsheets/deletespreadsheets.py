import gspread
import pandas as pd
from google.oauth2 import service_account
import tkinter as tk

gc = gspread.service_account(
    filename="Place your api key here"
)

# Makes a new spreadsheet with desired name and shares to email entered.
def delsh(name):
    gc.del_spreadsheet(name)
    return


shname = input("Input sheet name here:")
delsh(shname)

