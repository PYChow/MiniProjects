import tkinter as tk
import random as rand
import string

NUMBERS = string.digits
SYMBOLS = ("!", "@", "#", "$", "%", "^", "&", "*", "?")
LETTERS = string.ascii_letters
ALL = NUMBERS + LETTERS + "".join(SYMBOLS)

# To generate randomised string from list and defined length
def get_random(list, num):
    random = rand.sample(list, num)
    rand.shuffle(random)
    # Remove spaces in string
    random = "".join(random)
    return random


# Count number of characters of randomised string
def count_char(pwstring):
    ndigit = 0
    nsymbol = 0
    nletter = 0

    for x in pwstring:
        if x in list(string.digits):
            ndigit += 1
        if x in list(string.punctuation):
            nsymbol += 1
        if x in list(string.ascii_letters):
            nletter += 1

    return ndigit, nsymbol, nletter


# To generate randomised password with set requirement
def pwdgen():
    password = get_random(ALL, pwlength.get())
    total_digit, total_symbol, total_letter = count_char(password)

    while total_digit < 1 or total_symbol < 1 or total_letter < 1:
        password = get_random(ALL, pwlength.get())
        total_digit, total_symbol, total_letter = count_char(password)

    return info.configure(text=password)


# To copy generated password as shown in label
def copyme():
    copy = tk.Tk()
    copy.withdraw()
    copy.clipboard_append(info["text"])
    copy.update()
    copy.destroy()


# Window for app
window = tk.Tk()
window.title("Password Generator")
window.geometry("200x200")

# Info on app on how to generate password
info = tk.Label(
    window, width=20, height=5, wraplength="200", text="Please key length of password"
)
info.pack()

# Entry fields for pw length
pwlength = tk.IntVar()
length = tk.Entry(window, textvariable=pwlength, width=5, justify="center")
length.pack()

# Button to be clicked for password generation
genbutton = tk.Button(
    window, text="Give Me a Password!", command=pwdgen, height=2, width=12
)
genbutton.pack()

# Button to be clicked to copy password to clipboard
copybutton = tk.Button(window, text="Copy!", command=copyme, height=2, width=12)
copybutton.pack()

window.mainloop()
