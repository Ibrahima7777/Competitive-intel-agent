"""
AI Competitive Intelligence Agent
Multi-agent system for automated competitor monitoring in the AI infrastructure space.
"""

from langgraph.graph import StateGraph, END
from langchain_anthropic import ChatAnthropic
from langchain_community.tools import DuckDuckGoSearchResults
from typing import TypedDict, List, Dict
from datetime import datetime
import json

# ============ State Definition ============
class AgentState(TypedDict):
    companies: List[str]
    scraped_data: Dict[str, str]
    analysis: str
    report: str

# ============ Initialize LLM ============
llm = ChatAnthropic(model="claude-sonnet-4-20250514", temperature=0)

# ============ Agent Nodes ============

def gather_data(state: AgentState) -> AgentState:
    """
    Data Collection Agent
    Searches the web for recent news about AI chip companies.
    """
    search = DuckDuckGoSearchResults(max_results=5)
    
    companies = ["AMD MI300", "Cerebras AI", "Groq LPU"]
    scraped = {}
    
    for company in companies:
        try:
            query = f"{company} announcement news 2025"
            results = search.invoke(query)
            scraped[company] = results
            print(f"✓ Gathered data for {company}")
        except Exception as e:
            scraped[company] = f"Error fetching data: {str(e)}"
            print(f"✗ Failed to gather data for {company}: {e}")
    
    return {
        **state,
        "companies": companies,
        "scraped_data": scraped
    }


def analyze_data(state: AgentState) -> AgentState:
    """
    Analysis Agent
    Uses Claude to identify strategic implications from gathered data.
    """
    data_str = "\n\n".join([
        f"=== {company} ===\n{data}" 
        for company, data in state["scraped_data"].items()
    ])
    
    prompt = f"""You are a competitive intelligence analyst specializing in the AI chip market.
    
Analyze this data about NVIDIA's competitors and identify:

1. **Key Product Announcements**: Any new chips, models, or significant updates
2. **Strategic Moves**: Partnerships, pricing changes, market positioning
3. **Performance Claims**: Any benchmarks or performance comparisons mentioned
4. **Implications for NVIDIA**: How these developments affect NVIDIA's competitive position

Data collected:
{data_str}

Provide a structured analysis. Be specific about what you found and what it means strategically."""

    print("⚙ Analysis Agent processing...")
    response = llm.invoke(prompt)
    
    return {
        **state,
        "analysis": response.content
    }


def generate_report(state: AgentState) -> AgentState:
    """
    Report Generation Agent
    Synthesizes analysis into an executive brief format.
    """
    prompt = f"""Based on this competitive analysis, create a concise executive intelligence brief.

Analysis:
{state["analysis"]}

Format the report exactly as follows:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WEEKLY COMPETITIVE INTELLIGENCE BRIEF
AI Infrastructure Market
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXECUTIVE SUMMARY
• [3 key takeaways, one line each]

COMPETITOR UPDATES

AMD
• [Key development]
• [Strategic implication]

Cerebras  
• [Key development]
• [Strategic implication]

Groq
• [Key development]
• [Strategic implication]

STRATEGIC IMPLICATIONS FOR NVIDIA
• [2-3 bullet points on what this means for NVIDIA's strategy]

RECOMMENDED ACTIONS
• [2-3 specific, actionable recommendations]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Keep it concise and actionable. Focus on insights, not raw data."""

    print("📝 Report Agent generating brief...")
    response = llm.invoke(prompt)
    
    return {
        **state,
        "report": response.content
    }


# ============ Build the Agent Graph ============

def build_agent():
    """Constructs the LangGraph workflow."""
    workflow = StateGraph(AgentState)
    
    # Add nodes (agents)
    workflow.add_node("gather", gather_data)
    workflow.add_node("analyze", analyze_data)
    workflow.add_node("report", generate_report)
    
    # Define the flow
    workflow.set_entry_point("gather")
    workflow.add_edge("gather", "analyze")
    workflow.add_edge("analyze", "report")
    workflow.add_edge("report", END)
    
    return workflow.compile()


# ============ Main Execution ============

def run_agent():
    """Runs the competitive intelligence agent and returns the report."""
    print("\n" + "="*60)
    print("🤖 AI COMPETITIVE INTELLIGENCE AGENT")
    print("="*60 + "\n")
    
    print("Starting multi-agent workflow...\n")
    
    # Build and run the agent
    app = build_agent()
    
    initial_state: AgentState = {
        "companies": [],
        "scraped_data": {},
        "analysis": "",
        "report": ""
    }
    
    result = app.invoke(initial_state)
    
    # Output the report
    print("\n" + "="*60)
    print(f"📊 REPORT GENERATED: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*60 + "\n")
    print(result["report"])
    
    return result


if __name__ == "__main__":
    run_agent()
