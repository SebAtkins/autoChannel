from instaloader import *
import os

def downloadVideo(account, maxPosts):
    # Download last 4 videos
    instance = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(instance.context, account)
    i = 0
    for post in profile.get_posts():
        if post.is_video:
            i += 1
            if i > maxPosts:
                break
            instance.download_post(post, target=profile.username)

    # Remove all files that are not .mp4
    for file in os.listdir(account):
        if not file.endswith(".mp4"):
            os.remove(account + "\\" + file)

if __name__ == "__main__":
    downloadVideo("bbnomula", 5)
