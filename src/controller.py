from fastapi import APIRouter, Depends

from enums import LampEnum
from src.service import LampService

lamp_router = APIRouter(
    prefix="/api/lamp", tags=["lamp"], responses={404: {"description": "Not found"}}
)


@lamp_router.get("/{command}")
def switch_lamp(command: LampEnum, metadata: str | None = None, service: LampService = Depends(LampService)):
    return service.switch_lamp(command=command, metadata=metadata)
