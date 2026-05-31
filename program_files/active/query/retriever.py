#知識検索
'''
Retrieverのフロー


str query

embedding

vector検索

RetrievedChunkを返す
'''

from infrastructure.embedding.embedder import STEmbedder
from shared.schemas import RetrievedChunk


class Retriever:
    
    def __init__(self):
        self._embedder = STEmbedder()

    def retrieve(
        self,
        query: str
    ) -> list[RetrievedChunk]:

        query_embedding = self._embedder.embed(query)
