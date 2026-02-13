from __future__ import annotations
from loguru import logger

from typing import TYPE_CHECKING
# if TYPE_CHECKING:

from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(
    model='nomic-embed-text:v1.5',
)

client = QdrantClient(path="./t_qdrant")


# client.create_collection(
#     collection_name="demo",
#     vectors_config=VectorParams(
#         size=768,
#         distance=Distance.COSINE,
#     )
# )

client.close()

