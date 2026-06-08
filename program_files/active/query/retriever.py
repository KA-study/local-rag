#知識検索
'''
Retrieverのフロー


str query

embedding

vector検索

RetrievedChunkを返す
'''
import numpy

from program_files.active._types import Message
from program_files.infrastructure.embedding.embedder import STEmbedder
from program_files.infrastructure.vector_store.chroma_store import ChromaVectorStore
from program_files.shared.schemas import RetrievedChunk


class Retriever:
    
    def __init__(self):
        self._embedder = STEmbedder()
        self._vector_store = ChromaVectorStore()

    def retrieve(
        self,
        message: Message
    ) -> list[RetrievedChunk]:
        query = message.content

        #embedding
        query_embedding: numpy.ndarray = self._embedder.embed(query)

        #vector検索
        l_query_embedding: list[float] = query_embedding.tolist()
        retrieved_chunk: list[RetrievedChunk] = self._vector_store.search(l_query_embedding, top_k=5)

        return retrieved_chunk


