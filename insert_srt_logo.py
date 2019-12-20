import os
import subprocess
import sys

source_path = "/Volumes/pan/fix_video/rough_video/"
srt_path = "/Volumes/pan/fix_video/vanessa_srt/"
dest_path = "/Volumes/pan/fix_video/vanessa_video/"
logo_path = "/Volumes/pan/fix_video/logo.png"

files = os.listdir(source_path)


for file in files:
    cmd = "source /etc/profile &&  ffmpeg -i '%s' -vf \"movie=%s[logo];[in][logo]overlay=x='if(gte(t\,2)\,((t-2)*80)-w\,NAN)'\",subtitles='%s' '%s'"
    if file.endswith(".mp4"):
        print(file)

        mp4_src = source_path + file
        writePath = dest_path + file

        srt = file.replace(".mp4", ".srt")
        srt_file = srt_path + srt
        out_file = dest_path + file

        cmd = cmd % (mp4_src, logo_path, srt_file, out_file)
        sys.stdout.flush()
        ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        for line in iter(ret.stdout.readline, b''):
            line = line.decode('utf8')
            print(line)

        ret.stdout.close()
        # wait finished
        # ret_out = ret.stdout.read().decode('utf8')
        # print(ret_out)
