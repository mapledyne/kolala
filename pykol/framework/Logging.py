import logging


try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass


class Logging(object):

    logging.getLogger(__name__).addHandler(NullHandler())
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')  # noqa
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @staticmethod
    def warning(msg):
        Logging.logger.warning(msg)

    @staticmethod
    def info(msg):
        Logging.logger.info(msg)

    @staticmethod
    def critical(msg):
        Logging.logger.critical(msg)

    @staticmethod
    def log(level, msg):
        Logging.logger.log(level, msg)

    @staticmethod
    def log_level(level=None):
        if level is not None:
            Logging.logger.setLevel(level)
        return Logging.logger.getEffectiveLevel()

    @staticmethod
    def error(err):
        Logging.logger.error(err)
