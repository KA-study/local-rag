from passive.pdf.chunker import TokenChunker
from shared.schemas import Document, Chunk

def test_make_chunk_returns_chunk_list():

    chunker = TokenChunker()

    docs = [
        Document(
            text="これはテスト用サンプルです。\nThis is a sumple text for test.",
            page=1,
            source="sanple.txt"
        )
    ]

    result = chunker.make_chunk(docs)

    assert isinstance(result, list)
    assert len(result) > 0 
    assert all(isinstance(chunk, Chunk) for chunk in result)

def test_make_chunk_generates_sequencial_chunk():

    chunker = TokenChunker()

    docs = [
        Document(
            text="これはテスト用サンプルです。\nThis is a sumple text for test.",
            page=1,
            source="sanple.txt"
        )
    ]

    result = chunker.make_chunk(docs)

    for i, chunk in enumerate(result):
        assert i == chunk.chunk_index


