from dataclasses import dataclass

"""
重要：
このファイルは、ほかのファイルからインポートしてはならない。
"""

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

class ExitCommandError(Exception):
    pass
    #現在の処理ブロックを終了するための例外

#=================interface関連=====================

@dataclass
class TreeNode:
    name: str
    current: str | None
    choices: list[str] | None
    #前方参照
    children: list["TreeNode"]

@dataclass
class EditRequest:
    path: tuple[str, ...]
    selected_name: str
