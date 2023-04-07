from downloadVideo import downloadVideo
from stitchVideos import stitchVideos
from createList import createList
from uploadVideo import upload
import shutil, os

accounts = ["bbnomula", "connorprice_", "magmidt"]
listFile = "merge.txt"
output = "final.mp4"
title = "Upload Test"
desc = "This is a test of my auto upload script"
tags = ["Epic", "Swag", "Gamer moment"]
cat = "23" # 23 is comedy
privacy = "unlisted" # Can be public, unlisted or private

# Download videos and create list
paths = []
for i in accounts:
    downloadVideo(i, 2)
    paths.extend(createList(i))

with open(listFile, "w") as file:
    file.write("\n".join(paths))

# Stitch videos together
stitchVideos(listFile, output)

# Upload video 
upload(title, desc, tags, cat, privacy, output)

# Clear directory of files
for i in accounts:
    shutil.rmtree(i)
os.remove(listFile)
os.remove(output)
