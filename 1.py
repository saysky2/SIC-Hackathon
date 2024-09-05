import tkinter as tk
from tkinter import messagebox
import json
import os

# Path to the dictionary file
DICTIONARY_FILE = "dictionary.json"

# Load dictionary data from file
def load_dictionary():
    if os.path.exists(DICTIONARY_FILE):
        with open(DICTIONARY_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save dictionary data to file
def save_dictionary(data):
    with open(DICTIONARY_FILE, 'w') as file:
        json.dump(data, file)

# Search for a word in the dictionary
def search_word():
    word = entry_word.get().lower()
    if word in dictionary:
        text_definition.delete(1.0, tk.END)
        text_definition.insert(tk.END, dictionary[word])
    else:
        messagebox.showinfo("Not Found", f"The word '{word}' is not in the dictionary.")

# Add a new word to the dictionary
def add_word():
    word = entry_word.get().lower()
    definition = entry_definition.get(1.0, tk.END).strip()
    if word and definition:
        if word in dictionary:
            messagebox.showwarning("Already Exists", f"The word '{word}' is already in the dictionary.")
        else:
            dictionary[word] = definition
            save_dictionary(dictionary)
            messagebox.showinfo("Success", f"The word '{word}' has been added to the dictionary.")
    else:
        messagebox.showwarning("Input Error", "Please enter both a word and a definition.")

# Update the definition of an existing word
def update_word():
    word = entry_word.get().lower()
    definition = entry_definition.get(1.0, tk.END).strip()
    if word in dictionary:
        dictionary[word] = definition
        save_dictionary(dictionary)
        messagebox.showinfo("Success", f"The definition for '{word}' has been updated.")
    else:
        messagebox.showinfo("Not Found", f"The word '{word}' is not in the dictionary.")

# Delete a word from the dictionary
def delete_word():
    word = entry_word.get().lower()
    if word in dictionary:
        del dictionary[word]
        save_dictionary(dictionary)
        messagebox.showinfo("Success", f"The word '{word}' has been deleted from the dictionary.")
    else:
        messagebox.showinfo("Not Found", f"The word '{word}' is not in the dictionary.")

# Initialize the dictionary
dictionary = load_dictionary()

# Create the main window
root = tk.Tk()
root.title("Dictionary App")

# Word entry
tk.Label(root, text="Word:").grid(row=0, column=0, padx=10, pady=10)
entry_word = tk.Entry(root)
entry_word.grid(row=0, column=1, padx=10, pady=10)

# Definition entry
tk.Label(root, text="Definition:").grid(row=1, column=0, padx=10, pady=10)
entry_definition = tk.Text(root, height=5, width=40)
entry_definition.grid(row=1, column=1, padx=10, pady=10)

# Buttons
tk.Button(root, text="Search", command=search_word).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Add", command=add_word).grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
tk.Button(root, text="Update", command=update_word).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Delete", command=delete_word).grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

# Definition display
tk.Label(root, text="Definition:").grid(row=3, column=0, padx=10, pady=10)
text_definition = tk.Text(root, height=10, width=40)
text_definition.grid(row=3, column=1, padx=10, pady=10)

# Run the application
root.mainloop()