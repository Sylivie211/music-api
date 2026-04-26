songs = [
    {"id": 1, "title": "HUMBLE.", "artist": "Kendrick Lamar"},
    {"id": 2, "title": "God's Plan", "artist": "Drake"},
]

def get_all_songs():
    return songs

def get_song_by_id(id):
    for song in songs:
        if song["id"] == id:
            return song
    return None