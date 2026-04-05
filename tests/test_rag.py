"""Tests for GroceryBot RAG pipeline."""
import pytest
import json


def test_knowledge_base_loads():
    """Test that knowledge files are valid JSON."""
    with open("knowledge/produce_guide.json") as f:
        data = json.load(f)
    assert len(data) > 0
    assert "item" in data[0]


def test_faq_loads():
    """Test that FAQ file loads."""
    with open("knowledge/faq.json") as f:
        data = json.load(f)
    assert len(data) > 0
    assert "question" in data[0]
