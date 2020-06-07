import re


def string_decoder(song):
    return re.sub("(WUB)+", " ", song).strip()
