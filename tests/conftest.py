"""Test configuration for Interview Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "interview-agent", "category": "Human Resources"}
