from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from pytube import YouTube, Playlist, Channel
from pytubefix import Channel as ChannelFIX
from CTkMessagebox import CTkMessagebox
from colorama import Fore, init

import customtkinter
import subprocess
import webbrowser
import time
import sys
import os
import re 

cwd = os.getcwd()
customtkinter.set_appearance_mode("dark")
init(autoreset=True)
#_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID"]

#pre code checks
try:
    if os.path.exists(f"{cwd}\\content") == False:
        os.mkdir(f"{cwd}\\content")
        time.sleep(1)
        os.mkdir(f"{cwd}\\content\\youtube")
        os.mkdir(f"{cwd}\\content\\youtube\\videos")
        os.mkdir(f"{cwd}\\content\\youtube\\videos\\mp3")
        os.mkdir(f"{cwd}\\content\\youtube\\videos\\mp4")
        os.mkdir(f"{cwd}\\content\\youtube\\playlists")
        os.mkdir(f"{cwd}\\content\\youtube\\playlists\\mp3")
        os.mkdir(f"{cwd}\\content\\youtube\\playlists\\mp4")
        os.mkdir(f"{cwd}\\content\\youtube\\channels")
        os.mkdir(f"{cwd}\\content\\youtube\\channels\\mp3")
        os.mkdir(f"{cwd}\\content\\youtube\\channels\\mp4")
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

youtube_videos_folder_mp3 = f"{cwd}\\content\\youtube\\videos\\mp3"
youtube_videos_folder_mp4 = f"{cwd}\\content\\youtube\\videos\\mp4"
youtube_playlists_folder_mp3 = f"{cwd}\\content\\youtube\\playlists\\mp3"
youtube_playlists_folder_mp4 = f"{cwd}\\content\\youtube\\videos\\mp4"
youtube_channels_folder_mp3 = f"{cwd}\\content\\youtube\\channels\\mp3"
youtube_channels_folder_mp4 = f"{cwd}\\content\\youtube\\channels\\mp4"

spotify_songs_folder = f"{cwd}\\content\\spotify\\songs"
spotify_albums_folder = f"{cwd}\\content\\spotify\\albums"
spotify_playlists_folder = f"{cwd}\\content\\spotify\\playlists"

logo_images = f"{cwd}\\images"

def sanitize_filename(filename):
    illegal_chars = r'[\\/:"*?=<>|]' 
    return re.sub(illegal_chars, "-", filename)

