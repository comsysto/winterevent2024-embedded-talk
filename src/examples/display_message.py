import json

from src.esp8266.display import Display
from src.examples import service_request


def api_message():
    display = Display()
    display.on()

    status: {} = service_request.api_status()

    display.message(message=json.dumps(status), duration=3)
