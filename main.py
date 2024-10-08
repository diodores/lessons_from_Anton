from fastapi import FastAPI
import uvicorn
from hotel import router as hotel_router


app = FastAPI()
app.include_router(hotel_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host="127.0.0.1", port=8000)