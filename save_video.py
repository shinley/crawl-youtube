
import requests
proxies = {"http":"127.0.0.1:7890", "https":"127.0.0.1:7890"}
response = requests.get('https://r1---sn-ipoxu-un5e7.googlevideo.com/videoplayback?expire=1573503063&ei=92vJXcfNMYmptQf485eYCQ&ip=36.231.120.123&id=o-AFXBhuC6j7KZlMZTjW-JP_W_91LKTGinrFvgWqaa377u&itag=22&source=youtube&requiressl=yes&mm=31%2C26&mn=sn-ipoxu-un5e7%2Csn-i3b7kn7d&ms=au%2Conr&mv=m&mvi=0&pcm2cms=yes&pl=20&initcwndbps=877500&mime=video%2Fmp4&ratebypass=yes&dur=314.885&lmt=1499172212895419&mt=1573481366&fvip=6&fexp=23842630&c=WEB&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRAIgQIA0VEilzEt1AR9WXZsf4tewn4ia0Nv-oHqhBdf53bUCIAWIYaRNHYAUtC4eDAgjesYDFmna_dxGHvJUt2hRofe1&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AHylml4wRQIgGngTxiyT_3ZitKBy77mfUP2h-KUmv9K2xLdGjEuztgMCIQDaEwCI60rQnnm3QKj_cYs_QaGs_cvqTSYkgb5CvOTexQ%3D%3D', proxies=proxies)
data = response.content
with open("test.mp4", 'wb') as f:
    f.write(data)
    f.close()
    print("下载完成!")