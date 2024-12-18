import sys
from simplelogger import Logger, BaseLogWriter


class ConsoleLogWriter(BaseLogWriter):
    def write(self, message: dict) -> str:
        string = self.get_filled_template(message)
        if message["level"] in [4, 3]:
            sys.stderr.write(string)
        else:
            sys.stdout.write(string)


class FileLogWriter(BaseLogWriter):
    def write(self, message: dict) -> str:
        string = self.get_filled_template(message)

        if message["level"] in [4, 3]:
            with open("example/err_log.txt", "a") as file:
                file.write(string)
        else:
            with open("example/log.txt", "a") as file:
                file.write(string)


class CustomLogger(Logger):

    LEVEL = ["debug", "info", "warning", "error", "critical"]

    LEVELS = [
        {"level": 0, "strlevel": "DEBUG   "},
        {"level": 1, "strlevel": "INFO    "},
        {"level": 2, "strlevel": "WARNING "},
        {"level": 3, "strlevel": "ERROR   "},
        {"level": 4, "strlevel": "CRITICAL"},
    ]

    def info(self, msg: str) -> None:
        self._proto_log(msg=msg, **self.LEVELS[0])

    def debug(self, msg: str) -> None:
        self._proto_log(msg=msg, **self.LEVELS[1])

    def warning(self, msg: str) -> None:
        self._proto_log(msg=msg, **self.LEVELS[2])

    def error(self, msg: str) -> None:
        self._proto_log(msg=msg, **self.LEVELS[3])

    def critical(self, msg: str) -> None:
        self._proto_log(msg=msg, **self.LEVELS[4])
