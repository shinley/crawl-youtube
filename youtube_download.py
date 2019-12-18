from __future__ import unicode_literals
import youtube_dl

start = 0
end = 20


def my_hook(d):
    print(d)
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


with open('mmmEnglish_url.txt', 'r') as f:
    all_list = list(f)
    all_list.reverse()

    while start < end:
        if len(all_list) >= start + 1:
            line = all_list[start]

        temp_count = start + 1
        count = '%03d' % temp_count
        ydl_opts = {
            'proxy': 'http://127.0.0.1:7890',
            'subtitlesformat': 'vtt',
            'writeautomaticsub': True,
            'progress_hooks': [my_hook],
            'nocheckcertificate': True,
            'format':'mp4',
            'outtmpl': "./mmm_video/" + count + '.%(title)s.%(ext)s'
        }

        url = "https://www.youtube.com" + line
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        start = start + 1
