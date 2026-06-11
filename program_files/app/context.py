from dataclasses import dataclass

from program_files.app.components import Components
from program_files.app._types import (
    DEFAULT_COMPONENTS,
    DEFAULT_USER_ID
)

@dataclass
class AppContext:
    user_id: str = DEFAULT_USER_ID
    components: Components = DEFAULT_COMPONENTS

    
