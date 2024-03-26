from colorama import Fore, init
from CTkMessagebox import CTkMessagebox

import customtkinter
import os
import time

cwd = os.getcwd()

init(autoreset=True)

#pre code checks
try:
    if os.path.exists(f"{cwd}\\content") == False:
        os.mkdir(f"{cwd}\\content")
        time.sleep(1)
        os.mkdir(f"{cwd}\\content\\youtube")
        os.mkdir(f"{cwd}\\content\\youtube\\videos")
        os.mkdir(f"{cwd}\\content\\youtube\\playlists")
        os.mkdir(f"{cwd}\\content\\youtube\\channels")
        os.mkdir(f"{cwd}\\content\\spotify")
        os.mkdir(f"{cwd}\\content\\spotify\\songs")
        os.mkdir(f"{cwd}\\content\\spotify\\albums")
        os.mkdir(f"{cwd}\\content\\spotify\\playlists")
    elif os.path.exists(f"{cwd}\\content") == True:
        pass
    else:
        print(Fore.RED + "Error")
except Exception as e:
    print(Fore.RED + e)

#defining vars
icon = f"{cwd}\\icon.ico" #icon from https://icon-icons.com/

youtube_videos_folder = f"{cwd}\\content\\youtube\\videos"
youtube_playlists_folder = f"{cwd}\\content\\youtube\\playlists"
youtube_channels_folder = f"{cwd}\\content\\youtube\\channels"

spotify_songs_folder = f"{cwd}\\content\\spotify\\songs"
spotify_albums_folder = f"{cwd}\\content\\spotify\\albums"
spotify_playlists_folder = f"{cwd}\\content\\spotify\\playlists"

def spotify():
    pass

def youtube():
    pass

def main():
    root = customtkinter.CTk()
    root.minsize(480, 270)
    root.title("spotitube")
    root.iconbitmap(icon)
    root.mainloop()

if __name__ == "__main__":
    main()