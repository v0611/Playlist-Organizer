import os
from dotenv import load_dotenv
from pymongo import MongoClient

# load environment variable
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# connect to Mongo
try:
    client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
    db = client["playlistDB"] # database name
    playlists_collection = db["playlists"]
    # Test connection
    # print("Successfully connected to MongoDB")
except Exception as e:
    print('Failed to connect to DB:', e)