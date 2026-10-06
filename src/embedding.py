from operator import index

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class Retriever:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        # 1. Load a pretrained Sentence Transformer model
        self.model = SentenceTransformer(model_name)
        self.index = None

    def  embedding_similarity(self, sentences):

        # The sentences to encode
        # sentences = [
        #     "The weather is lovely today.",
        #     "It's so sunny outside!",
        #     "He drove to the stadium.",
        # ]

        # 2. Calculate embeddings by calling model.encode()
        embeddings = self.model.encode(sentences)
        # [3, 384]

        # 3. Calculate the embedding similarities
        similarities = self.model.similarity(embeddings, embeddings)
        # tensor([[1.0000, 0.6660, 0.1046],
        #         [0.6660, 1.0000, 0.1411],
        #         [0.1046, 0.1411, 1.0000]])
        print(similarities)

        # Get embedding dimension
        dimension = embeddings.shape[1]

        # Create a flat index using L2 distance
        self.index = faiss.IndexFlatL2(dimension)

        # Add embeddings to the index
        self.index.add(np.array(embeddings))