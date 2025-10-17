#Aqui pones una api melisma pa' 

import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017") # Aqui Makelele pone la uri de mongo
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["mini_lista_compras"]
