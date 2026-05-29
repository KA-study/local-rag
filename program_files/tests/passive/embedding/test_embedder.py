from passive.embedding.embedder import STEmbedder
from shared.schemas import Chunk, EmbeddedChunk


def create_sample_chunks() -> list[Chunk]:
    
    return[
        Chunk(
            text="sample text",
            page=1,
            source="sample.pdf",
            chunk_index=1,
        ),
        Chunk(
            text="sample text2",
            page=2,
            source="sample2.pdf",
            chunk_index=2
            )
    ]


def test_embed_batch_returns_embedded_list():

    embedder = STEmbedder()
    chunks = create_sample_chunks()

    embedded_chunks = embedder.embed_batch(chunks)

    for embedded_chunk in embedded_chunks:

        assert isinstance(embedded_chunk, EmbeddedChunk)
        assert isinstance(embedded_chunk.embedding, list)
        assert len(embedded_chunk.embedding) > 0
