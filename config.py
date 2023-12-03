from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6130431757:AAFqc13P_5r-E8RAdjW8-JS6qUZcfRr1khk")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://ammu:ammu@cluster0.kmy3bak.mongodb.net/?retryWrites=true&w=majority",
)
