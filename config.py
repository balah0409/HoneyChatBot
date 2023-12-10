from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6009759960:AAEXoV1tVEQjNg2kwApWlYe-7oPx7SNIBzw")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://cutegirl143bot:cutegirl143bot@cluster0.evn8tez.mongodb.net/?retryWrites=true&w=majority",
)
