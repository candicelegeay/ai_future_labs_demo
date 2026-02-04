"""
SOVEREIGN EXECUTIVE AGENT - STREAMLIT DEMO
==========================================
Interactive demonstration of the 8-stage AI recovery workflow.
Showcases AI Futures Lab concepts in a visual, step-by-step format.
"""

import streamlit as st
import time
import json
from agent import SovereignExecutiveAgent

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Sovereign Executive Agent",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM STYLING
# ============================================================
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #1e3a5f, #2d5a87);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #666;
        margin-top: 0;
    }
    .stage-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
        border-left: 4px solid #2d5a87;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
    }
    .concept-badge {
        background: #2d5a87;
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .success-box {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
    }
    .alert-box {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeeba 100%);
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
    }
    .privacy-box {
        background: linear-gradient(135deg, #e7e9fd 0%, #d4d7f9 100%);
        border-left: 4px solid #6c63ff;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
    }
    .code-block {
        background: #1e1e1e;
        color: #d4d4d4;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Fira Code', monospace;
        font-size: 0.85rem;
        overflow-x: auto;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    .timeline-dot {
        width: 12px;
        height: 12px;
        background: #2d5a87;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR - CONFIGURATION
# ============================================================
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield.png", width=80)
    st.markdown("## ⚙️ Configuration")
    
    use_llm = st.checkbox("Use Local LLM (Llama 3.1)", value=False, 
                          help="Requires Ollama with llama3.1:8b model")
    
    animation_speed = st.slider("Animation Speed", 0.5, 3.0, 1.5, 0.5,
                                help="Delay between stages (seconds)")
    
    st.markdown("---")
    st.markdown("### 📚 AI Futures Lab Concepts")
    
    concepts = [
        ("🔲", "Edge AI", "Processing at the source"),
        ("📋", "Contextual AI", "Understanding the situation"),
        ("🔗", "Causal AI", "Cause-effect reasoning"),
        ("🧮", "True Reasoning", "Logical deduction"),
        ("🛡️", "Sovereign AI", "Data sovereignty"),
        ("🔒", "Privacy Preserving", "Anonymous queries"),
        ("🤖", "Agentic AI", "Autonomous action"),
        ("📚", "Continuous Learning", "Self-improvement"),
    ]
    
    for icon, name, desc in concepts:
        st.markdown(f"{icon} **{name}**")
        st.caption(desc)
    
    st.markdown("---")
    st.markdown("### 📊 Demo Statistics")
    if 'run_count' not in st.session_state:
        st.session_state.run_count = 0
    st.metric("Total Runs", st.session_state.run_count)

# ============================================================
# MAIN CONTENT
# ============================================================

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p class="main-header">🛡️ Sovereign Executive Agent</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">An 8-Stage Demonstration of Next-Generation AI Capabilities</p>', unsafe_allow_html=True)

with col2:
    st.markdown("")
    st.markdown("")
    if st.button("🔄 Reset Demo", use_container_width=True):
        st.session_state.clear()
        st.rerun()

st.markdown("---")

# ============================================================
# SCENARIO INTRODUCTION
# ============================================================
with st.expander("📖 THE SCENARIO", expanded=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 The Mission")
        st.markdown("""
        **Operation Sakura**
        - M&A signing ceremony
        - 6 months of negotiations
        - $2.4B semiconductor deal
        - Tokyo, 09:00 AM
        """)
    
    with col2:
        st.markdown("### ⚠️ The Crisis")
        st.markdown("""
        **23:00 - Charles de Gaulle Airport**
        - Flight AF276 CANCELLED
        - Weather conditions
        - CEO stranded in Paris
        - No direct Tokyo flights available
        """)
    
    with col3:
        st.markdown("### 🔒 The Constraints")
        st.markdown("""
        **Sovereign Requirements**
        - Identity must stay confidential
        - Mission details classified
        - No public cloud exposure
        - Japanese protocol: physical presence required
        """)

st.markdown("---")

# ============================================================
# MAIN DEMO EXECUTION
# ============================================================
incident_input = st.text_input(
    "📝 Incident Description",
    value="CEO Flight AF276 to Tokyo cancelled due to weather at 23:00",
    help="Modify the incident to test different scenarios"
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    run_button = st.button("🚀 LAUNCH SOVEREIGN RECOVERY PROTOCOL", 
                           type="primary", 
                           use_container_width=True)

if run_button:
    st.session_state.run_count = st.session_state.get('run_count', 0) + 1
    
    # Initialize agent
    with st.spinner("Initializing Sovereign Agent..."):
        try:
            agent = SovereignExecutiveAgent(use_llm=use_llm)
        except Exception as e:
            st.error(f"Error initializing agent: {e}")
            st.stop()
    
    # Progress tracking
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Run the agent
    status_text.text("🔄 Executing recovery protocol...")
    
    try:
        result = agent.run(incident_input)
    except Exception as e:
        st.error(f"Execution error: {e}")
        st.stop()
    
    # Display results stage by stage
    st.markdown("## 📊 Execution Timeline")
    
    stage_icons = {
        1: "📱", 2: "📋", 3: "🔗", 4: "🧮", 
        5: "🛡️", 6: "🤖", 7: "👤", 8: "📚"
    }
    
    stage_colors = {
        1: "#3498db", 2: "#9b59b6", 3: "#e74c3c", 4: "#f39c12",
        5: "#6c63ff", 6: "#27ae60", 7: "#16a085", 8: "#8e44ad"
    }
    
    for i, log in enumerate(result["stage_logs"]):
        progress_bar.progress((i + 1) / len(result["stage_logs"]))
        status_text.text(f"Stage {log['stage']}: {log['name']}")
        
        # Create expandable section for each stage
        with st.expander(
            f"{stage_icons.get(log['stage'], '📌')} STAGE {log['stage']}: {log['name']} — {log['timestamp']}", 
            expanded=(i < 3)  # First 3 stages expanded by default
        ):
            # Concept badge
            st.markdown(f"""
            <span class="concept-badge">💡 {log['concept']}</span>
            """, unsafe_allow_html=True)
            
            st.markdown("")
            
            # Actions display
            for action in log["actions"]:
                if action.strip():  # Skip empty lines
                    st.markdown(f"`{action}`")
            
            # Special content for certain stages
            if log['stage'] == 4 and 'llm_reasoning' in log:
                st.markdown("#### 🧠 LLM Reasoning Output")
                st.code(log['llm_reasoning'], language="text")
            
            if log['stage'] == 7 and 'executive_message' in log:
                st.markdown("#### 📨 Executive Notification")
                st.code(log['executive_message'], language="text")
            
            # Key insight
            st.markdown("---")
            st.info(f"💡 **Key Insight:** {log['key_insight']}")
        
        time.sleep(animation_speed)
    
    progress_bar.progress(1.0)
    status_text.text("✅ Recovery protocol complete!")
    
    # ============================================================
    # FINAL SUMMARY
    # ============================================================
    st.markdown("---")
    st.markdown("## ✅ MISSION RECOVERY COMPLETE")
    
    final = result.get("final_solution", {})
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Status", "SECURED", delta="SUCCESS")
    with col2:
        st.metric("ETA Tokyo", final.get("timeline", {}).get("tokyo_arrival", "08:15"))
    with col3:
        st.metric("Buffer Time", final.get("buffer_time", "20 min"))
    with col4:
        st.metric("Privacy", "PROTECTED", delta="SOVEREIGN")
    
    # Route visualization
    st.markdown("### 🗺️ Recovery Route")
    
    route_cols = st.columns(5)
    route_steps = [
        ("🛫", "Paris CDG", "01:20"),
        ("✈️", "Flight JL416", "12h 25m"),
        ("🛬", "Osaka KIX", "19:45"),
        ("🚄", "Nozomi 64", "2h 15m"),
        ("🏢", "Tokyo Venue", "08:40")
    ]
    
    for col, (icon, label, time_info) in zip(route_cols, route_steps):
        with col:
            st.markdown(f"""
            <div style="text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 8px;">
                <div style="font-size: 2rem;">{icon}</div>
                <div style="font-weight: bold; margin: 0.5rem 0;">{label}</div>
                <div style="color: #666; font-size: 0.9rem;">{time_info}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Technical summary
    with st.expander("🔧 Technical Summary", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Privacy Actions")
            for action in result.get("privacy_actions", []):
                st.json(action)
        
        with col2:
            st.markdown("#### Bookings Secured")
            for booking in result.get("bookings", []):
                st.json(booking)
    
    # Full JSON output
    with st.expander("📄 Full Execution Log (JSON)", expanded=False):
        st.json(result)

# ============================================================
# FOOTER - CONCEPT SUMMARY
# ============================================================
st.markdown("---")
st.markdown("### 🎓 AI Futures Lab - Concepts Demonstrated")

concept_cols = st.columns(4)

concepts_summary = [
    ("🏛️ Responsible AI", "Sovereign AI, Privacy Preserving", "Trust & confidentiality by design"),
    ("🔄 Systems Thinking", "Edge AI, Agentic AI", "Pervasive AI at scale"),
    ("🎯 Real-World Alignment", "Causal AI, True Reasoning", "Understanding physics & consequences"),
    ("📈 Continuous Improvement", "Continuous Learning", "Experience captured & applied"),
]

for col, (title, concepts, desc) in zip(concept_cols, concepts_summary):
    with col:
        st.markdown(f"**{title}**")
        st.caption(concepts)
        st.markdown(f"_{desc}_")

st.markdown("---")
st.caption("🛡️ Sovereign Executive Agent Demo | AI Futures Lab 2026")