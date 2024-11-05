from fastapi import FastAPI
import uvicorn
from logging_setup import LoggerSetup
import logging

# Setup root logger
logger_setup = LoggerSetup()

# Get logger for module
LOGGER = logging.getLogger(__name__) 

def init_app():
    apps = FastAPI(
        title="Thabo Chalatse Logging System",
        description="FastAPI",
        version="1.0.0"
    )

    @apps.on_event("startup")  # Use 'apps' here
    async def startup():
        LOGGER.info("---- startup APP -----")

    @apps.on_event("shutdown")  # Use 'apps' here
    async def shutdown():
        LOGGER.info("----- shutdown APP -----")

    @apps.get('/')  # Use 'apps' here
    def home():
        return "welcome home!"
    
    from controllers import home
    apps.include_router(home.router)
    
    return apps

app = init_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8888, reload=True)
