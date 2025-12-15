# 🤖 AI Competitive Intelligence Agent

A multi-agent system for automated competitor monitoring in the AI infrastructure market. Built with LangGraph and Claude to demonstrate enterprise AI agent orchestration.

## Overview

This system uses **3 specialized AI agents** working together to automate competitive intelligence gathering:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Data Collection│────▶│    Analysis     │────▶│     Report      │
│     Agent       │     │     Agent       │     │   Generation    │
│                 │     │                 │     │     Agent       │
│ • Web search    │     │ • Strategic     │     │ • Executive     │
│ • News monitor  │     │   implications  │     │   summary       │
│ • Multi-source  │     │ • Claude LLM    │     │ • Action items  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## Features

- **Multi-agent orchestration** via LangGraph with state management
- **Automated web search** for real-time competitive data
- **LLM-powered analysis** using Claude Sonnet 4 for strategic reasoning
- **Executive brief generation** with actionable recommendations
- **Interactive dashboard** built with Streamlit

## Tech Stack

| Component | Technology |
|-----------|------------|
| Agent Orchestration | LangGraph |
| LLM Reasoning | Claude Sonnet 4 (Anthropic) |
| Web Search | DuckDuckGo Search |
| Dashboard | Streamlit |
| Language | Python 3.10+ |

## Quick Start

### 1. Clone and Install

```bash
git clone https://github.com/Ibrahima7777/competitive-intel-agent.git
cd competitive-intel-agent
pip install -r requirements.txt
```

### 2. Set API Key

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

### 3. Run

**Command Line:**
```bash
python basic_agent.py
```

**Dashboard:**
```bash
streamlit run dashboard.py
```

## Sample Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WEEKLY COMPETITIVE INTELLIGENCE BRIEF
AI Infrastructure Market
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTIVE SUMMARY
• AMD MI300X gaining traction in enterprise AI inference workloads
• Groq demonstrating 10x inference speed improvements for LLM serving
• Cerebras expanding cloud partnerships for large model training

STRATEGIC IMPLICATIONS FOR NVIDIA
• Increased competition in inference-optimized hardware segment
• Need to emphasize software ecosystem advantages (CUDA, TensorRT)
• Enterprise customers evaluating multi-vendor strategies

RECOMMENDED ACTIONS
• Accelerate Blackwell B200 deployment timelines
• Strengthen inference performance benchmarks
• Expand enterprise partnership programs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Architecture Deep Dive

### Agent State Management

The system uses LangGraph's `StateGraph` for managing state across agents:

```python
class AgentState(TypedDict):
    companies: List[str]      # Target companies to monitor
    scraped_data: Dict        # Raw data from web search
    analysis: str             # Strategic analysis output
    report: str               # Final executive brief
```

### Agent Workflow

1. **Data Collection Agent**: Searches multiple web sources for recent news about AMD, Cerebras, and Groq
2. **Analysis Agent**: Uses Claude to extract strategic implications and identify key developments
3. **Report Generation Agent**: Synthesizes findings into actionable executive brief

### Key Design Decisions

- **LangGraph over CrewAI**: Chose LangGraph for finer control over agent orchestration and state management
- **Claude Sonnet 4**: Optimal balance of reasoning capability and cost for analysis tasks
- **DuckDuckGo Search**: No API key required, suitable for demonstration purposes

## Metrics

| Metric | Value |
|--------|-------|
| Data sources processed | 15+ per run |
| Manual research time saved | ~15 hours → 2 minutes |
| Agent coordination steps | 3 |
| Average report generation time | 30-45 seconds |

## Future Enhancements

- [ ] SEC filing monitoring for public companies
- [ ] Historical change detection and trend analysis
- [ ] Scheduled weekly email delivery
- [ ] Expand to 10+ competitor companies
- [ ] Add sentiment analysis agent
- [ ] Integrate with Slack for notifications

## Project Structure

```
competitive-intel-agent/
├── basic_agent.py      # Core agent implementation
├── dashboard.py        # Streamlit web interface
├── requirements.txt    # Python dependencies
└── README.md          # Documentation
```

## License

MIT

---

Built to demonstrate practical enterprise AI agent applications for competitive intelligence workflows.
