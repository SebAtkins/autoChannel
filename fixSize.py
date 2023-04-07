import os

def fixSize(video):
    out = video[:-4] + "2" + video[-4:]
    print(out)
    os.system(f"ffmpeg -y -i {video} -vf \"pad=ih*16/9:ih:(ow-iw)/2:(oh-ih)/2\" temp.mp4")
    os.system(f"ffmpeg -y -i temp.mp4 -vf \"scale=1920:-1\" {video}")

if __name__ == "__main__":
    fixSize("bbnomula\\2023-02-23_20-53-03_UTC.mp4")
