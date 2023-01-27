from enums import LampEnum
from src.schema import Lamp


class LampService:
    def switch_lamp(self, lamp: Lamp):
        match lamp.command:
            case LampEnum.on:
                return {"Фонарь включили", "\U0001F4A1"}
            case LampEnum.color:
                return {f'Сменили цвет, фонарь {lamp.metadata}'},
            case LampEnum.off:
                return {"Фонарь выключили"}
            case _:
                return {"Команда не может быть обработана"}
