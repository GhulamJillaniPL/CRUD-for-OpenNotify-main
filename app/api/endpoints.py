from fastapi import APIRouter, HTTPException
from ..services.iss_service import ISSService
from ..models import ISSLocation, AstronautData

router = APIRouter()
iss_service = ISSService()

@router.get("/iss-now.json", response_model=ISSLocation)
async def get_iss_location():
    """
    Get current ISS location
    """
    try:
        location = iss_service.get_iss_location()
        return location
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/astros", response_model=AstronautData)
async def get_astronauts():
    """
    Get current astronauts in space
    """
    try:
        astronauts = iss_service.get_astronauts()
        return astronauts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
