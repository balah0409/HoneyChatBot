from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6009759960:AAGA_Pshq9D3TvtQWf1pgkv0X_JC5WuDDzQ")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://moni:moni@cluster0.dcufenj.mongodb.net/?retryWrites=true&w=majority",
)
