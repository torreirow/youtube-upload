import os
import re

from googleapiclient.http import MediaFileUpload

from .lib import debug

LANG_RE = re.compile(r"^[a-z]{2,3}(-[A-Za-z0-9]+)?$")

def get_language(path, default):
    """Return the language code from a filename like name.nl.srt (or default)."""
    lang = os.path.splitext(os.path.splitext(os.path.basename(path))[0])[1][1:]
    return lang if LANG_RE.match(lang) else default

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
