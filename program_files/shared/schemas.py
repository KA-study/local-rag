from dataclasses import dataclass

@dataclass
class Document:
    page: int
    text: str
    source: str

@dataclass
class Chunk:
    text: str
    page: int
    source: str
    chunk_index: int

@dataclass
class EmbeddedChunk:
    chunk: Chunk
    embedding: list[float]

@dataclass
class RetrievedChunk:
    chunk: Chunk
    #現在、小さいほど強い
    distance: float
