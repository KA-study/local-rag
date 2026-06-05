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
    #このdistanceがどのchunk/embeddingからの距離なのかについてのデータを含むべきでは？

@dataclass
class LLMResponse:
    text: str
    model: str
    usage: Usage | None

@dataclass
class Usage:
    input_tokens: int
    output_tokens: int
    model_name: str


@dataclass
class ModelPrice:
    input_fee: float
    output_fee: float

PRICE_TABLE: dict[str, ModelPrice] = {
    "gpt-4.1-mini": ModelPrice(0.40, 1.60),
}
