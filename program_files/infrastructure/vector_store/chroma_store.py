import chromadb
from typing import Any

from infrastructure.vector_store._types import PERSIST_DIRECTORY, COLLECTION_NAME
from infrastructure.vector_store.base import VectorStore
from shared.schemas import Chunk, EmbeddedChunk, RetrievedChunk

class ChromaVectorStore(VectorStore):
    
    def __init__(
            self,
    ) -> None:

        self._client = chromadb.PersistentClient(
            path = PERSIST_DIRECTORY
        )

        self._collection = self._client.get_or_create_collection(
            name=COLLECTION_NAME
        )
        

    def add(self, chunks: list[EmbeddedChunk]) -> None:
        
        if not chunks:
            return

        data = self._to_chroma_format(chunks)

        self._collection.add(**data)


    def count(self) -> int:
        return self._collection.count()


    def delete(self, ids: list[str]) -> None:

        if not ids:
            return

        self._collection.delete(ids=ids)




















