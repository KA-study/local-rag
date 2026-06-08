import chromadb
from typing import Any

from program_files.infrastructure.vector_store._types import PERSIST_DIRECTORY, COLLECTION_NAME
from program_files.infrastructure.vector_store.base import VectorStore
from program_files.shared.schemas import Chunk, EmbeddedChunk, RetrievedChunk

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


    def _to_chroma_format(self, chunks: list[EmbeddedChunk]) -> dict:

        #この四つのパラメータはchromedbによって定められている
        texts: list[str] = []
        embeddings: list[list[float]] = []
        metadatas: list[dict[str, Any]] = []
        ids: list[str] = []

        for chunk in chunks:

            texts.append(chunk.chunk.text)

            embeddings.append(chunk.embedding)

            metadatas.append({
                "page": chunk.chunk.page, 
                "source": chunk.chunk.source,
                "index": chunk.chunk.chunk_index
            })

            ids.append(
                f"{chunk.chunk.source}_{chunk.chunk.page}_{chunk.chunk.chunk_index}"
            )

        return {
            "documents": texts,
            "embeddings": embeddings,
            "metadatas": metadatas,
            "ids": ids
        }


    def search(
        self,
        query_embedding: list[float],
        top_k: int = 5
    ) -> list[RetrievedChunk]:

        result = self._collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        if not (
            result["documents"] and
            result["metadatas"] and
            result["distances"]
        ):
            raise ValueError("some data in chromedb was racked.")

        #batchではなく、単一のqueryであるから、[0]指定
        #result["documents"] = [[...],] という構造
        texts = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]

        retrieved_chunks: list[RetrievedChunk] = []

        for text, metadata, distance in zip(
            texts,
            metadatas,
            distances
        ):

            if not isinstance(metadata["page"],int):
                raise ValueError("Invalid object type.")
            if not isinstance(metadata["source"],str):
                raise ValueError("Invalid object type.")
            if not isinstance(metadata["index"],int):
                raise ValueError("Invalid object type.")

            chunk = Chunk(
                text=text,
                page=metadata["page"],
                source=metadata["source"],
                chunk_index=metadata["index"]
            )

            retrieved_chunk = RetrievedChunk(
                chunk=chunk,
                distance=distance
            )

            retrieved_chunks.append(retrieved_chunk)

        return retrieved_chunks


    def count(self) -> int:
        return self._collection.count()


    def delete(self, ids: list[str]) -> None:

        if not ids:
            return

        self._collection.delete(ids=ids)




















