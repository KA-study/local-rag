from dataclasses import dataclass



@dataclass(frozen=True)
class Path:
    pdf: str
    history_db: str
    usage_db: str

@dataclass(frozen=True)
class UserConfig:
    path: Path
