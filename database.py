import motor.motor_asyncio
import os


from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

print(motor.version)
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get('mongodb_uri'),8000)
db = client.demo_db