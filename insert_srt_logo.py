import os
import subprocess
import sys

source_path = "/Volumes/Data/fix_video/rough_video/"
srt_path = "/Volumes/Data/fix_video/vanessa_srt/"
dest_path = "/Volumes/Data/fix_video/vanessa_video/"
logo_path = "/Volumes/Data/fix_video/logo.png"

files = os.listdir(source_path)


for file in files:
    cmd = "source /etc/profile &&  ffmpeg -i '%s' -vf \"movie=%s[logo];[in][logo]overlay=x='if(gte(t\,2)\,((t-2)*80)-w\,NAN)'\",subtitles='%s' '%s' >> log.lgo"
    if file.endswith(".mp4"):
        print(file)

        mp4_src = source_path + file.strip()
        writePath = dest_path + file.strip()

        srt = file.replace(".mp4", ".srt").strip()
        srt_file = srt_path + srt.strip()
        out_file = dest_path + file.strip()

        cmd = cmd % (mp4_src, logo_path, srt_file, out_file)
        sys.stdout.flush()
        ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        stdout, stderr = ret.communicate()
        print(ret.returncode)
        print(stdout)
        print(stderr)
        ret.stdout.close()
        ret.stderr.close()
        # wait finished
        # ret_out = ret.stdout.read().decode('utf8')
        # print(ret_out)
