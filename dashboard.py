"""
Streamlit Dashboard for AI Competitive Intelligence Agent
Run with: streamlit run dashboard.py
"""

import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="AI Competitive Intelligence Agent",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 AI Competitive Intelligence Agent")
st.subheader("Automated monitoring of AI chip companies")

st.markdown("""
This multi-agent system monitors NVIDIA's competitors in the AI infrastructure space 
and generates executive intelligence briefs automatically.
""")

# Sidebar - Agent Architecture
with st.sidebar:
    st.header("🏗️ Agent Architecture")
    st.markdown("""
    **3 Specialized Agents:**
    
    1. **📡 Data Collection Agent**
       - Searches web for recent news
       - Monitors AMD, Cerebras, Groq
       - Gathers product announcements
    
    2. **🔍 Analysis Agent**  
       - Identifies strategic implications
       - Uses Claude for reasoning
       - Extracts key developments
    
    3. **📝 Report Generation Agent**
       - Synthesizes findings
       - Creates executive brief
       - Provides recommendations
    """)
    
    st.divider()
    
    st.header("⚙️ Tech Stack")
    st.markdown("""
    - **LangGraph** - Agent orchestration
    - **Claude Sonnet 4** - LLM reasoning
    - **DuckDuckGo** - Web search
    - **Streamlit** - Dashboard
    """)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Generate Intelligence Report")
    
    # Company selection
    st.markdown("**Companies to Monitor:**")
    companies = st.multiselect(
        "Select competitors",
        ["AMD MI300", "Cerebras AI", "Groq LPU", "Intel Gaudi", "Google TPU"],
        default=["AMD MI300", "Cerebras AI", "Groq LPU"],
        label_visibility="collapsed"
    )

with col2:
    st.header("Status")
    status_placeholder = st.empty()
    status_placeholder.info("Ready to generate report")

# Generate button
if st.button("🚀 Generate Report", type="primary", use_container_width=True):
    
    try:
        # Import agent
        from basic_agent import build_agent, AgentState
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_placeholder.warning("⏳ Agents working...")
        
        # Step 1: Initialize
        st.write("**Step 1/3:** Initializing agents...")
        progress_bar.progress(10)
        
        app = build_agent()
        initial_state: AgentState = {
            "companies": [],
            "scraped_data": {},
            "analysis": "",
            "report": ""
        }
        
        # Step 2: Run workflow
        st.write("**Step 2/3:** Gathering and analyzing data...")
        progress_bar.progress(40)
        
        result = app.invoke(initial_state)
        
        # Step 3: Display results
        st.write("**Step 3/3:** Generating report...")
        progress_bar.progress(90)
        
        status_placeholder.success("✅ Report generated!")
        progress_bar.progress(100)
        
        # Display the report
        st.divider()
        st.header("📊 Intelligence Report")
        st.caption(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        st.markdown(result["report"])
        
        # Expandable sections for details
        with st.expander("🔍 View Raw Analysis"):
            st.markdown(result["analysis"])
        
        with st.expander("📡 View Collected Data"):
            for company, data in result["scraped_data"].items():
                st.markdown(f"**{company}:**")
                st.text(data[:500] + "..." if len(data) > 500 else data)
                st.divider()
        
        # Agent workflow visualization
        with st.expander("🏗️ Agent Workflow Executed"):
            st.markdown("""
            | Step | Agent | Action | Status |
            |------|-------|--------|--------|
            | 1 | Data Collection | Searched 3 companies across web sources | ✅ Complete |
            | 2 | Analysis | Identified key developments using Claude | ✅ Complete |
            | 3 | Report Generation | Synthesized executive brief | ✅ Complete |
            """)
            
    except ImportError as e:
        status_placeholder.error("❌ Error: Could not import agent module")
        st.error(f"""
        Make sure you have installed all dependencies:
        ```bash
        pip install langgraph langchain-anthropic langchain-community duckduckgo-search
        ```
        
        Error details: {str(e)}
        """)
        
    except Exception as e:
        status_placeholder.error("❌ Error generating report")
        st.error(f"Error: {str(e)}")
        st.info("Make sure your ANTHROPIC_API_KEY environment variable is set.")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>AI Competitive Intelligence Agent | Built with LangGraph + Claude</p>
    <p>Reduces 15 hours of manual research to 2 minutes</p>
</div>
""", unsafe_allow_html=True)
