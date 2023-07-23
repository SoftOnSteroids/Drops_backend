from fastapi import FastAPI
import uvicorn
from v1.routers import droppers, doses

app = FastAPI()

# Routers
app.include_router(droppers.router)
app.include_router(doses.router)

@app.get("/")
async def root():
    return "API v1"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)