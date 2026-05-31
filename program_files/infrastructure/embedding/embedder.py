from sentence_transformers import SentenceTransformer

from infrastructure.embedding._types import BATCH_SIZE, MODEL_NAME
from infrastructure.embedding.base import BaseEmbedder
from shared.schemas import Chunk, EmbeddedChunk

class STEmbedder(BaseEmbedder):


    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)


    def embed(self, chunk: Chunk) -> EmbeddedChunk:
        return self.embed_batch([chunk])[0] 
    

    def embed_batch(self, chunks: list[Chunk]) -> list[EmbeddedChunk]:
        
        embedded_chunks = []
        texts = [
            chunk.text for chunk in chunks
        ]

        embeddings = self.model.encode(
            texts,
            batch_size=BATCH_SIZE,
            normalize_embeddings=True
        ) 

        for chunk, embedding in zip(
            chunks,
            embeddings
        ):

            embedded_chunks.append(
                EmbeddedChunk(
                    chunk=chunk,
                    embedding=embedding.tolist()
                )
            )

        return embedded_chunks
                
