import re

from enum import Enum

class Sites(Enum):
    YouTube = "YouTube"
    Unknown = "Unknown"

url_regex = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

def get_url(msg):
    regex = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

    if re.search(regex, msg):
        result = regex.search(msg)
        url = result.group(0)
        return url
    else:
        return None


def identify_url(msg):
    if msg is None:
        return Sites.Unknown
    elif "https://www.youtu" in msg or "https://youtu.be" in msg:
        return Sites.YouTube
    else:
        return Sites.Unknown
