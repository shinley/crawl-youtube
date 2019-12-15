'''
Created on 2019年1月29日
@author:  Yvon_fajin
'''
import os, os.path, time


def rename(file, keyword):
    ''' file: 文件路径    keyWord: 需要修改的文件中所包含的关键字 '''
    start = time.clock()
    cur_dir = os.path.dirname(__file__)
    vtt_dir = cur_dir + "/" + file
    items = os.listdir(vtt_dir)
    os.chdir(vtt_dir)
    print(os.getcwd())
    for name in items:
        print(name)
        # 遍历所有文件
        if not os.path.isdir(name):
            if keyword in name:
                new_name = name.replace(keyword, "'")
                os.renames(name, new_name)
        else:
            continue
    print('-----------------------分界线------------------------')
    items = os.listdir(cur_dir)
    for name in items:
        print(name)


rename('vtt/srt', "$")
