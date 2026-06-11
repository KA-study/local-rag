from dataclasses import dataclass

from program_files.app.settings import Settings

@dataclass
class AppContext:
    user_id: str
    settings: Settings
    
