from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psapp_clone_backend.infrastructure.logging.logging_config import get_logger
from psapp_clone_backend.infrastructure.middlewares.auth_middleware import AuthMiddleware
from psapp_clone_backend.modules.profile.infrastructure.router import router as profile_router
from psapp_clone_backend.modules.friends.infrastructure.router import router as friends_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    logger = get_logger(__name__)
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
app.include_router(profile_router)
app.include_router(friends_router)