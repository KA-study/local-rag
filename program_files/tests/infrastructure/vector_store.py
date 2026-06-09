

from program_files.infrastructure.vector_store.base import VectorStore
from program_files.infrastructure.vector_store.chroma_store import ChromaVectorStore
from shared.schemas import EmbeddedChunk

def sample_chunk() -> EmbeddedChunk:
    ...


def test_add_and_count(vector_store: VectorStore):
    assert vector_store.count() == 0

    vector_store.add([sample_chunk()])

    assert vector_store.count() == 1
