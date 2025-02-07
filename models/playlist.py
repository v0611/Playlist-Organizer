from datetime import datetime
from App.database import playlists_collection


class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        self.songs = []
        self.created_at = datetime.utcnow()

    def save(self):
        playlist_data = {
            "name": self.name,
            "songs": self.songs,
            "created_at": self.created_at
        }
        result = playlists_collection.insert_one(playlist_data)
        return result.inserted_id

    @staticmethod
    def get_all():
        return list(playlists_collection.find({}, {"_id": 0}))

    @staticmethod
    def delete_playlist(name):
        result = playlists_collection.delete_one({"name": name})
        return result.deleted_count > 0
