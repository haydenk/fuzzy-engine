from tempfile import gettempdir

from pydantic import BaseModel, Field
from yaml import safe_load


class Config(BaseModel):
    hours: int = Field(default=24)
    max_score: int = Field(default=100)
    sort: str = Field(default="new")
    clear_vote: bool = Field(default=False)
    item: str = Field(default="overview")
    whitelist: list[str] = Field(default=[])
    blacklist: list[str] = Field(default=[])
    whitelist_ids: list[str] = Field(default=[])
    multi_blacklist: list[str] = Field(default=[])
    multi_whitelist: list[str] = Field(default=[])
    trial_run: bool = Field(default=False)
    whitelist_distinguished: bool = Field(default=True)
    whitelist_gilded: bool = Field(default=True)
    nuke_hours: int = Field(default=4320)
    keep_a_copy: bool = Field(default=False)
    save_directory: str = Field(default=gettempdir())
    replacement_format: str = Field(default="random")
    log_level: str = Field(default="debug")
    wordlist: list[str] = Field(default=[])
    batch_cooldown: int = Field(default=10)

    def __init__(self, **data: any):
        user_config = safe_load(open(data.get('config_filename')))
        super().__init__(**user_config)
