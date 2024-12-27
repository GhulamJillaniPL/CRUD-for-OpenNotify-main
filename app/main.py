from fastapi import FastAPI
from .api.endpoints import router as api_router
from .config import settings

app = FastAPI(
    title=settings.api_title,
    version=settings.api_version
)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)