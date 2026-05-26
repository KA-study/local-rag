from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List

from pdf.base import PDFChunkerBase
from schemas import Document, Chunk


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

    def make_chunk(self, docs: List[Document]) -> List[Chunk]:

        results = []

        for doc in docs:
            split_texts = self._splitter.split_text(doc.text)

            for i, text in enumerate(split_texts):
                results.append(
                    Chunk(
                        text=text,
                        source=doc.source,
                        chunk_index=i,
                    )
                )

        return results

