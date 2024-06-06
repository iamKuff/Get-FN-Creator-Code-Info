import tkinter as tk
from tkinter import messagebox
import requests

# Function to get creator code information
def get_creator_code_info(creator_name):
    url = f"https://fortnite-api.com/v2/creatorcode?name={creator_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            return data['data']
        else:
            return None
    elif response.status_code == 400:
        return {"error": "Invalid or missing parameter(s)"}
    elif response.status_code == 404:
        return {"error": "Code does not exist"}
    else:
        return {"error": "An unknown error occurred"}

# Function to handle the button click
def fetch_creator_code_info():
    creator_name = entry_creator_name.get()
    if not creator_name:
        messagebox.showerror("Error", "Please enter a creator name.")
        return

    info = get_creator_code_info(creator_name)
    
    if info and "error" not in info:
        result_text = f"Creator Code: {info['code']}\n" \
                      f"Account ID: {info['account']['id']}\n" \
                      f"Name: {info['account']['name']}\n" \
                      f"Status: {info['status']}\n" \
                      f"Verified: {info['verified']}"
    else:
        result_text = info.get("error", "Unknown error occurred")

    result_label.config(text=result_text)

# Setting up the GUI
root = tk.Tk()
root.title("Fortnite Creator Code Info")

# Creator name input
tk.Label(root, text="Enter Creator Name:").grid(row=0, column=0, padx=10, pady=10)
entry_creator_name = tk.Entry(root)
entry_creator_name.grid(row=0, column=1, padx=10, pady=10)

# Fetch button
fetch_button = tk.Button(root, text="Fetch Info", command=fetch_creator_code_info)
fetch_button.grid(row=0, column=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
