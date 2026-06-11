from dataclasses import dataclass

from program_files.app.settings import Settings
from program_files.app._types import (
    DEFAULT_SETTINGS,
    DEFAULT_USER_ID
)

@dataclass
class AppContext:
    user_id: str = DEFAULT_USER_ID
    settings: Settings = DEFAULT_SETTINGS
    
