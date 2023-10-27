from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6577602955:AAHpVhSSau9jV7K1fPFVDa2io5F7eMfRlqk")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://karthika:karthika@cluster0.6jms6m3.mongodb.net/?retryWrites=true&w=majority",
)
