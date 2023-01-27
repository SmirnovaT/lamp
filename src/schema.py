from pydantic import BaseModel

from enums import LampEnum


class Lamp(BaseModel):
    command: LampEnum
    metadata: str | None = None
