from settings import *
from models import *


def ExtractInfo():
    fh = open("info.txt", "r")
    for line in fh:
        rank, album, artist, year, genre = line.split("|")
        genre = genre.encode('utf-8')
        InsertRecord(artist=artist, tracklist=None, genre=genre,
            album=album, rarity=0.0, art=None, year=year)
    fh.close()

ExtractInfo()
