from sentence_transformers import SentenceTransformer
import numpy
from typing import cast

from program_files.infrastructure.embedding._types import BATCH_SIZE, MODEL_NAME
from program_files.infrastructure.embedding.base import BaseEmbedder
from program_files.app.registry.components_registry import ComponentsRegistry


@ComponentsRegistry.component(
    base=BaseEmbedder,
    name="st_embedder"
)
class STEmbedder(BaseEmbedder):


    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)


    def embed(self, text: str) -> numpy.ndarray:
        #shape: (D,)
        emb = self.embed_batch([text])

        return emb.squeeze(0)
    

    def embed_batch(self, texts: list[str]) -> numpy.ndarray:
        #shape: (N, D)

        embeddings = self.model.encode(
            texts,
            batch_size=BATCH_SIZE,
            normalize_embeddings=True
        ) 

        #castなしでは型エラー（誤作動）
        return cast(numpy.ndarray, embeddings)

                
