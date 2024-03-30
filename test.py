import tkinter as tk
from tkinter import ttk
from pytube import YouTube

def fetch_resolutions():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        global streams
        streams = yt.streams.filter(progressive=True).all()
        resolutions = [stream.resolution for stream in streams if stream.resolution]
        resolution_var.set(resolutions[0])
        resolution_dropdown['values'] = resolutions
    except Exception as e:
        resolution_var.set("Error: Invalid URL")

def download_video():
    selected_resolution = resolution_var.get()
    for stream in streams:
        if stream.resolution == selected_resolution:
            stream.download()
            print("Download complete.")
            break
    else:
        print("Error: Resolution not found.")

root = tk.Tk()
root.title("YouTube Video Downloader")

url_label = ttk.Label(root, text="Enter YouTube URL:")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

url_entry = ttk.Entry(root, width=40)
url_entry.grid(row=0, column=1, padx=5, pady=5)

fetch_button = ttk.Button(root, text="Fetch Resolutions", command=fetch_resolutions)
fetch_button.grid(row=0, column=2, padx=5, pady=5)

resolution_var = tk.StringVar()
resolution_label = ttk.Label(root, text="Available Resolutions:")
resolution_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

resolution_dropdown = ttk.Combobox(root, textvariable=resolution_var, state='readonly', width=37)
resolution_dropdown.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

download_button = ttk.Button(root, text="Download", command=download_video)
download_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()
