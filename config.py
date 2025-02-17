import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "26992030"))
API_HASH = os.environ.get("API_HASH", "4da7d71c6bc4512a886e41aca83a5ee3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7781040017:AAEo-zuKXfEBzHYpoaJ7CPtPyH0PVoNWqiI")
ADMIN = int(os.environ.get("ADMIN", "7406982863"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1002350746988")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002402091090"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sunil664023:eieqy2jRVIbzD29r@cluster0.ezot5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
