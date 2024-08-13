import uvicorn
from fastapi import FastAPI
from logging_setup import LoggerSetup
import logging
from controllers import home  # Import the router before using it

# Setup root logger
logger_setup = LoggerSetup()

# Get logger for module
LOGGER = logging.getLogger(__name__)

def init_app():
    app = FastAPI(
        title="Hult - Application",
        description="Fast API",
        version="1.0.0"
    )

    @app.on_event("startup")
    async def startup():
        LOGGER.info("--- Start up App -----")

    @app.on_event("shutdown") 
    async def shutdown():
        LOGGER.info("----- Shutdown ------")

    app.include_router(home.router)  # Include the router

    return app

app = init_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8888, reload=True)







