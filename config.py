from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6009759960:AAEMOCsUrfzdqesHaXE214ERgqQr1sRzlhU")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://moni:<password>@cluster0.i3djv5s.mongodb.net/?retryWrites=true&w=majority",
)
