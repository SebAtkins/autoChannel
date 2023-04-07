from youtube_upload.client import YoutubeUploader

def upload(title, description, tags, categoryId, privacyStatus, file):
    uploader = YoutubeUploader(secrets_file_path="client_secrets.json")

    uploader.authenticate()

    # Video options
    options = {
        "title" : title, # The video title
        "description" : description, # The video description
        "tags" : tags,
        "categoryId" : categoryId,
        "privacyStatus" : privacyStatus, # Video privacy. Can either be "public", "private", or "unlisted"
        "kids" : False, # Specifies if the Video if for kids or not. Defaults to False.
    }

    # upload Video
    uploader.upload(file, options)

    uploader.close()
