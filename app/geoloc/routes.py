from fastapi import APIRouter
from pydantic import BaseModel
from .controller import Controller
from starlette.requests import Request


router = APIRouter()
controller = Controller()


@router.get('/')
def get(ip):
    return controller.get_geoloc(ip)
