from dataclasses import dataclass
from typing import Optional

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

@dataclass
class LLMResponse:
    text: str
    model: str
    usage: Usage | None

@dataclass
class Usage:
    input_tokens: int
    output_tokens: int
