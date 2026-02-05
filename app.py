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
    .concept-badge {
        background: #2d5a87;
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
    }

    /* ---- incoming notification banner ---- */
    @keyframes slideDown {
        0%   { transform: translateY(-100%); opacity: 0; }
        100% { transform: translateY(0);     opacity: 1; }
    }
    .notif-banner {
        animation: slideDown 0.5s ease-out;
        background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
        color: white;
        padding: 1.2rem 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(220,53,69,0.4);
    }
    .notif-banner h3 { margin: 0 0 0.4rem 0; color: white; }
    .notif-banner p  { margin: 0; opacity: 0.95; }

    /* ---- stage card (rendered after completion) ---- */
    @keyframes fadeSlideIn {
        0%   { transform: translateY(12px); opacity: 0; }
        100% { transform: translateY(0);    opacity: 1; }
    }
    .stage-card {
        animation: fadeSlideIn 0.4s ease-out;
        border-left: 4px solid var(--accent, #2d5a87);
        background: #f8f9fb;
        padding: 1rem 1.2rem;
        border-radius: 0 10px 10px 0;
        margin-bottom: 0.8rem;
    }
    .stage-card .stage-title {
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 0.3rem;
    }
    .stage-card code {
        display: block;
        font-size: 0.84rem;
        line-height: 1.6;
    }
    .stage-card .insight {
        margin-top: 0.6rem;
        padding: 0.5rem 0.8rem;
        background: #e8f0fe;
        border-radius: 6px;
        font-size: 0.88rem;
    }

    /* ---- final summary section ---- */
    @keyframes popIn {
        0%   { transform: scale(0.92); opacity: 0; }
        100% { transform: scale(1);    opacity: 1; }
    }
    .final-summary { animation: popIn 0.5s ease-out; }

    .route-step {
        text-align: center;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
    }
    .route-step .icon  { font-size: 2rem; }
    .route-step .label { font-weight: bold; margin: 0.5rem 0; }
    .route-step .time  { color: #666; font-size: 0.9rem; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR - CONFIGURATION  (concepts list removed)
# ============================================================
with st.sidebar:
    st.markdown("## ⚙️ Configuration")

    use_llm = st.checkbox("Use Local LLM (Llama 3.1)", value=False,
                          help="Requires Ollama with llama3.1:8b model")

    animation_speed = st.slider("Animation Speed", 0.5, 3.0, 1.5, 0.5,
                                help="Delay between stages (seconds)")

    st.markdown("---")
    st.markdown("### 📊 Demo Statistics")
    if "run_count" not in st.session_state:
        st.session_state.run_count = 0
    st.metric("Total Runs", st.session_state.run_count)

# ============================================================
# MAIN HEADER
# ============================================================
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p class="main-header">🛡️ Sovereign Executive Agent</p>',
                unsafe_allow_html=True)
    st.markdown('<p class="sub-header">'
                'An 8-Stage Demonstration of Next-Generation AI Capabilities'
                '</p>', unsafe_allow_html=True)
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
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### 🎯 The Mission")
        st.markdown("""
        **Operation Sakura**
        - M&A signing ceremony
        - 6 months of negotiations
        - $2.4B semiconductor deal
        - Tokyo, 09:00 AM
        """)
    with c2:
        st.markdown("### ⚠️ The Crisis")
        st.markdown("""
        **23:00 — Charles de Gaulle Airport**
        - Flight AF276 CANCELLED
        - Weather conditions
        - CEO stranded in Paris
        - No direct Tokyo flights available
        """)
    with c3:
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
# LAUNCH AREA
# ============================================================
incident_input = st.text_input(
    "📝 Incident Description",
    value="CEO Flight AF276 to Tokyo cancelled due to weather at 23:00",
    help="Modify the incident to test different scenarios"
)

col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    run_button = st.button("🚀 LAUNCH SOVEREIGN RECOVERY PROTOCOL",
                           type="primary",
                           use_container_width=True)

# ============================================================
# DEMO EXECUTION  —  sequential, reveal-one-at-a-time
# ============================================================
if run_button:
    st.session_state.run_count = st.session_state.get("run_count", 0) + 1

    # ----------------------------------------------------------
    # 0. Initialize agent (hidden spinner)
    # ----------------------------------------------------------
    with st.spinner("Initializing Sovereign Agent..."):
        try:
            agent = SovereignExecutiveAgent(use_llm=use_llm)
        except Exception as e:
            st.error(f"Error initializing agent: {e}")
            st.stop()

    # ----------------------------------------------------------
    # 1. NOTIFICATION POP-IN  🔔
    # ----------------------------------------------------------
    notif_slot = st.empty()
    notif_slot.markdown("""
    <div class="notif-banner">
        <h3>🔔 &nbsp;INCOMING ALERT — Secure Executive Device</h3>
        <p>
            <strong>23:00</strong> &nbsp;|&nbsp;
            Flight AF276 Paris → Tokyo &nbsp;|&nbsp;
            <strong>CANCELLED</strong> — severe weather
        </p>
        <p style="margin-top:0.5rem;font-size:0.85rem;opacity:0.85;">
            ⚡ Edge AI intercepted on local device &nbsp;·&nbsp;
            No data sent to cloud
        </p>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(animation_speed + 0.5)  # let the user read the alert

    # ----------------------------------------------------------
    # 2. Run the full agent graph
    # ----------------------------------------------------------
    try:
        result = agent.run(incident_input)
    except Exception as e:
        st.error(f"Execution error: {e}")
        st.stop()

    # ----------------------------------------------------------
    # 3. Progress bar + status line
    # ----------------------------------------------------------
    st.markdown("## 📊 Execution Timeline")
    progress_bar = st.progress(0)
    status_text  = st.empty()

    stage_icons = {
        1: "📱", 2: "📋", 3: "🔗", 4: "🧮",
        5: "🛡️", 6: "🤖", 7: "👤", 8: "📚"
    }
    stage_accents = {
        1: "#3498db", 2: "#9b59b6", 3: "#e74c3c", 4: "#f39c12",
        5: "#6c63ff", 6: "#27ae60", 7: "#16a085", 8: "#8e44ad"
    }

    total = len(result["stage_logs"])

    # Pre-allocate empty slots — nothing is visible yet
    stage_slots = [st.empty() for _ in range(total)]

    # Placeholder for everything that comes AFTER the stages
    final_slot = st.empty()

    # ----------------------------------------------------------
    # 4. Reveal stages one-by-one
    # ----------------------------------------------------------
    for i, log in enumerate(result["stage_logs"]):
        progress_bar.progress((i + 1) / total)
        status_text.text(f"⏳  Stage {log['stage']}/{total}: {log['name']}")

        icon   = stage_icons.get(log["stage"], "📌")
        accent = stage_accents.get(log["stage"], "#2d5a87")

        # Build action lines as individual <div> rows (no <pre> to break)
        def _esc(txt):
            return txt.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

        action_html = "".join(
            f'<div style="font-family:monospace;font-size:0.84rem;'
            f'line-height:1.6;white-space:pre-wrap">{_esc(a)}</div>'
            for a in log["actions"] if a.strip()
        )

        # Optional extra blocks
        extra_html = ""
        if log["stage"] == 4 and "llm_reasoning" in log:
            escaped = _esc(log["llm_reasoning"])
            extra_html += (
                '<details style="margin-top:0.6rem">'
                '<summary><strong>🧠 LLM Reasoning Output</strong></summary>'
                '<div style="background:#1e1e1e;color:#d4d4d4;padding:0.8rem;'
                'border-radius:6px;font-family:monospace;font-size:0.82rem;'
                f'overflow-x:auto;margin-top:0.4rem;white-space:pre-wrap">{escaped}</div>'
                '</details>'
            )

        if log["stage"] == 7 and "executive_message" in log:
            escaped = _esc(log["executive_message"])
            extra_html += (
                '<details open style="margin-top:0.6rem">'
                '<summary><strong>📨 Executive Notification</strong></summary>'
                '<div style="background:#1e1e1e;color:#d4d4d4;padding:0.8rem;'
                'border-radius:6px;font-family:monospace;font-size:0.82rem;'
                f'overflow-x:auto;margin-top:0.4rem;white-space:pre-wrap">{escaped}</div>'
                '</details>'
            )

        # Assemble the complete card — no <pre> tags, only <div>s
        card_html = (
            f'<div class="stage-card" style="--accent:{accent}">'
            f'  <div class="stage-title">'
            f'    {icon} STAGE {log["stage"]}: {_esc(log["name"])}'
            f'    <span style="float:right;font-size:0.82rem;color:#888">'
            f'      {_esc(log["timestamp"])}'
            f'    </span>'
            f'  </div>'
            f'  <span class="concept-badge">💡 {_esc(log["concept"])}</span>'
            f'  <div style="margin-top:0.6rem">{action_html}</div>'
            f'  {extra_html}'
            f'  <div class="insight">💡 <em>{_esc(log["key_insight"])}</em></div>'
            f'</div>'
        )

        # Render into the pre-allocated slot → appears with animation
        stage_slots[i].markdown(card_html, unsafe_allow_html=True)

        time.sleep(animation_speed)

    # ----------------------------------------------------------
    # 5. Clear notification banner & finalise progress
    # ----------------------------------------------------------
    notif_slot.empty()
    progress_bar.progress(1.0)
    status_text.text("✅ Recovery protocol complete!")

    # ----------------------------------------------------------
    # 6. FINAL SUMMARY  (rendered only after all stages)
    # ----------------------------------------------------------
    with final_slot.container():
        st.markdown("---")
        st.markdown('<div class="final-summary">', unsafe_allow_html=True)
        st.markdown("## ✅ MISSION RECOVERY COMPLETE")

        final = result.get("final_solution", {})

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Status",      "SECURED",   delta="SUCCESS")
        m2.metric("ETA Tokyo",
                  final.get("timeline", {}).get("tokyo_arrival", "08:15"))
        m3.metric("Buffer Time", final.get("buffer_time", "20 min"))
        m4.metric("Privacy",     "PROTECTED", delta="SOVEREIGN")

        # Route visualisation
        st.markdown("### 🗺️ Recovery Route")
        route_cols = st.columns(5)
        route_steps = [
            ("🛫", "Paris CDG",    "01:20"),
            ("✈️", "Flight JL416", "12h 25m"),
            ("🛬", "Osaka KIX",    "19:45"),
            ("🚄", "Nozomi 64",    "2h 15m"),
            ("🏢", "Tokyo Venue",  "08:40"),
        ]
        for col, (icon, label, t) in zip(route_cols, route_steps):
            with col:
                st.markdown(f"""
                <div class="route-step">
                    <div class="icon">{icon}</div>
                    <div class="label">{label}</div>
                    <div class="time">{t}</div>
                </div>
                """, unsafe_allow_html=True)

        # Technical details (collapsed)
        with st.expander("🔧 Technical Summary", expanded=False):
            tc1, tc2 = st.columns(2)
            with tc1:
                st.markdown("#### Privacy Actions")
                for action in result.get("privacy_actions", []):
                    st.json(action)
            with tc2:
                st.markdown("#### Bookings Secured")
                for booking in result.get("bookings", []):
                    st.json(booking)

        with st.expander("📄 Full Execution Log (JSON)", expanded=False):
            st.json(result)

        st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("### 🎓 AI Futures Lab — Concepts Demonstrated")

fc1, fc2, fc3, fc4 = st.columns(4)
for col, (title, concepts, desc) in zip(
    [fc1, fc2, fc3, fc4],
    [
        ("🏛️ Responsible AI",
         "Sovereign AI · Privacy Preserving",
         "Trust & confidentiality by design"),
        ("🔄 Systems Thinking",
         "Edge AI · Agentic AI",
         "Pervasive AI at scale"),
        ("🎯 Real-World Alignment",
         "Causal AI · True Reasoning",
         "Understanding physics & consequences"),
        ("📈 Continuous Improvement",
         "Continuous Learning",
         "Experience captured & applied"),
    ],
):
    with col:
        st.markdown(f"**{title}**")
        st.caption(concepts)
        st.markdown(f"_{desc}_")

st.markdown("---")
st.caption("🛡️ Sovereign Executive Agent Demo | AI Futures Lab 2026")
