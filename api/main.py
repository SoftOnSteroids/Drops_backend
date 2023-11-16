from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

from v1.routers import droppers, doses

app = FastAPI()

load_dotenv()

# Routers
app.include_router(droppers.router)
app.include_router(doses.router)


@app.get("/")
async def root():
    return "Drops API vAlfa - Docker Dev"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="debug", reload=True)