def youtube(root):
    def yt_to_mp4(root):
        pass
    def yt_to_mp3(root):
        def yt_mp3_video(youtube_url):
            try:
                url = str(youtube_url.get()).strip("")
                yt = YouTube(url)
                title = yt.title

                try:
                    title = sanitize_filename(title)
                    output_path = f"{youtube_videos_folder_mp3}\\{title}"
                except Exception as e:
                    CTkMessagebox(title="Error", message=f"{e}", icon="cancel")

                audio_stream = yt.streams.filter(only_audio=True).first()
                down = audio_stream.download(output_path=output_path)

                base, extension = os.path.splitext(down)
                new_file = base + '.mp3'
                original_stdout = sys.stdout
                sys.stdout = open(os.devnull, 'w')

                ffmpeg_extract_audio(down, new_file)
                os.remove(down)
                sys.stdout = original_stdout
                CTkMessagebox(message=f"{title} successfully downloaded to {output_path}", icon="check", option_1="OK")
            except Exception as e:
                CTkMessagebox(title="Error", message=f"{e}", icon="cancel")
        def yt_mp3_playlist(youtube_url):
            try:
                url = str(youtube_url.get()).strip("")
                playlist = Playlist(url)

                try:
                    title = sanitize_filename(playlist.title)
                    output_path = f"{youtube_playlists_folder_mp3}\\{title}"
                except Exception as e:
                    CTkMessagebox(title="Error", message=f"{e}", icon="cancel")

                try:
                    for video_url in playlist.video_urls:
                        yt = YouTube(video_url)
                        audio_stream = yt.streams.filter(only_audio=True).first()
                        down = audio_stream.download(output_path=output_path)
                        base, extension = os.path.splitext(down)
                        new_file = base + '.mp3'
                        original_stdout = sys.stdout
                        sys.stdout = open(os.devnull, 'w')

                        ffmpeg_extract_audio(down, new_file)
                        os.remove(down)
                        sys.stdout = original_stdout
                    CTkMessagebox(message=f"{title} successfully downloaded to {output_path}", icon="check", option_1="OK")
                except Exception as e:
                    CTkMessagebox(title="Error", message=f"{e}", icon="cancel")
            except Exception as e:
                CTkMessagebox(title="Error", message=f"{e}", icon="cancel")
        def yt_mp3_channel(youtube_url):
            try:
                url = str(youtube_url.get()).strip("")

                if "/channel/" not in url:
                    CTkMessagebox(title="Error", message=f"Channel url must be in format of /channel/(channel id)", icon="cancel")
                elif "/channel/" in url:
                    channel = ChannelFIX(url)
                    try:
                        for url in channel.video_urls:
                            try:
                                url = str(url).strip("<pytubefix.__main__.YouTube object: videoId=")
                                url = url.strip(">")
                                url = f"https://youtube.com/watch/{url}"
                                
                                yt = YouTube(url)
                                try:
                                    video_title = sanitize_filename(yt.title)
                                    title = sanitize_filename(channel.channel_name)
                                    output_path = f"{youtube_channels_folder_mp3}\\{title}"
                                except Exception as e:
                                    CTkMessagebox(title="Error", message=f"{e}", icon="cancel")
                                audio_stream = yt.streams.filter(only_audio=True).first()
                                down = audio_stream.download(output_path=output_path, filename=video_title)
                                base, extension = os.path.splitext(down)
                                new_file = base + '.mp3'
                                original_stdout = sys.stdout
                                sys.stdout = open(os.devnull, 'w')

                                ffmpeg_extract_audio(down, new_file)
                                os.remove(down)
                                sys.stdout = original_stdout
                            except Exception as e:
                                CTkMessagebox(title="Error", message=f"{e}", icon="cancel")

                        CTkMessagebox(message=f"{title} successfully downloaded to {output_path}", icon="check", option_1="OK")
                    except Exception as e:
                        CTkMessagebox(title="Error", message=f"{e}", icon="cancel")
                else:
                    CTkMessagebox(title="Error", message=f"some kind of error with your input - not sure what though", icon="cancel")                
            except Exception as e:
                CTkMessagebox(title="Error", message=f"{e}", icon="cancel")
        def yt_mp3_from_txt():
            CTkMessagebox(title="uncomleted code - this wont work", message=f"{e}", icon="cancel")

        ytmp3_window = customtkinter.CTkToplevel(root)
        ytmp3_window.minsize(480, 330)
        ytmp3_window.maxsize(480, 330)
        try:
            ytmp3_window.after(300, lambda: ytmp3_window.iconbitmap(f"{cwd}\\images\\youtube.ico"))
            ytmp3_window.after(300, lambda: ytmp3_window.lift())
        except:
            print(Fore.YELLOW + "icon.ico not found, continuing")
        ytmp3_window.title("YouTube to mp3")

        ytmp3_window.update()
        window_width = ytmp3_window.winfo_width()

        top_frame = customtkinter.CTkFrame(master=ytmp3_window, width=window_width, height=30, fg_color="#242424")
        top_frame.pack(padx=10, pady=10)

        youtube_url = customtkinter.CTkEntry(master=ytmp3_window, placeholder_text="YouTube URL:", width=350)
        youtube_url.pack(padx=10, pady=0)
        youtube_video_button = customtkinter.CTkButton(master=ytmp3_window, command=lambda: yt_mp3_video(youtube_url), text="Video", width=350)
        youtube_video_button.pack(padx=10, pady=10)
        youtube_playlist_button = customtkinter.CTkButton(master=ytmp3_window, command=lambda: yt_mp3_playlist(youtube_url), text="Playlist", width=350)
        youtube_playlist_button.pack(padx=10, pady=0)
        youtube_channel_button = customtkinter.CTkButton(master=ytmp3_window, command=lambda: yt_mp3_channel(youtube_url), text="Channel", width=350)
        youtube_channel_button.pack(padx=10, pady=10)

        spotify_from_txt = customtkinter.CTkButton(master=ytmp3_window, command=lambda: yt_mp3_from_txt(), text="Load from youtube_list.txt", width=350)
        spotify_from_txt.pack(padx=10, pady=0)

        back_button = customtkinter.CTkButton(master=ytmp3_window, command=ytmp3_window.destroy, text="Back", width=350)
        back_button.pack(padx=10, pady=10)
    youtube_window = customtkinter.CTkToplevel(root)
    youtube_window.minsize(480, 220)
    youtube_window.maxsize(480, 220)
    try:
        youtube_window.after(300, lambda: youtube_window.iconbitmap(f"{cwd}\\images\\youtube.ico"))
        youtube_window.after(300, lambda: youtube_window.lift())
    except:
        print(Fore.YELLOW + "icon.ico not found, continuing")
    youtube_window.title("YouTube")

    youtube_window.update()
    window_width = youtube_window.winfo_width()

    top_frame = customtkinter.CTkFrame(master=youtube_window, width=window_width, height=30, fg_color="#242424")
    top_frame.pack(padx=10, pady=10)

    YouTube_to_mp4_button = customtkinter.CTkButton(master=youtube_window, command=lambda: yt_to_mp4(root), text="YouTube to mp4", width=350)
    YouTube_to_mp4_button.pack(padx=10, pady=0)
    YouTube_to_mp3_button = customtkinter.CTkButton(master=youtube_window, command=lambda: yt_to_mp3(root), text="YouTube to mp3", width=350)
    YouTube_to_mp3_button.pack(padx=10, pady=10)
    back_button = customtkinter.CTkButton(master=youtube_window, command=youtube_window.destroy, text="Back", width=350)
    back_button.pack(padx=10, pady=0)

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

    def sp_playlist(spotify_url):
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
    def sp_from_txt():
        with open(f"{cwd}\\spotify_list.txt", "r") as file:
            file = file.readlines()
            for line in file:
                url = line.strip()
                try:
                    if "you can add spotify SONG links to download from txt - remove the links below and add what you want AS LONG AS RIGHT FORMAT" in url:
                        pass
                    else:
                        try:
                            if "track" in url:
                                os.chdir(spotify_songs_folder)
                                subprocess.run(['spotdl', url], check=True)
                                CTkMessagebox(message="Songs successfully downloaded to content/spotify/songs", icon="check", option_1="OK")
                            elif "album" in url:
                                CTkMessagebox(title="Error", message=f"{url} seems to be an album", icon="cancel")
                            elif "playlist" in url:
                                CTkMessagebox(title="Error", message=f"{url} seems to be a playlist", icon="cancel")
                            else:
                                CTkMessagebox(title="Error", message=f"{url} doesnt seem to be track, album or playlist", icon="cancel")
                        except Exception as e:
                            CTkMessagebox(title="error", message=f"{e}", icon="cancel")
                except Exception as e:
                    CTkMessagebox(title="error", message=f"{e}", icon="cancel")

    spotify_window = customtkinter.CTkToplevel(root)
    spotify_window.minsize(480, 330)
    spotify_window.maxsize(480, 330)
    try:
        spotify_window.after(300, lambda: spotify_window.iconbitmap(f"{cwd}\\images\\spotify.ico"))
        spotify_window.after(300, lambda: spotify_window.lift())
    except:
        print(Fore.YELLOW + "icon.ico not found, continuing")
    spotify_window.title("Spotify")

    spotify_window.update()
    window_width = spotify_window.winfo_width()

    top_frame = customtkinter.CTkFrame(master=spotify_window, width=window_width, height=30, fg_color="#242424")
    top_frame.pack(padx=10, pady=10)

    spotify_url = customtkinter.CTkEntry(master=spotify_window, placeholder_text="Spotify URL:", width=350)
    spotify_url.pack(padx=10, pady=0)
    spotify_song_button = customtkinter.CTkButton(master=spotify_window, command=lambda: sp_song(spotify_url), text="Song", width=350)
    spotify_song_button.pack(padx=10, pady=10)
    spotify_album_button = customtkinter.CTkButton(master=spotify_window, command=lambda: sp_album(spotify_url), text="Album", width=350)
    spotify_album_button.pack(padx=10, pady=0)
    spotify_playlist_button = customtkinter.CTkButton(master=spotify_window, command=lambda: sp_playlist(spotify_url), text="Playlist", width=350)
    spotify_playlist_button.pack(padx=10, pady=10)

    spotify_from_txt = customtkinter.CTkButton(master=spotify_window, command=lambda: sp_from_txt(), text="Load from spotify_list.txt", width=350)
    spotify_from_txt.pack(padx=10, pady=0)

    back_button = customtkinter.CTkButton(master=spotify_window, command=spotify_window.destroy, text="Back", width=350)
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

    top_frame = customtkinter.CTkFrame(master=root, width=window_width, height=50, fg_color="#242424")
    top_frame.pack(padx=10, pady=10)
    customtkinter.CTkLabel(master=top_frame, text="SPOTITUBE GUI", text_color="grey",font=("", 20), width=window_width, height=50).pack()
    
    #buttons
    youtube_button = customtkinter.CTkButton(master=root, command=lambda: youtube(root), text="YouTube", width=350)
    youtube_button.pack(padx=10, pady=0)
    spotify_button = customtkinter.CTkButton(master=root, command=lambda: spotify(root), text="Spotify", width=350)
    spotify_button.pack(padx=10, pady=10)

    github_button = customtkinter.CTkButton(master=root, command=lambda: webbrowser.open("https://github.com/3022-2/spotitube-gui"), text="GitHub", width=350)
    github_button.pack(padx=10, pady=0)
    exit_button = customtkinter.CTkButton(master=root, command=lambda: exit(), text="Exit", width=350)
    exit_button.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()