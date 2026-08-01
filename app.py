import time
import streamlit as st

from src.langgraph.graph import app
from src.utils.config import (
    MODEL,
    TOP_K,
    MAX_HISTORY
)
from src.utils.source_formatter import format_sources

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="ScholarAgent",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

section[data-testid="stSidebar"]{
    border-right:1px solid #3b3b3b;
}

div[data-testid="metric-container"]{
    border:1px solid #3b3b3b;
    border-radius:12px;
    padding:15px;
    background-color:#262730;
}

div[data-testid="stExpander"]{
    border-radius:10px;
}

.stButton button{
    width:100%;
    border-radius:10px;
}

.stChatMessage{
    border-radius:12px;
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)
# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🎓 ScholarAgent")

st.caption(
    "AI Research Assistant powered by LangGraph • Gemini • RAG"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("⚙️ Settings")

    st.success("Backend Connected ✅")

    st.divider()

    st.write("### 🤖 Model")
    st.info(MODEL)

    st.write("### 📚 Retrieval")
    st.info(f"Top K = {TOP_K}")

    st.write("### 💬 Memory")
    st.info(f"History = {MAX_HISTORY}")

    st.divider()

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []
        st.session_state.chat_history = []

        st.rerun()

    st.divider()

    st.caption(
        "ScholarAgent\n\nLangGraph • ChromaDB • Tavily • arXiv"
    )

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --------------------------------------------------
# Welcome Screen
# --------------------------------------------------

if len(st.session_state.messages) == 0:

    st.info("👋 Welcome to ScholarAgent!")

    st.markdown("### 💡 Try asking")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
- Explain self-attention
- What is LangGraph?
- Explain MCP
""")

    with c2:

        st.markdown("""
- Latest AI news
- Latest RAG papers
- Summarize Attention Is All You Need
""")

# --------------------------------------------------
# Previous Messages
# --------------------------------------------------

for message in st.session_state.messages:

    avatar = "👤" if message["role"] == "user" else "🎓"

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):
        st.markdown(message["content"])
# --------------------------------------------------
# Chat Input
# --------------------------------------------------

query = st.chat_input("Ask ScholarAgent...")

if query:

    # -------------------------
    # Show User Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message(
        "user",
        avatar="👤"
    ):
        st.markdown(query)

    # -------------------------
    # Backend Call
    # -------------------------

    try:

        start = time.time()

        with st.spinner("🧠 Thinking..."):

            result = app.invoke(
                {
                    "query": query,
                    "chat_history": st.session_state.chat_history
                }
            )

        response_time = time.time() - start

        answer = result["answer"]

        st.session_state.chat_history = result["chat_history"]

    except Exception as e:

        with st.chat_message(
            "assistant",
            avatar="🎓"
        ):
            st.error(f"❌ {str(e)}")

        st.stop()

    # -------------------------
    # Save Assistant Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # -------------------------
    # Assistant Response
    # -------------------------

    with st.chat_message(
        "assistant",
        avatar="🎓"
    ):

        st.markdown(answer)

        st.divider()

        # -------------------------
        # Metrics
        # -------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "⏱ Response",
                f"{response_time:.2f}s"
            )

        with col2:

            st.metric(
                "📚 Sources",
                len(result.get("sources", []))
            )

        with col3:

            tool = result.get("last_tool", "N/A")

            st.metric(
                "🛠 Tool",
                tool.upper()
            )
                # --------------------------------------------------
        # Execution Summary
        # --------------------------------------------------

        execution_steps = result.get("execution_steps", [])

        if execution_steps:

            with st.expander("🛠 Execution Summary", expanded=False):

                for step in execution_steps:
                    st.success(step)

        # --------------------------------------------------
        # Sources
        # --------------------------------------------------

        sources = result.get("sources", [])

        if sources:

            with st.expander("📚 Sources", expanded=False):

                for i, source in enumerate(sources, start=1):

                    title = source.get("title", "Unknown Source")
                    url = source.get("url", "")
                    page = source.get("page", "Unkown")
                    if url:
                        st.markdown(
                            f"""
                            <div style="font-size:13px; line-height:1.4; margin-bottom:6px;">
                            📄 <a href="{url}" target="_blank">{title}</a>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        
                    else:
                       st.markdown(
                            f"📄 **{title}** &nbsp;&nbsp;<span style='color:gray;'>Page {page}</span>",
                            unsafe_allow_html=True
                        )

        # --------------------------------------------------
        # Retrieved Context
        # --------------------------------------------------

        context = result.get("context", "")

        if context:

            with st.expander("📄 Retrieved Context", expanded=False):

                st.code(
                    context[:3000],
                    language="text"
                )

        # --------------------------------------------------
        # Error
        # --------------------------------------------------

        if result.get("error"):

            st.warning(result["error"])