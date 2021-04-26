import gspread
from google.oauth2 import service_account
import tkinter as tk

# To authenticate Google Service Account
gc = gspread.service_account(
    filename="/Users/chow/assignments/Week2/Exercise3/excelentsheets-7f71669766da.json"
)

# Makes a new spreadsheet with desired name and shares to email entered.
def makesprsh(name, email):
    sh = gc.create(name)
    sh.share(email, perm_type="user", role="writer")
    sh.add_worksheet(title="Presentation Schedule", rows="100", cols="20")
    sh.add_worksheet(title="AIDP Course Plan", rows="100", cols="20")
    wksh = sh.worksheet("Sheet1")
    sh.del_worksheet(wksh)


# Formats created sheet
def formatter(name):
    wksh = gc.open(name).sheet1

    # Update a range of cells using the top left corner address
    wksh.update(
        "A1",
        [
            ["Wk#", "Theme", "Presenter 1", "Presenter 2", "Presenter 3"],
            [1, "Data Analytics", "Khatijah", "Elias"],
            [2, "Programming Fundamentals", "Lih Yan", "Andy"],
            [3, "EDA", "Pei Yueng", "Rosmawati", "Joy"],
            [4, "Data Curation & RPA", "Elias", "Poi Yee"],
            [5, "Data Engineering Fundamentals", "Rosmawati", "Andy"],
            [6, "Machine Learning I", "Joy", "Pei Yueng"],
            [7, "Machine Learning II", "Poi Yee", "Lih Yan", "Khatijah"],
        ],
    )

    # Format the header
    wksh.format(
        "A1:F1", {"horizontalAlignment": "CENTER", "textFormat": {"bold": True}}
    )
    wksh.format("A2:F8", {"horizontalAlignment": "CENTER"})


# Command for "share" button push
def share():
    makesprsh(shname.get(), usermail.get())
    formatter(shname.get())
    return


# GUI for script
window = tk.Tk()
window.title("Share Sheets")
frame = tk.Frame(window, width=500, height=200)

info = tk.Label(window, width=30, height=3, text="Get your spreadsheet here!",)

# Labels of what inputs are required
labelemail = tk.Label(window, text="email:")
labelname = tk.Label(window, text="sheet name:")

# Entry fields for email and sheet name
usermail = tk.StringVar()
email = tk.Entry(window, textvariable=usermail)
shname = tk.StringVar()
sheet = tk.Entry(window, textvariable=shname)

# Button to be clicked to input email and sheetname
genbutton = tk.Button(
    window, text="Send", command=share, height=2, width=4, wraplength=100
)

# Geometery grid for GUI format
info.grid(column=2, row=0)
labelemail.grid(column=1, row=1)
labelname.grid(column=1, row=2)
email.grid(column=2, row=1)
sheet.grid(column=2, row=2)
genbutton.grid(column=2, row=3)
frame.grid(column=0, row=0, columnspan=10, rowspan=10)
window.mainloop()
