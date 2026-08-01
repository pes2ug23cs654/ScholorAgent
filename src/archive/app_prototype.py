import streamlit as st
from src.langgraph.graph import app
from src.utils.source_formatter import format_sources
import time
st.set_page_config(
    page_title="ScholorAgent",
    page_icon="🎓",
    layout = "wide"
    initial_sidebar_state = "expanded"
)
from src.utils.config import (
    MODEL,
    TOP_K,
    MAX_HISTORY
)

st.title("🎓 ScholarAgent")
st.caption("Your AI Research Assistant powered by LangGraph, RAG, and Gemini")
with st.sidebar:

    st.header("⚙️ Settings")

    st.write("### 🤖 Model")
    st.info(MODEL)

    st.write("### 📚 Retrieval")
    st.info(f"Top K = {TOP_K}")

    st.write("### 💬 Memory")
    st.info(f"History = {MAX_HISTORY}")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []
        st.session_state.chat_history = []

        st.rerun()
# --------------
# Session State
# --------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --------------
# Display Previous Messages
# --------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------
# Chat Input
# --------------
query = st.chat_input("Ask ScholorAgent....")

if query:
    
    # show user message
    st.session_state.messages.append(
        {
            "role":"user",
            "content": query
        }
    )
    with st.chat_message("user"):
        st.markdown(query)
    if not st.session_state.messages:

        st.info("👋 Welcome to ScholarAgent!")

        st.markdown("### Try asking:")

        st.markdown("""
- Explain self-attention
- What is LangGraph?
- Latest RAG papers
- Explain MCP
- Latest OpenAI news
""")
    try:
        start = time.time()
        with st.spinner("🧠 Thinking...."):
            result = app.invoke(
            {
                "query":query,
                "chat_history":st.session_state.chat_history
            }
        )
        response_time = time.time() - start
        answer = result["answer"]
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.stop()
    st.session_state.chat_history = result["chat_history"]
    
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content": answer
        }
    )
    with st.chat_message("assistant"):

        st.markdown(answer)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("⏱ Response Time", f"{response_time:.2f}s")

        with col2:
            st.metric("📚 Sources", len(result["sources"]))

        if result["execution_steps"]:
            with st.expander("🛠 Execution Summary"):
                for step in result["execution_steps"]:
                    st.write(step)

        if result["sources"]:
            with st.expander("📚 Sources"):
                st.markdown(
                f"```text\n{format_sources(result['sources'])}\n```"
            )

        if result["context"]:
            with st.expander("📄 Retrieved Context"):
                st.text(result["context"][:3000])