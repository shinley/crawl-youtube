import os

files = os.listdir("./video")

for file in files:
    if file.endswith(".srt"):
        print(file)

        readPath = './video/'+file
        writePath = './srt/'+file

        with open(writePath, 'a+', encoding='utf-8') as outfiile, open(readPath, 'r', encoding='utf-8') as f:
            lines_seen = set()
            for line in f:
                if line not in lines_seen:
                    outfiile.write(line)
                    if not line == '\n':
                        lines_seen.add(line)
