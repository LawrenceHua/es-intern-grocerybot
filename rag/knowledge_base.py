"""
Knowledge Base Loader

TODO: Load produce knowledge from JSON files and index it in ChromaDB.

ChromaDB docs: https://docs.trychroma.com/getting-started
It's a vector database that runs locally — no server needed!
"""

import json
import chromadb


class KnowledgeBase:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = None

    def load(self, knowledge_dir: str = "knowledge"):
        """
        TODO: Load all knowledge files and add them to ChromaDB.

        Steps:
        1. Read produce_guide.json and faq.json
        2. Create a ChromaDB collection
        3. Add each knowledge entry as a document

        ChromaDB will automatically create embeddings!
        """
        # YOUR CODE HERE
        pass

    def search(self, query: str, n_results: int = 3) -> list[dict]:
        """
        TODO: Search the knowledge base for relevant info.

        Args:
            query: User's question
            n_results: Number of results to return

        Returns:
            List of relevant knowledge entries
        """
        # YOUR CODE HERE
        return []
