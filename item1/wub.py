import re


def string_decoder(song):
    clean_string = song.replace("WUB", " ").strip()
    return re.sub(" +", " ", clean_string)
