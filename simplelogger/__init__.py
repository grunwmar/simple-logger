from datetime import datetime
from abc import ABC, abstractmethod
from simplelogger.dotdict import DotDict


HOOK = DotDict({})  # just abbreviation


class BaseLogWriter(ABC):

    def __init__(self, message_template: str, time_stamp_format: str):
        self._message_template = message_template
        self._time_stamp_format = time_stamp_format

    def get_filled_template(self, message) -> str:

        if isinstance(message["time"], str):
            message["time"] = message["time"]
        else:
            message["time"] = message["time"].strftime(self._time_stamp_format)

        filled_message = self._message_template.format(**message)
        return filled_message

    @abstractmethod
    def write(self, message: dict) -> None: ...


class Logger:

    def __init__(
        self,
        name: str,
        log_writers: list[BaseLogWriter],
        dt_object: str | datetime = datetime.now(),
    ):
        self._properties: dict = {"name": name}
        self._log_writers = log_writers
        self._dt_object = dt_object
        HOOK.update({name: self})

    def _proto_log(self, *args, **kwargs) -> None:
        for writer in self._log_writers:
            message_dict = {}
            message_dict.update(self._properties)
            message_dict.update({"time": self._dt_object})
            message_dict.update(kwargs)
            writer.write(message_dict)
