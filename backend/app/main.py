from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import close_mongo_connection, connect_to_mongo
from app.routers import auth, dashboard, projects, tasks


app = FastAPI(
    title="Project & Task Management API",
    description="Full-stack project and task management system built with FastAPI and MongoDB.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event() -> None:
    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await close_mongo_connection()


app.include_router(auth.router, prefix="/api")
app.include_router(projects.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")
app.include_router(dashboard.router, prefix="/api")


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
