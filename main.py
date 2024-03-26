from CTkMessagebox import CTkMessagebox
from colorama import Fore, init

import customtkinter
import webbrowser
import time
import os

cwd = os.getcwd()
customtkinter.set_appearance_mode("dark")
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

def youtube():
    pass

def spotify(root):
    spotify_window = customtkinter.CTkToplevel(root)
    spotify_window.minsize(480, 270)
    spotify_window.maxsize(480, 270)
    try:
        spotify_window.after(300, lambda: spotify_window.iconbitmap(icon))
    except:
        print(Fore.YELLOW + "icon.ico not found, continuing")
    spotify_window.title("Spotify")

    back_button = customtkinter.CTkButton(master=spotify_window, command=spotify_window.destroy, text="Back")
    back_button.pack(padx=10, pady=10)


def main():
    root = customtkinter.CTk()
    root.minsize(480, 270)
    root.maxsize(480, 270)
    root.title("spotitube")

    try:
        root.iconbitmap(icon)
    except:
        print(Fore.YELLOW + "icon.ico not found, continuing")
        
    root.update()
    window_width = root.winfo_width()

    top_frame = customtkinter.CTkFrame(master=root, width=window_width, height=50)
    top_frame.pack(padx=10, pady=20)

    customtkinter.CTkLabel(master=top_frame, text="spotitube GUI witten by github.com/3022-2/", text_color="grey",font=("", 20), width=window_width, height=50).pack()
    
    #buttons
    youtube_button = customtkinter.CTkButton(master=root, command=lambda: youtube(), text="YouTube")
    youtube_button.pack(padx=10, pady=0)
    spotify_button = customtkinter.CTkButton(master=root, command=lambda: spotify(root), text="Spotify")
    spotify_button.pack(padx=10, pady=10)
    github_button = customtkinter.CTkButton(master=root, command=lambda: webbrowser.open("https://github.com/3022-2/spotitube-gui"), text="GitHub")
    github_button.pack(padx=10, pady=0)
    exit_button = customtkinter.CTkButton(master=root, command=lambda: exit(), text="Exit")
    exit_button.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()