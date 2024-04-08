from motor.motor_asyncio import AsyncIOMotorClient



def get_db():
    conn = AsyncIOMotorClient("mongodb://localhost:27017/test")
    try:
        yield conn
    finally:
        conn.close()