from fastapi import FastAPI
import uvicorn
from routes.user import user

app = FastAPI()
app.include_router(user)

if __name__ == "__main__":
    try:
        uvicorn.run(app="app:app", reload=True)
    except KeyboardInterrupt:
        print("App stop")