from googleapiclient.http import MediaFileUpload

from .lib import debug

def add_captions(youtube, video_id, path, lang):
    """Upload a captions file (e.g. SRT) as a caption track for the video."""
    debug("Adding captions: {0} (language={1})".format(path, lang))
    body = {
        "snippet": {
            "videoId": video_id,
            "language": lang,
            "name": "",
            "isDraft": False,
        },
    }
    media = MediaFileUpload(path, mimetype="application/octet-stream")
    return youtube.captions().insert(part="snippet", body=body,
                                     media_body=media).execute()
