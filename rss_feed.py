import tkinter as tk
from tkinter import ttk
import feedparser
import webbrowser

def fetch_feed():
    global feed
    url = url_entry.get()
    if url:
        feed = feedparser.parse(url)
        
        # Clear the current list
        feed_list.delete(0, tk.END)
        
        # Add new items to the list
        for index, entry in enumerate(feed.entries, start=1):
            feed_list.insert(tk.END, f"{index}. {entry.title}")
    else:
        print("Please enter a URL")

def show_description(event):
    # Get selected item
    selection = feed_list.curselection()
    if selection:
        index = selection[0]
        entry = feed.entries[index]
        description_text.delete(1.0, tk.END)
        description_text.insert(tk.END, entry.description)
        
        # Enable the "Open Full Article" button
        open_article_button.config(state=tk.NORMAL)

def open_full_article():
    selection = feed_list.curselection()
    if selection:
        index = selection[0]
        entry = feed.entries[index]
        webbrowser.open(entry.link)

# Create the main window
root = tk.Tk()
root.title("RSS Feed Reader")
root.geometry("800x600")

# Create and pack the URL entry field
url_frame = ttk.Frame(root)
url_frame.pack(pady=10, padx=10, fill=tk.X)

url_label = ttk.Label(url_frame, text="RSS Feed URL:")
url_label.pack(side=tk.LEFT)

url_entry = ttk.Entry(url_frame, width=50)
url_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(10, 0))

fetch_button = ttk.Button(url_frame, text="Fetch", command=fetch_feed)
fetch_button.pack(side=tk.LEFT, padx=(10, 0))

# Create and pack the feed list
feed_list = tk.Listbox(root)
feed_list.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
feed_list.bind('<<ListboxSelect>>', show_description)

# Create and pack the description text area
description_text = tk.Text(root, height=5, wrap=tk.WORD)
description_text.pack(pady=10, padx=10, fill=tk.X)

# Create and pack the "Open Full Article" button
open_article_button = ttk.Button(root, text="Open Full Article", command=open_full_article, state=tk.DISABLED)
open_article_button.pack(pady=10)

# Initialize feed variable
feed = None

# Start the GUI event loop
root.mainloop()