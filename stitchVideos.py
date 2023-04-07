from os import system

def stitchVideos(fileList, out):
    system(f"ffmpeg -f concat -i {fileList} -c copy {out}")
