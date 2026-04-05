"""
RAG Retriever

TODO: Combine knowledge base search with smart retrieval logic.
"""

from rag.knowledge_base import KnowledgeBase


class Retriever:
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb

    def retrieve(self, query: str) -> str:
        """
        TODO: Retrieve relevant context for the LLM.

        Steps:
        1. Search knowledge base
        2. Format results into a context string
        3. Return the context
        """
        results = self.kb.search(query)
        # Format results into readable context
        # YOUR CODE HERE
        return "No knowledge loaded yet."
