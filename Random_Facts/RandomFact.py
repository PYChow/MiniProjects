## This script opens up a window and generates a random fact at a push of a button
## Random facts are obtained from API

import tkinter as tk
import requests


def RandomFacts():
    # Get random facts from API
    response = requests.get(
        "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1"
    )

    # Check request status
    if response.status_code == 200:
        # To assign "text" portion from string to label
        quote = response.json()["text"]
        info.configure(text=quote)

    else:
        info.configure(text="ERROR: Toebeans not found :(")
        return


# Window for fact app
window = tk.Tk()
window.title("Random Facts Generator")

# Info on app on how to generate facts
info = tk.Label(
    window,
    width=30,
    height=8,
    wraplength=250,
    text="This is a random facts generator, click on the button for one!",
)
info.pack()

# Button to be clicked for fact generation
factbutton = tk.Button(
    window, text="Give Me Facts!", command=RandomFacts, height=2, width=9
)
factbutton.pack()

window.mainloop()
