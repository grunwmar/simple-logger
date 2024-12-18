from datetime import datetime
from example.custom_logger import CustomLogger, ConsoleLogWriter, FileLogWriter
from pytz import timezone


def run():
    msg_template = "{name} [{strlevel} ] {time} > {msg}\n"
    ts_template = "%Y/%m/%d - %H:%M:%S %Z"

    logger = CustomLogger(
        "CustomLogger",
        log_writers=[
            ConsoleLogWriter(
                message_template=msg_template,
                time_stamp_format=ts_template,
            ),
            FileLogWriter(
                message_template=msg_template,
                time_stamp_format=ts_template,
            ),
        ],
        dt_object=timezone("Europe/Prague")
        .localize(datetime.now())
        .isoformat(timespec="microseconds"),
    )

    # test of defined methods
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
