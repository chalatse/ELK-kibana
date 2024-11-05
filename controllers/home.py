from fastapi import APIRouter
import logging


# Get logger module
LOGGER = logging.getLogger(__name__)

router = APIRouter(
    prefix='/home',
    tags=['home']
)

@router.get('')
async def welcome_home():
    LOGGER.info("Welcome Loggerstash Application")
    return "Welcome to LStash Application"


@router.get("/test")
async def test_home():
    LOGGER.info("Welcome page test")
    return "Welcome page test!!"


