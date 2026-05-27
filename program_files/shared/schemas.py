from dataclasses import dataclass

#今のところ下に継承されていく形になっている。
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
    text: str
    page: int
    source: str
    chunk_index: int
    embedding: list[float]

