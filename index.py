# coding: utf8
import sys
import os
import zipfile

print '下載Youtube音樂專用'

download_type = input("轉入單首請輸入 0\n轉入整份播放清單請輸入 1\n")
source_dir = raw_input("請輸入資料夾名稱\n")
if download_type == 0:
    print '你選擇單首下載'
    url = raw_input("請輸入youtube網址\n")
    cmd = "youtube-dl -o " + source_dir + \
        "/'%(title)s.%(ext)s' -x --audio-format mp3 --embed-thumbnail -i --add-metadata " + url
    os.system(cmd)
elif download_type == 1:
    print '你選擇播放清單下載'
    url = raw_input("請輸入播放清單網址\n")
    list_type = raw_input("是否全部下載 y/n\n")
    if list_type == "y":
        cmd = "youtube-dl -o " + source_dir + \
            "/'%(title)s.%(ext)s' -x --audio-format mp3 --embed-thumbnail -i --add-metadata " + url
    elif list_type == "n":
        start = raw_input("請輸入要從第幾首開始\n")
        end = raw_input("請輸入要從第幾首結束\n")
        cmd = "youtube-dl -o " + source_dir + \
            "/'%(title)s.%(ext)s' -x --audio-format mp3 --embed-thumbnail -i --playlist-items " + \
            start + "-" + end + " --add-metadata " + url
    os.system(cmd)

print '開始壓縮'
zf = zipfile.ZipFile(source_dir + '.ZIP', mode = 'w', compression = zipfile.ZIP_DEFLATED)
os.chdir(source_dir)
#print sFilePath
for root, folders, files in os.walk(".\\"):
    for sfile in files:
        aFile = os.path.join(root, sfile)
        #print aFile
        zf.write(aFile)
zf.close()