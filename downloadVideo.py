from instaloader import *
from fixSize import fixSize
import os

def containsTrue(arr):
    val = False

    for x in arr:
        if x:
            val = True

    return val

def downloadVideo(account, maxPosts):
    # Download last 4 videos
    instance = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(instance.context, account)
    i = 0
    for post in profile.get_posts():
        if containsTrue(post.get_is_videos()):
            i += 1
            if i > maxPosts:
                break
            instance.download_post(post, target=profile.username)

    # Remove all files that are not .mp4
    for file in os.listdir(account):
        if not file.endswith(".mp4"):
            os.remove(account + "\\" + file)
        else:
            fixSize(account + "\\" + file)
    # Remove temp.mp4
    os.remove("temp.mp4")

if __name__ == "__main__":
    downloadVideo("bbnomula", 4)
