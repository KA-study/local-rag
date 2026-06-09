import pytest
import uuid

from program_files.infrastructure.vector_store.base import VectorStore
from program_files.infrastructure.vector_store.chroma_store import ChromaVectorStore
from shared.schemas import EmbeddedChunk, Chunk

@pytest.fixture(params=[
    ChromaVectorStore,
])
def vector_store(request, tmp_path) -> VectorStore:

    cls = request.param

    if cls is ChromaVectorStore:
        return cls(
            persist_directory=str(tmp_path),
            collection_name=f"test_{uuid.uuid4()}"
        )

    return cls()


def sample_chunk() -> EmbeddedChunk:
    return EmbeddedChunk(
        chunk=Chunk(
            text="This is a test sentence.",
            page=1,
            source="sample.pdf",
            chunk_index=0
        ),
        embedding=[0.1, 0.2, 0.3]
    )


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


#chunk_idの管理を変更すべきだ。
def test_delete(vector_store: VectorStore):
    chunk = sample_chunk()

    vector_store.add([chunk])

    chunk_id = (
        f"{chunk.chunk.source}_"
        f"{chunk.chunk.page}_"
        f"{chunk.chunk.chunk_index}"
    )

    vector_store.delete([chunk_id])

    assert vector_store.count() == 0
