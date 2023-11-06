from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6582609535:AAH1Xw6M-Gj4gNLMlFArc6iXSGpFM9-1GfU")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://ammu:ammu@cluster0.kmy3bak.mongodb.net/?retryWrites=true&w=majority",
)
