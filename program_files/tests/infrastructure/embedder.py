# tests/infrastructure/embedding/test_embedder.py

import numpy
import pytest

from program_files.infrastructure.embedding.base import BaseEmbedder
from program_files.infrastructure.embedding.embedder import STEmbedder


@pytest.fixture(params=[
    STEmbedder,
])
def embedder(request) -> BaseEmbedder:
    return request.param()


def test_embed_interface(embedder: BaseEmbedder):
    """
    BaseEmbedderのインターフェース仕様を検証する。

    検証内容:
    - embed() が1次元ベクトルを返す
    - embed_batch() が2次元行列を返す
    - embed(text) と embed_batch([text])[0] が一致する
    """

    text = "hello world"

    # ===== embed() =====
    single = embedder.embed(text)

    assert isinstance(single, numpy.ndarray)
    assert single.ndim == 1
    assert single.size > 0

    # ===== embed_batch() =====
    batch = embedder.embed_batch([text])

    assert isinstance(batch, numpy.ndarray)
    assert batch.ndim == 2
    assert batch.shape[0] == 1

    # ===== 整合性確認 =====
    assert numpy.allclose(
        single,
        batch[0]
    )
