from dataclasses import dataclass


@dataclass
class ActiveSettings:
    history_db: str

@dataclass
class PassiveSettings:
    pdf_loader: str
    chunker: str

@dataclass
class InterfaceSettings:
    chat_interface: str
    session_manager_interface: str

@dataclass
class InfrastructureSettings:
    vector_store: str
    llm_engine: str
    usage_db: str
    embedder: str

@dataclass 
class Settings:
    active: ActiveSettings
    passive: PassiveSettings
    interface: InterfaceSettings
    infrastructure: InfrastructureSettings
