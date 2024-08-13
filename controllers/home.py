from fastapi import APIRouter
import logging

# Get logger for module
LOGGER = logging.getLogger(__name__)

router = APIRouter(
    prefix="/home",
    tags=['home']
)

@router.get("")
async def welcome_home():
    LOGGER.info("Hult Application")
    return "Welcome Hult Application"

@router.get("/test")
async def test_home():
    LOGGER.info("Welcome page test!")
    return "Welcome to test page"

