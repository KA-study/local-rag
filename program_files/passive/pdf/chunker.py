from langchain_text_splitters import RecursiveCharacterTextSplitter

from pdf.base import PDFChunkerBase
from shared.schemas import Document, Chunk


class TokenChunker(PDFChunkerBase):

    def __init__(self):
        self._splitter = RecursiveCharacterTextSplitter (
            separators=[
                "\n\n",
                "\n",
                "。",
                "、",
                "",
            ],
            chunk_size=500,
            chunk_overlap=50,
        )

    def make_chunk(self, docs: list[Document]) -> list[Chunk]:

        chunks = []

        for doc in docs:
            split_texts = self._splitter.split_text(doc.text)

            for i, s_text in enumerate(split_texts):
                chunks.append(
                    Chunk(
                        text=s_text,
                        page=doc.page,
                        source=doc.source,
                        chunk_index=i,
                    )
                )

        return chunks

