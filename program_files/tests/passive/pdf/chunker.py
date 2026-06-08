import pytest

from passive.pdf.base import PDFChunkerBase
from passive.pdf.chunker import TokenChunker
from shared.schemas import Document, Chunk


@pytest.mark.parametrize(
    "chunker",
    [
        TokenChunker,
    ]
)
def test_make_chunk(chunker: PDFChunkerBase):

    docs = [
        Document(
            text="あ" * 1000,
            page=1,
            source="sample.pdf"
        )
    ]

    result = chunker.make_chunk(docs)

    assert isinstance(result, list)
    assert len(result) > 0

    for chunk in result:
        assert isinstance(chunk, Chunk)
