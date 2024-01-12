"""File for the main config."""
import dataclasses
import enum
import pathlib
import typing as t

import omegaconf
import typing_extensions as te

from src import utils

BASE_DIR = pathlib.Path(__file__).parent.parent


@dataclasses.dataclass
class SentryConfigSection:
    """Sentry config section."""

    enabled: bool = False
    dsn: str = "..."
    traces_sample_rate: float = 1.0


class LoggingLevel(enum.IntEnum):
    TRACE = 5
    """Use only for tracing error without a debugger."""
    DEBUG = 10
    INFO = 20
    SUCCESS = 25
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


@dataclasses.dataclass
class LoggingSection:
    level: LoggingLevel = LoggingLevel.INFO
    json: bool = False


@dataclasses.dataclass
class Config(metaclass=utils.Singleton):
    """The main config that holds everything in itself."""

    token: str = "..."
    start_command_photo_id: str = "..."
    admins: list[int] = dataclasses.field(default_factory=list)
    sentry: SentryConfigSection = dataclasses.field(default_factory=SentryConfigSection)
    logging: LoggingSection = dataclasses.field(default_factory=LoggingSection)

    @classmethod
    def _setup(cls) -> te.Self:
        """Set up the config.

        Loads config from a file, and then rewrites it with data merged from defaults.
        """
        config_path = BASE_DIR / "data" / "config.yml"
        config_path.parent.mkdir(exist_ok=True)
        cfg = omegaconf.OmegaConf.structured(cls)

        if config_path.exists():
            loaded_config = omegaconf.OmegaConf.load(config_path)
            cfg = omegaconf.OmegaConf.merge(cfg, loaded_config)

        with open(config_path, "w") as config_file:
            omegaconf.OmegaConf.save(cfg, config_file)

        return t.cast(te.Self, cfg)
