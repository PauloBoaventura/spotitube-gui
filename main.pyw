from CTkMessagebox import CTkMessagebox
from colorama import Fore, init

import customtkinter
import subprocess
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

def youtube(root):
    def yt_to_mp4(YouTube_url):
        pass
    def yt_to_mp3(YouTube_url):
        pass
    youtube_window = customtkinter.CTkToplevel(root)
    youtube_window.minsize(480, 270)
    youtube_window.maxsize(480, 270)
    try:
        youtube_window.after(300, lambda: youtube_window.iconbitmap(icon))
    except:
        print(Fore.YELLOW + "icon.ico not found, continuing")
    youtube_window.title("YouTube")

    youtube_window.update()
    window_width = youtube_window.winfo_width()

    top_frame = customtkinter.CTkFrame(master=youtube_window, width=window_width, height=50)
    top_frame.pack(padx=10, pady=10)
    customtkinter.CTkLabel(master=top_frame, text="YouTube", text_color="grey",font=("", 20), width=window_width, height=50).pack()

    YouTube_url = customtkinter.CTkEntry(master=youtube_window, placeholder_text="YouTube URL:")
    YouTube_url.pack(padx=10, pady=0)
    YouTube_to_mp4_button = customtkinter.CTkButton(master=youtube_window, command=lambda: yt_to_mp4(), text="YouTube to mp4")
    YouTube_to_mp4_button.pack(padx=10, pady=10)
    YouTube_to_mp3_button = customtkinter.CTkButton(master=youtube_window, command=lambda: yt_to_mp3(), text="YouTube to mp3")
    YouTube_to_mp3_button.pack(padx=10, pady=0)
    back_button = customtkinter.CTkButton(master=youtube_window, command=youtube_window.destroy, text="Back")
    back_button.pack(padx=10, pady=10)

def spotify(root): #using spotdl https://github.com/marshallcares/spotdl
    def sp_song(spotify_url):
        url = str(spotify_url.get())
        try:
            if "track" in url:
                os.chdir(spotify_songs_folder)
                subprocess.run(['spotdl', url], check=True)
                CTkMessagebox(message="Song successfully downloaded to content/spotify/songs", icon="check", option_1="OK")
            elif "album" in url:
                CTkMessagebox(title="Error", message=f"{url} seems to be an album", icon="cancel")
            elif "playlist" in url:
                CTkMessagebox(title="Error", message=f"{url} seems to be a playlist", icon="cancel")
            else:
                CTkMessagebox(title="Error", message=f"{url} doesnt seem to be track, album or playlist", icon="cancel")
        except Exception as e:
            CTkMessagebox(title="Error", message=f"{e}", icon="cancel") 

    def sp_album(spotify_url):
        url = str(spotify_url.get())
        try:
            if "track" in url:
                CTkMessagebox(title="Error", message=f"{url} seems to be a track", icon="cancel")
            elif "album" in url:
                factor_url = url.strip("https://open.spotify.com/").replace("/", "-")
                factor_url = factor_url.replace("=", "-")
                factor_url = factor_url.replace("?", "-")
                os.chdir(spotify_albums_folder)
                time.sleep(0.5)
                os.mkdir(f"{spotify_albums_folder}\\{factor_url}")
                time.sleep(0.5)
                os.chdir(f"{spotify_albums_folder}\\{factor_url}")
                subprocess.run(['spotdl', url], check=True)
                CTkMessagebox(message=f"Album successfully downloaded to content/spotify/albums/{factor_url}", icon="check", option_1="OK")
            elif "playlist" in url:
                CTkMessagebox(title="Error", message=f"{url} seems to be a playlist", icon="cancel")
            else:
                CTkMessagebox(title="Error", message=f"{url} doesnt seem to be track, album or playlist", icon="cancel")
        except Exception as e:
            CTkMessagebox(title="Error", message=f"{e}", icon="cancel") 

    def sp_playlist():
        url = str(spotify_url.get())
        try:
            if "track" in url:
                CTkMessagebox(title="Error", message=f"{url} seems to be a track", icon="cancel")
            elif "album" in url:
                CTkMessagebox(title="Error", message=f"{url} seems to be an album", icon="cancel")
            elif "playlist" in url:
                factor_url = url.strip("https://open.spotify.com/").replace("/", "-")
                factor_url = factor_url.replace("=", "-")
                factor_url = factor_url.replace("?", "-")
                os.chdir(spotify_playlists_folder)
                time.sleep(0.5)
                os.mkdir(f"{spotify_playlists_folder}\\{factor_url}")
                time.sleep(0.5)
                os.chdir(f"{spotify_playlists_folder}\\{factor_url}")
                subprocess.run(['spotdl', url], check=True)
                CTkMessagebox(message=f"Playlist successfully downloaded to content/spotify/playlists/{factor_url}", icon="check", option_1="OK")
            else:
                CTkMessagebox(title="Error", message=f"{url} doesnt seem to be track, album or playlist", icon="cancel")
        except Exception as e:
            CTkMessagebox(title="Error", message=f"{e}", icon="cancel") 

    spotify_window = customtkinter.CTkToplevel(root)
    spotify_window.minsize(480, 270)
    spotify_window.maxsize(480, 270)
    try:
        spotify_window.after(300, lambda: spotify_window.iconbitmap(icon))
    except:
        print(Fore.YELLOW + "icon.ico not found, continuing")
    spotify_window.title("Spotify")

    spotify_window.update()
    window_width = spotify_window.winfo_width()

    top_frame = customtkinter.CTkFrame(master=spotify_window, width=window_width, height=50)
    top_frame.pack(padx=10, pady=10)
    customtkinter.CTkLabel(master=top_frame, text="Spotify", text_color="grey",font=("", 20), width=window_width, height=50).pack()

    spotify_url = customtkinter.CTkEntry(master=spotify_window, placeholder_text="Spotify URL:")
    spotify_url.pack(padx=10, pady=0)
    spotify_song_button = customtkinter.CTkButton(master=spotify_window, command=lambda: sp_song(spotify_url), text="Song")
    spotify_song_button.pack(padx=10, pady=10)
    spotify_album_button = customtkinter.CTkButton(master=spotify_window, command=lambda: sp_album(spotify_url), text="Album")
    spotify_album_button.pack(padx=10, pady=0)
    spotify_playlist_button = customtkinter.CTkButton(master=spotify_window, command=lambda: sp_playlist(spotify_url), text="Playlist")
    spotify_playlist_button.pack(padx=10, pady=10)

    back_button = customtkinter.CTkButton(master=spotify_window, command=spotify_window.destroy, text="Back")
    back_button.pack()

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
    top_frame.pack(padx=10, pady=10)
    customtkinter.CTkLabel(master=top_frame, text="spotitube GUI witten by github.com/3022-2/", text_color="grey",font=("", 20), width=window_width, height=50).pack()
    
    #buttons
    youtube_button = customtkinter.CTkButton(master=root, command=lambda: youtube(root), text="YouTube")
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