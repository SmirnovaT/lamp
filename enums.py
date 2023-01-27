from enum import Enum


class LampEnum(str, Enum):
    on = "on"
    off = "off"
    color = "color"
