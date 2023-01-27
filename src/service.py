from enums import LampEnum


class LampService:
    def switch_lamp(self, command: LampEnum, metadata: str | None = None):
        match command:
            case command.on:
                return {"Фонарь включили", "\U0001F4A1"}
            case command.color:
                return {f'Сменили цвет, фонарь {metadata}'},
            case command.off:
                return {"Фонарь выключили"}
            case _:
                return {"Команда не может быть обработана"}
