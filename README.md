# Фонарь

При старте приложения вызывается внешняя система - сервер фонаря. Далее приложение готово примать от сервера команды:
on, off, color через api методом post по Протоколу Управления Фонарем.

Запуск проекта:

1. Настройка виртуальноего окружения

```shell
python -m venv venv
```

2. Активация окружения:

```shell
venv\Scripts\activate.bat - для Windows
source venv/bin/activate - для Linux и MacOS
```

3. Установить все зависимости

```shell
pip install -r requirements.txt
```

4. Запустить проект из директории lamp

```shell
uvicorn main:app --reload
```