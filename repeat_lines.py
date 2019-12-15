import shutil

readPath = '001.Living in the South of France.srt'
writePath = '001.Living in the South of France.m.srt'

lines_seen = set()
outfiile = open(writePath, 'a+', encoding='utf-8')

f = open(readPath, 'r', encoding='utf-8')

for line in f:
    if line not in lines_seen:
        outfiile.write(line)
        if not line == '\n':
            lines_seen.add(line)
