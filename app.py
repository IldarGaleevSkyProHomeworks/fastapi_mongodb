from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from routes.user import user



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Life span")
    yield
    print("Complete")
    
app = FastAPI(lifespan=lifespan)
app.include_router(user)

if __name__ == "__main__":
    try:
        uvicorn.run(app="app:app", reload=True)
    except KeyboardInterrupt:
        print("App stop")