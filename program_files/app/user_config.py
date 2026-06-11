from dataclasses import dataclass



@dataclass
class Path:
    pdf: str
    history_db: str
    usage_db: str

@dataclass
class UserConfig:
    path: Path
