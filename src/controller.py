from fastapi import APIRouter, Depends

from src.schema import Lamp
from src.service import LampService

lamp_router = APIRouter(
    prefix="/api/lamp", tags=["lamp"], responses={404: {"description": "Not found"}}
)


@lamp_router.post("/command")
def switch_lamp(lamp: Lamp, service: LampService = Depends(LampService)):
    return service.switch_lamp(lamp)
