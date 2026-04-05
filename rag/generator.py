"""
LLM Response Generator

TODO: Use Claude or OpenAI to generate responses based on retrieved context.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Generator:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY") or os.getenv("OPENAI_API_KEY")

    def generate(self, question: str, context: str, history: list = None) -> str:
        """
        TODO: Generate a response using the LLM.

        Args:
            question: User's question
            context: Retrieved knowledge base context
            history: Previous conversation messages

        Returns:
            str: The chatbot's response
        """
        # YOUR CODE HERE
        # Hint: Build a system prompt like:
        # "You are GroceryBot, a helpful assistant for grocery and produce questions.
        #  Use the following knowledge to answer: {context}
        #  If you don't know, say so honestly."
        return "Generator not implemented yet."
