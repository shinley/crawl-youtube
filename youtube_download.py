from __future__ import unicode_literals
import youtube_dl


def my_hook(d):
    print(d)
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'proxy':'http://127.0.0.1:7890',
    'subtitlesformat': 'srt',
    'writeautomaticsub': True,
    'progress_hooks': [my_hook],
    'nocheckcertificate': True,
    'outtmpl': '%(title)s%(ext)s'
}

with open('video_url.txt', 'r') as video_url:
    while True:
        line = video_url.readline()
        if not line:
            break

        url = "https://www.youtube.com" + line

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
