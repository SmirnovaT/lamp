from enums import LampEnum


class LampService:
    def switch_lamp(self, command: LampEnum, metadata: str | None = None):
        match command:
            case command.on | command.color | command.off:
                return {"command": command, "metadata": metadata}
            case _:
                return {"Команда не может быть обработана"}
