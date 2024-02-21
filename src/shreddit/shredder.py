from logging import Logger, basicConfig, getLogger, getLevelNamesMapping

from shreddit.config import Config


class Shredder(object):
    _logger: Logger
    _config: Config

    def __init__(self, config: Config, user: str, verbose: bool = False):
        basicConfig()
        self._logger = getLogger("shreddit")
        log_level = getLevelNamesMapping().get("DEBUG" if verbose else config.log_level.upper())
        self._logger.setLevel(level=log_level)

        self._config = config
        self._user = user

        self._logger.debug("Initializing shredder")
        self._logger.info("Initializing")
