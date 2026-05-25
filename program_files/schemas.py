from dataclasses import dataclass

@dataclass
class Document:
    page: int
    text: str
    source: str

@dataclass
class Chunk:
    text: str
    source: str
    chunk_index: int
