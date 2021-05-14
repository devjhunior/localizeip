from fastapi import APIRouter
from .geoloc import routes as geoLoc

apiRouter = APIRouter()
apiRouter.include_router(
    geoLoc.router, 
    tags=["geoloc"], 
    prefix='/geoloc'
)
