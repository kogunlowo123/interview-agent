"""Interview Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_interview_guide():
    """Test Generate a structured interview guide for a role and interview stage."""
    tools = AgentTools()
    result = await tools.generate_interview_guide(job_id="test", interview_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_create_question_bank():
    """Test Create role-specific behavioral and technical questions."""
    tools = AgentTools()
    result = await tools.create_question_bank(role="test", competencies="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_evaluate_feedback():
    """Test Evaluate and normalize interviewer feedback for consistency."""
    tools = AgentTools()
    result = await tools.evaluate_feedback(candidate_id="test", feedback_entries="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_bias_signals():
    """Test Detect potential bias signals in interviewer feedback language."""
    tools = AgentTools()
    result = await tools.detect_bias_signals(feedback_text="test", candidate_demographics="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.interview_agent_agent import InterviewAgentAgent
    agent = InterviewAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
