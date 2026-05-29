from passive.pdf.chunker import TokenChunker
from shared.schemas import Document, Chunk


def create_sample_docs() -> list[Document]:

    return[
        Document(
            text="これはサンプルテキストです。\nThis is a sample text.",
            page=1,
            source="sample.pdf"
        ),
        Document(
            text="これはサンプルテキスト２です。\nThis is a sample text2.",
            page=2,
            source="sample2.pdf"
        )
    ]


def test_make_chunk_returns_chunk_list():

    chunker = TokenChunker()

    docs = create_sample_docs()

    result = chunker.make_chunk(docs)

    assert isinstance(result, list)
    assert len(result) > 0 
    assert all(isinstance(chunk, Chunk) for chunk in result)


def test_make_chunk_generates_sequencial_chunk():

    chunker = TokenChunker()

    docs = create_sample_docs() 

    result = chunker.make_chunk(docs)

    for i, chunk in enumerate(result):
        assert i == chunk.chunk_index


