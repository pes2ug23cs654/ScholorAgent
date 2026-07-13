import os
import sys
import time

from utils.tools_registry import TOOLS
from utils.router import choose_tool
from utils.prompt import build_prompt
from utils.llm import ask_llm
from utils.formatter import print_sources
from utils.query_rewritter import rewrite_query


# -------------------------------------------------
# Verify Vector Database
# -------------------------------------------------

if not os.path.exists("chroma_db"):
    print("❌ Vector Database not found.")
    print("Please run 'index_documents.py' first.")
    sys.exit()


# -------------------------------------------------
# Banner
# -------------------------------------------------

print("=" * 60)
print("📚 ScholarAgent - Research Paper Assistant")
print("Type 'exit' to quit.")
print("=" * 60)


# -------------------------------------------------
# Main Chat Loop
# -------------------------------------------------

while True:

    query = input("\nYou: ").strip()

    if query.lower() in ["exit", "quit"]:
        print("\n👋 Exiting ScholarAgent...")
        break

    overall_start = time.time()

    try:
         # -------------------------------
        # Route Query
        # -------------------------------

        print("\n🧠 Selecting tool...")

        tool = choose_tool(query)

        print(f"Using Tool: {tool}")
        # -------------------------------
        # Rewrite Query
        # -------------------------------

        print("\n🔄 Optimizing query...")
        rewritten_query = rewrite_query(query,tool)

        print(f"Search Query: {rewritten_query}")

       

        # -------------------------------
        # Fetch Tool
        # -------------------------------

        tool_function = TOOLS.get(tool)

        if tool_function is None:
            print(f"\n❌ Tool '{tool}' not found.")
            continue

        # -------------------------------
        # Execute Tool
        # -------------------------------

        print(f"\n🔍 Running {tool} search...")

        result = tool_function(rewritten_query)

        context = result.get("context", "")
        sources = result.get("sources", [])

        if not context.strip():
            print("\n⚠️ No relevant information found.")
            continue

        # -------------------------------
        # Tool Summary
        # -------------------------------

        print("\n========== TOOL SUMMARY ==========")
        print(f"Tool            : {result.get('tool')}")
        print(f"Sources         : {len(sources)}")
        print(f"Context Length  : {len(context)} characters")
        print(f"Execution Time  : {result.get('execution_time', 0):.2f}s")
        print("==================================")

        # -------------------------------
        # Build Prompt
        # -------------------------------

        print("\n📝 Building prompt...")

        prompt = build_prompt(context, rewritten_query)

        # Uncomment for debugging
        # print(prompt)

        # -------------------------------
        # Ask LLM
        # -------------------------------

        print("\n🤖 Generating answer...")

        answer = ask_llm(prompt)

        # -------------------------------
        # Display Response
        # -------------------------------

        print("\nAssistant:\n")
        print(answer)

        print_sources(sources)

        print(
            f"\n⏱️ Total Pipeline Time: "
            f"{time.time() - overall_start:.2f} seconds"
        )

    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        break

    except Exception as e:
        print(f"\n❌ {type(e).__name__}: {e}")