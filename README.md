# Interview Agent

[![CI](https://github.com/kogunlowo123/interview-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/interview-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Human Resources | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Interview management agent that generates structured interview guides, creates role-specific question banks, evaluates interviewer feedback, detects assessment inconsistencies, and produces hiring committee summaries.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_interview_guide` | Generate a structured interview guide for a role and interview stage |
| `create_question_bank` | Create role-specific behavioral and technical questions |
| `evaluate_feedback` | Evaluate and normalize interviewer feedback for consistency |
| `detect_bias_signals` | Detect potential bias signals in interviewer feedback language |
| `generate_hiring_summary` | Generate a hiring committee summary from all interview feedback |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/interviews/guide` | Generate interview guide |
| `POST` | `/api/v1/interviews/questions` | Create question bank |
| `POST` | `/api/v1/interviews/feedback` | Evaluate feedback |
| `POST` | `/api/v1/interviews/bias-check` | Detect bias signals |
| `POST` | `/api/v1/interviews/summary` | Generate hiring summary |

## Features

- Interview Guide Generation
- Question Bank
- Feedback Evaluation
- Consistency Detection
- Hiring Summary

## Integrations

- Greenhouse
- Lever
- Brighthire
- Metaview
- Coderpad

## Architecture

```
interview-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── interview_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**ATS + Interview Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
