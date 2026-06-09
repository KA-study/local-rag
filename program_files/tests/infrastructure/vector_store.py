

from program_files.infrastructure.vector_store.base import VectorStore
from program_files.infrastructure.vector_store.chroma_store import ChromaVectorStore
from shared.schemas import EmbeddedChunk

def sample_chunk() -> EmbeddedChunk:
    ...


def test_add_and_count(vector_store: VectorStore):
    assert vector_store.count() == 0

    vector_store.add([sample_chunk()])

    assert vector_store.count() == 1

def test_search_returns_added_chunk(vector_store: VectorStore):
    chunk = sample_chunk()

    vector_store.add([chunk])

    result = vector_store.search(
        query_embedding=chunk.embedding,
        top_k=1
    )

    assert len(result) == 1
    assert result[0].chunk.text == chunk.chunk.text
