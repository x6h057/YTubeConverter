from flask import Flask, render_template, request, send_file
import yt_dlp
import os
import time
import source.config as config
import shutil

def download_video(url, format_type, folder="temp"):
    ydl_opts = config.config.get(format_type, config.config["mp3"])
    ydl_opts["outtmpl"] = os.path.join(folder, "%(title)s.%(ext)s")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        ext = "mp3" if format_type == "mp3" else "mp4"
        filename = f"{info['title']}.{ext}"
        filepath = os.path.join(folder, filename)

        return send_file(filepath, as_attachment=True)

def cleanup(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                print(f"Cleaning up: {folder}")
                os.unlink(file_path)
                print(f"Deleted: {filename}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def auto_cleanup(folder, timeout):
    current_time = time.time()
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                print(f"Cleaning up: {folder}")
                file_age = current_time - os.path.getctime(file_path)
                if file_age > timeout:
                    os.unlink(file_path)
                    print(f"Deleted: {filename}")
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
