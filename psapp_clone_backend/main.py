from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psapp_clone_backend.infrastructure.logging.logging_config import setup_logging
from psapp_clone_backend.features.check_profile import router as check_profile_router
import logging

from psapp_clone_backend.infrastructure.middlewares.auth_middleware import AuthMiddleware

setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger = logging.getLogger("main")
    logger.info("App Startup...")
    yield

app = FastAPI(version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(AuthMiddleware)

app.include_router(check_profile_router.router)

