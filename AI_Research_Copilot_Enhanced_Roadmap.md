# 🚀 AI Research Copilot (Agentic RAG) — Enhanced 7-Week Roadmap
## With Realistic Timings, YouTube Links & Step-by-Step Guide

---

## 📋 BEFORE YOU START: Complete This Checklist

### System Requirements
- [ ] Computer with 8GB+ RAM (16GB ideal)
- [ ] Python 3.10+ installed
- [ ] ~4-5 hours per day available for next 7 weeks
- [ ] GitHub account created
- [ ] Google account (for Gemini API)

### Mental Checklist
- [ ] Ready to ship over polish (Week 4 MVP > perfect Week 1 code)
- [ ] Okay with debugging errors (not all tutorials work first try)
- [ ] Can ask for help when stuck (don't struggle alone)
- [ ] Have a quiet place to work (focus matters)

---

# 🎯 PHASE 0: SETUP (2 Days) — DO THIS FIRST

## What You'll Do
- Set up development environment
- Create project repository
- Install essential tools
- **Total Time: 3-4 hours**

## Step-by-Step Setup

### Step 1: Install Python (30 min)
1. Go to **python.org**
2. Download Python 3.11 or 3.12 (not 3.9, not 3.13 beta)
3. Install with ✓ "Add Python to PATH" checkbox **checked**
4. Verify:
   ```bash
   python --version
   ```
   Should output: `Python 3.11.x` or `Python 3.12.x`

### Step 2: Install VS Code (15 min)
1. Go to **code.visualstudio.com**
2. Download and install
3. Open VS Code
4. Install extensions:
   - Python (Microsoft)
   - Pylance (Microsoft)
   - Thunder Client (optional, for API testing)

### Step 3: Install Git (10 min)
1. Go to **git-scm.com**
2. Download and install (use defaults)
3. Verify:
   ```bash
   git --version
   ```

### Step 4: Create GitHub Repository (15 min)
1. Go to **github.com** and sign in
2. Click "New repository"
3. Name: `ai-research-copilot`
4. Description: `Agentic RAG system for research paper analysis`
5. Public (so portfolio visible)
6. Add README.md (tick the checkbox)
7. Create repository
8. Clone to your computer:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-research-copilot.git
   cd ai-research-copilot
   ```

### Step 5: Create Virtual Environment (15 min)
1. Open terminal in your project folder
2. Run:
   ```bash
   python -m venv venv
   ```
3. Activate:
   - **Windows:** `venv\Scripts\activate`
   - **Mac/Linux:** `source venv/bin/activate`
4. You should see `(venv)` in your terminal prompt
5. Install pip upgrade:
   ```bash
   pip install --upgrade pip
   ```

### Step 6: Learn Git Basics (1 hour, WATCH THIS)
**YouTube Search:** `Git and GitHub Crash Course Traversy Media`
- Watch: **First 45 minutes only**
- Learn: clone, add, commit, push, pull
- Don't learn: branching, merging, advanced stuff
- **By end:** Understand commit workflow

### Step 7: Create First Commit
1. In your repo folder:
   ```bash
   echo "# AI Research Copilot" > README.md
   git add .
   git commit -m "Initial commit - setup"
   git push origin main
   ```
2. Check GitHub — you should see the commit

**✅ Phase 0 Complete Checklist:**
- [ ] Python 3.11+ installed and verified
- [ ] VS Code installed with Python extension
- [ ] Git installed
- [ ] GitHub repo created and cloned locally
- [ ] Virtual environment created and activated
- [ ] First commit pushed to GitHub
- [ ] Watched Git crash course (45 min)

---

# 📚 WEEK 1: Core Concepts (LLM → Embeddings → Vector DB → RAG)

## Weekly Goal
Understand the full RAG pipeline conceptually AND build a working mini-RAG system.

**Time Allocation:**
- Learning: ~2 hours/day
- Building: ~2 hours/day
- Notes: 15 min/day
- **Total: 4.25 hours/day × 5 days = ~21 hours**

---

## DAY 1: LLM Fundamentals (Learning)

### What You'll Learn
- What is an LLM?
- Tokens and tokenization
- Context window
- Temperature and parameters
- How GPT works (intuition)

### Video 1: Andrej Karpathy - Intro to LLMs
- **YouTube Search:** `Intro to Large Language Models Andrej Karpathy`
- **Link:** [Direct if available] Or search on YouTube
- **Duration:** 60 minutes
- **Watch Time:** 1 hour (watch first video only)
- **Note:** Don't take detailed notes. Just understand the concepts.

**Key Concepts to Understand (not memorize):**
- Tokens = words broken into subunits
- Context window = max tokens an LLM can see at once
- Temperature = randomness (0 = deterministic, 1 = creative)
- Transformer = architecture behind GPT

### Video 2: StatQuest - Tokens Explained (Optional, 15 min)
- **YouTube Search:** `Tokens in Large Language Models StatQuest`
- **If** Karpathy felt too fast, watch this for intuition
- **If** you understood Karpathy, skip it

### Video 3: How ChatGPT Works (5 min visual)
- **YouTube Search:** `How ChatGPT Works Explanation`
- Pick any popular one (Fireship or similar)
- Just watch to feel confident about your understanding

### Quick Notes Template (15 min)
Write these down in a file called `notes.md`:
```markdown
## Week 1 - Day 1: LLM Fundamentals

### Key Concepts
- Token: [1 sentence definition]
- Context Window: [1 sentence definition]
- Temperature: [1 sentence definition]
- LLM: [1 sentence definition]

### I understand
- [ ] What tokens are
- [ ] Why context window matters
- [ ] How LLMs predict text

### I'm confused about
- [List anything you didn't get]
```

**Time Breakdown:**
- Karpathy video: 60 min
- StatQuest (optional): 15 min
- Note-taking: 15 min
- **Total: 60-90 min**

---

## DAY 2: Use an LLM API (Hands-On Coding)

### What You'll Build
A simple chatbot that uses Gemini API

### Why Gemini?
- Free and easy
- Good quality responses
- Straightforward API

### Setup: Get Gemini API Key (10 min)
1. Go to **ai.google.dev/aistudio**
2. Click "Get API Key"
3. Create new API key
4. Copy the key (save safely)
5. **Never share this key publicly**

### Code: Simple Chatbot (45 min)

1. Create file: `01_simple_chatbot.py`
2. Install Gemini library:
   ```bash
   pip install google-generativeai
   ```
3. Write code:
   ```python
   import google.generativeai as genai
   
   # Set API key
   genai.configure(api_key="YOUR_API_KEY_HERE")
   
   # Initialize model
   model = genai.GenerativeModel('gemini-1.5-flash')
   
   # Simple chat loop
   print("=== Simple Chatbot ===")
   print("Type 'exit' to quit\n")
   
   while True:
       user_input = input("You: ")
       if user_input.lower() == 'exit':
           break
       
       try:
           response = model.generate_content(user_input)
           print(f"Bot: {response.text}\n")
       except Exception as e:
           print(f"Error: {e}\n")
   ```
4. Run:
   ```bash
   python 01_simple_chatbot.py
   ```
5. Test: Ask it questions
   - "What is Python?"
   - "Explain quantum computing in 2 sentences"
   - "What's 2+2?"

### Debugging Tips
- **"API key invalid"?** → Check you copied the key correctly
- **"Module not found"?** → Make sure venv is activated, then `pip install google-generativeai`
- **No response?** → Check internet connection

### Challenge (Optional, 15 min)
Modify the code to:
- Remember the conversation (store previous messages)
- Add a system prompt (e.g., "You are a helpful assistant")

**Time Breakdown:**
- Gemini API setup: 10 min
- Code writing: 20 min
- Testing: 10 min
- Challenge/debugging: 15 min
- **Total: 45-55 min**

### Commit Your Code
```bash
git add .
git commit -m "Week 1 Day 2: Simple chatbot with Gemini API"
git push origin main
```

---

## DAY 3: Embeddings (Learning + Building)

### What You'll Learn
- What embeddings are
- Why they matter
- How to compute similarity
- Vector representations

### Video: StatQuest - Embeddings Explained
- **YouTube Search:** `Embeddings StatQuest`
- **Duration:** ~15 minutes
- **Watch:** Entire video
- **Concept:** Turning text into numbers, then computing similarity

### Video 2: What Are Embeddings? (Alternative)
- **YouTube Search:** `What are embeddings AI explained`
- Pick any clear 10-min explanation
- Just for reinforcement

### Build: Embeddings + Similarity (60 min)

1. Install libraries:
   ```bash
   pip install numpy sentence-transformers
   ```

2. Create file: `02_embeddings.py`

3. Code:
   ```python
   from sentence_transformers import SentenceTransformer
   import numpy as np
   from sklearn.metrics.pairwise import cosine_similarity
   
   # Initialize embedding model (small, fast)
   model = SentenceTransformer('all-MiniLM-L6-v2')
   
   # Sample sentences
   sentences = [
       "The cat sat on the mat",
       "A feline rested on a rug",
       "Machine learning is fascinating",
       "AI and deep learning are related"
   ]
   
   # Generate embeddings
   embeddings = model.encode(sentences)
   print(f"Each sentence → {embeddings.shape[1]} dimensional vector\n")
   
   # Test similarity
   print("=== Similarity Matrix ===")
   similarity_matrix = cosine_similarity(embeddings)
   
   for i, sent1 in enumerate(sentences):
       for j, sent2 in enumerate(sentences):
           if i < j:  # Only upper triangle
               sim = similarity_matrix[i][j]
               print(f"\n'{sent1}' vs '{sent2}'")
               print(f"Similarity: {sim:.2%}")
   
   # Find most similar
   query = "A cat on furniture"
   query_embedding = model.encode([query])
   similarities = cosine_similarity(query_embedding, embeddings)[0]
   
   print(f"\n=== Most Similar to '{query}' ===")
   top_idx = np.argsort(similarities)[::-1][0]
   print(f"Answer: '{sentences[top_idx]}'")
   print(f"Similarity: {similarities[top_idx]:.2%}")
   ```

4. Run:
   ```bash
   python 02_embeddings.py
   ```
   
   Expected output:
   ```
   Each sentence → 384 dimensional vector
   
   === Similarity Matrix ===
   'The cat sat on the mat' vs 'A feline rested on a rug'
   Similarity: 78.92%
   ...
   ```

### What's Happening?
- Each sentence → 384-dimensional vector
- Similar sentences have higher cosine similarity
- This is the foundation of RAG (finding relevant documents)

### Commit
```bash
git add .
git commit -m "Week 1 Day 3: Embeddings and similarity search"
git push origin main
```

**Time Breakdown:**
- Videos: 25 min
- Embedding code: 25 min
- Testing + understanding: 15 min
- **Total: 65 min**

---

## DAY 4: Vector Databases (Learning + Building)

### What You'll Learn
- What is a vector database?
- Why ChromaDB?
- How to store and retrieve vectors

### Video: ChromaDB Intro (10 min)
- **YouTube Search:** `ChromaDB tutorial getting started`
- OR go to **docs.trychroma.com** (official docs are great)

### Build: Vector DB with ChromaDB (70 min)

1. Install:
   ```bash
   pip install chromadb
   ```

2. Create file: `03_vector_db.py`

3. Code:
   ```python
   import chromadb
   
   # Initialize Chroma client (local, in-memory)
   client = chromadb.Client()
   
   # Create collection
   collection = client.create_collection(name="documents")
   
   # Sample documents
   documents = [
       "Python is a programming language",
       "Machine learning uses algorithms",
       "Deep learning uses neural networks",
       "Vector databases store embeddings",
       "RAG combines retrieval and generation"
   ]
   
   # Add documents to collection
   collection.add(
       documents=documents,
       ids=[f"doc_{i}" for i in range(len(documents))]
   )
   
   print("✓ Added 5 documents to ChromaDB\n")
   
   # Query the database
   query = "What is machine learning?"
   
   results = collection.query(
       query_texts=[query],
       n_results=2
   )
   
   print(f"Query: '{query}'")
   print(f"\nTop 2 matching documents:")
   for i, doc in enumerate(results['documents'][0]):
       distance = results['distances'][0][i]
       print(f"{i+1}. {doc} (distance: {distance:.3f})")
   
   # Another query
   print("\n" + "="*50 + "\n")
   query2 = "Tell me about databases"
   
   results2 = collection.query(
       query_texts=[query2],
       n_results=3
   )
   
   print(f"Query: '{query2}'")
   print(f"\nTop 3 matching documents:")
   for i, doc in enumerate(results2['documents'][0]):
       distance = results2['distances'][0][i]
       print(f"{i+1}. {doc} (distance: {distance:.3f})")
   ```

4. Run:
   ```bash
   python 03_vector_db.py
   ```

### Expected Output
```
✓ Added 5 documents to ChromaDB

Query: 'What is machine learning?'

Top 2 matching documents:
1. Machine learning uses algorithms (distance: 0.123)
2. Deep learning uses neural networks (distance: 0.456)
```

### What's Happening?
- ChromaDB takes text, converts to embeddings automatically
- Stores them in a searchable database
- Your query gets embedded too
- It finds the closest documents (by vector distance)

### Commit
```bash
git add .
git commit -m "Week 1 Day 4: Vector database with ChromaDB"
git push origin main
```

**Time Breakdown:**
- Video: 10 min
- Setup + code: 35 min
- Testing + experimentation: 25 min
- **Total: 70 min**

---

## DAY 5: RAG Concept (Learning)

### What You'll Learn
- What is RAG?
- Why RAG is powerful
- The RAG pipeline

### Video 1: IBM - What is RAG? (8 min)
- **YouTube Search:** `What is RAG IBM`
- Short, clear explanation

### Video 2: RAG Explained (10 min)
- **YouTube Search:** `RAG explanation AssemblyAI`
- Slightly more detailed

### Diagram: RAG Pipeline (Write it down)
```
User Question
     ↓
     [Embedding]
     ↓
Search Vector DB
     ↓
Get Top 3 Documents
     ↓
Pass to LLM with Context
     ↓
LLM Generates Answer
     ↓
Return to User
```

### Key Insight
- **Without RAG:** LLM answers from training data only (hallucinations, outdated)
- **With RAG:** LLM answers from YOUR documents (accurate, current, verifiable)

### Notes: RAG Summary
```markdown
## RAG (Retrieval Augmented Generation)

### Pipeline
1. User asks a question
2. Question is converted to embedding
3. Vector DB finds most relevant documents
4. Documents + question sent to LLM
5. LLM generates answer using the documents

### Why it matters
- Prevents hallucinations
- Uses current/custom information
- Verifiable (sources included)
- More accurate than LLM alone

### Example
Question: "What did the CATDS paper find?"
Without RAG: LLM doesn't know what CATDS is
With RAG: Retrieves CATDS paper → LLM reads it → accurate answer
```

**Time Breakdown:**
- Videos: 20 min
- Reading + understanding: 15 min
- Note-taking: 15 min
- **Total: 50 min**

---

## DAY 6: Build Mini RAG (Hands-On)

### What You'll Build
A working RAG system (simple version, no LLM yet)

1. Create text file with sample content: `sample_doc.txt`
   ```
   Artificial Intelligence (AI) is the simulation of human intelligence
   by machines. Machine learning is a subset of AI that enables systems
   to learn from data. Deep learning uses neural networks to process
   complex patterns.
   
   Embeddings are numerical representations of text. They capture
   semantic meaning, allowing us to compute similarity between texts.
   Vector databases store embeddings for fast retrieval.
   
   RAG combines retrieval and generation. First, relevant documents
   are retrieved using similarity search. Then, an LLM generates
   responses based on these documents.
   ```

2. Create file: `04_mini_rag.py`

3. Code:
   ```python
   import chromadb
   from sentence_transformers import SentenceTransformer
   
   # Initialize embedding model
   embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
   
   # Initialize Chroma
   client = chromadb.Client()
   collection = client.create_collection(name="mini_rag")
   
   # Read sample document
   with open('sample_doc.txt', 'r') as f:
       text = f.read()
   
   # Split into sentences (simple chunking)
   sentences = text.split('. ')
   sentences = [s.strip() + '.' for s in sentences if s.strip()]
   
   # Add to vector DB
   collection.add(
       documents=sentences,
       ids=[f"chunk_{i}" for i in range(len(sentences))]
   )
   
   print(f"✓ Loaded {len(sentences)} text chunks\n")
   
   # Simple RAG: Query and retrieve
   def rag_search(query, top_k=2):
       results = collection.query(
           query_texts=[query],
           n_results=top_k
       )
       return results['documents'][0]
   
   # Test queries
   queries = [
       "What is AI?",
       "How do embeddings work?",
       "What is RAG?"
   ]
   
   for query in queries:
       print(f"Q: {query}")
       relevant_docs = rag_search(query)
       print(f"A: {relevant_docs[0]}")
       print()
   ```

4. Run:
   ```bash
   python 04_mini_rag.py
   ```

### Output Example
```
Q: What is AI?
A: Artificial Intelligence (AI) is the simulation of human intelligence by machines.

Q: How do embeddings work?
A: Embeddings are numerical representations of text.

Q: What is RAG?
A: RAG combines retrieval and generation.
```

### Commit
```bash
git add .
git commit -m "Week 1 Day 6: Mini RAG system without LLM"
git push origin main
```

**Time Breakdown:**
- Code writing: 30 min
- Testing + debugging: 20 min
- Understanding what happened: 15 min
- **Total: 65 min**

---

## DAY 7: Review & Reflect (No New Code)

### Review Checklist
- [ ] I can explain what tokens are
- [ ] I can explain embeddings
- [ ] I can explain vector similarity
- [ ] I can use ChromaDB
- [ ] I understand the RAG pipeline
- [ ] I've built: chatbot, embeddings search, vector DB, mini-RAG

### Write Summary Notes
Create file: `WEEK1_SUMMARY.md`

```markdown
# Week 1 Summary

## What I Built
1. Chatbot using Gemini API
2. Embedding-based similarity search
3. ChromaDB vector database
4. Mini RAG without LLM

## What I Learned
- Tokens: text broken into subunits
- Embeddings: vectors that capture meaning
- Vector DB: stores and searches embeddings
- RAG: retrieves relevant docs, then generates answers

## Key Insights
- Embeddings are the bridge between text and math
- ChromaDB makes building RAG accessible
- RAG = solve hallucination problem

## What I'm Confused About
[Write anything unclear]

## Next Week
- Add PDF support
- Integrate LLM for answering
- Build proper RAG pipeline with LangChain
```

### Reflection Questions (Write Answers)
1. What was the hardest part this week?
2. What excites you most about RAG?
3. What do you want to build next week?

**Time Breakdown:**
- Review: 15 min
- Summary writing: 20 min
- Reflection: 15 min
- **Total: 50 min**

### Week 1 Completion Checklist
- [ ] All 4 programs working (chatbot, embeddings, vector DB, mini-RAG)
- [ ] Committed to GitHub with good commit messages
- [ ] Summary notes written
- [ ] Understand RAG pipeline (can explain to someone else)
- [ ] Ready to move to Week 2

---

# 🔄 WEEK 2: Build PDF RAG with LangChain

## Weekly Goal
Build a real RAG system that reads PDFs and answers questions.

**Time Allocation:**
- Learning: ~1.5 hours/day
- Building: ~2.5 hours/day
- Testing: ~1 hour/day
- **Total: ~5 hours/day × 5 days = 25 hours**

---

## What You'll Learn This Week
- PDF parsing and text extraction
- Text chunking strategies
- LangChain basics
- Building RAG chains
- Handling multiple documents

---

## DAY 1: LangChain Fundamentals + PDF Handling

### Video: LangChain Intro
- **YouTube Search:** `LangChain Tutorial for Beginners`
- Watch: First 15 minutes (just basics)
- Key concepts: Components, chains, agents

### Video 2: PDF Processing
- **YouTube Search:** `Extract text from PDF Python pypdf`
- Learn: How to read PDF files programmatically

### Read Official Docs (30 min)
Go to **python.langchain.com/docs**
- Scroll to "Integrations"
- Find "Document Loaders"
- Read PDFs section

### Code: PDF Text Extraction (45 min)

1. Install:
   ```bash
   pip install pypdf langchain-community langchain-google-genai
   ```

2. Create sample PDF (use online tool to generate, or use any PDF)
   - Save as: `sample_paper.pdf` in your project folder

3. Create file: `05_pdf_extraction.py`

   ```python
   from pypdf import PdfReader
   
   # Load PDF
   pdf_path = "sample_paper.pdf"
   reader = PdfReader(pdf_path)
   
   print(f"Total pages: {len(reader.pages)}\n")
   
   # Extract text from all pages
   full_text = ""
   for page_num, page in enumerate(reader.pages):
       text = page.extract_text()
       full_text += text + "\n"
       print(f"Extracted page {page_num + 1}")
   
   print(f"\n=== First 500 characters ===")
   print(full_text[:500])
   
   # Save extracted text
   with open("extracted_text.txt", "w") as f:
       f.write(full_text)
   
   print(f"\n✓ Saved to extracted_text.txt")
   ```

4. Run:
   ```bash
   python 05_pdf_extraction.py
   ```

5. Check: You should have `extracted_text.txt` with the PDF content

### Commit
```bash
git add .
git commit -m "Week 2 Day 1: PDF extraction with pypdf"
git push origin main
```

**Time Breakdown:**
- Videos: 20 min
- Read docs: 30 min
- Code: 20 min
- Testing: 10 min
- **Total: 80 min**

---

## DAY 2: Text Chunking

### Why Chunking?
- PDFs can be long (too large for LLM context)
- Need to split into manageable pieces
- Overlap helps with semantic continuity

### Video: Chunking Strategies
- **YouTube Search:** `Text chunking for RAG explained`
- Learn: Fixed vs recursive chunking

### Read: LangChain Text Splitters
Go to **python.langchain.com/docs**
- Search: "Text Splitters"
- Read about `RecursiveCharacterTextSplitter`

### Code: Smart Chunking (60 min)

Create file: `06_text_chunking.py`

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Read extracted text
with open("extracted_text.txt", "r") as f:
    text = f.read()

# Initialize text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Characters per chunk
    chunk_overlap=50,    # Overlap between chunks
    separators=["\n\n", "\n", " ", ""]  # Split by these, in order
)

# Split text
chunks = splitter.split_text(text)

print(f"Total chunks: {len(chunks)}\n")

# Show first 3 chunks
for i, chunk in enumerate(chunks[:3]):
    print(f"=== Chunk {i+1} ===")
    print(chunk[:200] + "...\n")

# Save chunks
with open("chunks.txt", "w") as f:
    for i, chunk in enumerate(chunks):
        f.write(f"--- CHUNK {i} ---\n{chunk}\n\n")

print(f"✓ Saved {len(chunks)} chunks to chunks.txt")
```

Run:
```bash
python 06_text_chunking.py
```

### What Chunk Size Should You Use?
- **Small (100-300):** More precise retrieval, more chunks
- **Medium (500-800):** Balanced, recommended
- **Large (1000+):** Broader context, fewer chunks

**Time Breakdown:**
- Video: 15 min
- Read docs: 20 min
- Code: 20 min
- Testing + tuning: 15 min
- **Total: 70 min**

---

## DAY 3: LangChain RAG Pipeline

### What You'll Build
RAG chain that:
1. Takes user question
2. Searches vector DB
3. Gets relevant documents
4. Passes to LLM
5. Returns answer

### Video: LangChain RAG Implementation
- **YouTube Search:** `LangChain RAG example tutorial`
- Watch: ~20 minutes

### Code: Full RAG Pipeline (90 min)

Create file: `07_pdf_rag.py`

```python
from langchain_text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from pypdf import PdfReader

# =======================
# 1. Load & Extract PDF
# =======================
pdf_path = "sample_paper.pdf"
reader = PdfReader(pdf_path)
full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

print("✓ Loaded PDF\n")

# =======================
# 2. Split into Chunks
# =======================
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_text(full_text)
print(f"✓ Created {len(chunks)} chunks\n")

# =======================
# 3. Create Vector DB
# =======================
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key="YOUR_GEMINI_API_KEY"  # Use same as before
)

vectorstore = Chroma.from_texts(
    chunks,
    embedding=embeddings,
    collection_name="pdf_rag"
)
print("✓ Created vector database\n")

# =======================
# 4. Create Retriever
# =======================
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# =======================
# 5. Setup LLM
# =======================
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key="YOUR_GEMINI_API_KEY"
)

# =======================
# 6. Create RAG Chain
# =======================
system_prompt = """You are a helpful assistant analyzing research papers.
Use the provided documents to answer questions accurately.
If the information isn't in the documents, say so."""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# =======================
# 7. Test RAG
# =======================
print("="*50)
print("PDF RAG System Ready!")
print("="*50 + "\n")

queries = [
    "What is the main topic of this paper?",
    "What methods were used?",
    "What are the key findings?"
]

for query in queries:
    print(f"Q: {query}")
    result = rag_chain.invoke({"input": query})
    print(f"A: {result['answer']}\n")
```

### Important Notes
- Replace `YOUR_GEMINI_API_KEY` with your actual key
- Make sure `sample_paper.pdf` exists
- First run might take a minute (building vector DB)

Run:
```bash
python 07_pdf_rag.py
```

### Expected Output
```
Q: What is the main topic of this paper?
A: [Answer based on your PDF content]

Q: What methods were used?
A: [Relevant section from your paper]
```

### Commit
```bash
git add .
git commit -m "Week 2 Day 3: Full PDF RAG pipeline with LangChain"
git push origin main
```

**Time Breakdown:**
- Video: 20 min
- Code writing: 40 min
- Testing + debugging: 30 min
- **Total: 90 min**

---

## DAY 4-5: Multi-Document Support + Testing

### What You'll Build
RAG system that handles multiple PDFs at once

### Code: Multi-Document RAG (120 min)

Create file: `08_multi_pdf_rag.py`

```python
import os
from pathlib import Path
from langchain_text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from pypdf import PdfReader

# =======================
# 1. Load Multiple PDFs
# =======================
def load_pdfs_from_folder(folder_path):
    """Load all PDFs from a folder"""
    pdf_files = list(Path(folder_path).glob("*.pdf"))
    
    all_text = ""
    for pdf_file in pdf_files:
        print(f"Loading: {pdf_file.name}")
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            all_text += page.extract_text() + "\n"
    
    return all_text, len(pdf_files)

# For now, use single PDF, but structure allows multiple
pdf_text, num_pdfs = load_pdfs_from_folder(".")  # Current directory
print(f"✓ Loaded {num_pdfs} PDFs\n")

# =======================
# 2. Split & Embed
# =======================
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_text(pdf_text)
print(f"✓ Created {len(chunks)} chunks\n")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key="YOUR_GEMINI_API_KEY"
)

vectorstore = Chroma.from_texts(
    chunks,
    embedding=embeddings,
    collection_name="multi_pdf_rag"
)

# =======================
# 3. Setup RAG
# =======================
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key="YOUR_GEMINI_API_KEY"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert at analyzing research papers. Use the provided documents."),
    ("human", "{input}")
])

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# =======================
# 4. Interactive Chat
# =======================
print("="*50)
print("Multi-Document RAG System Ready!")
print("Type 'exit' to quit")
print("="*50 + "\n")

while True:
    query = input("You: ").strip()
    if query.lower() == 'exit':
        break
    
    if not query:
        continue
    
    try:
        result = rag_chain.invoke({"input": query})
        print(f"AI: {result['answer']}\n")
    except Exception as e:
        print(f"Error: {e}\n")
```

Run:
```bash
python 08_multi_pdf_rag.py
```

Now you can ask multiple questions interactively!

### Commit
```bash
git add .
git commit -m "Week 2 Day 4-5: Multi-document RAG with interactive chat"
git push origin main
```

**Time Breakdown:**
- Code: 50 min
- Testing: 40 min
- Adding features: 30 min
- **Total: 120 min**

### Week 2 Completion Checklist
- [ ] Can extract text from PDFs
- [ ] Can chunk text intelligently
- [ ] Can build RAG pipeline with LangChain
- [ ] Can answer questions about PDFs
- [ ] Understand all components (retriever, LLM, chain)
- [ ] All code on GitHub with good commits

---

# ⚡ WEEK 3: Improve RAG (Citations, Multiple PDFs, Deployment Prep)

## Weekly Goal
Make RAG production-ready: better chunking, citations, multiple PDFs, error handling.

---

## DAY 1: Advanced Chunking

### Concept: Chunking Quality Matters
- Bad chunking = bad retrieval = bad answers
- Good chunking = relevant documents = better answers

### Video: Advanced Chunking
- **YouTube Search:** `Semantic chunking for RAG`

### Code: Better Chunking with Metadata

Create file: `09_advanced_chunking.py`

```python
from langchain_text_splitter import RecursiveCharacterTextSplitter
from pypdf import PdfReader

# Load PDF
pdf_path = "sample_paper.pdf"
reader = PdfReader(pdf_path)

# Extract with page numbers
chunks_with_metadata = []
for page_num, page in enumerate(reader.pages):
    text = page.extract_text()
    
    # Split per page
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    page_chunks = splitter.split_text(text)
    
    for chunk_idx, chunk in enumerate(page_chunks):
        chunks_with_metadata.append({
            "text": chunk,
            "page": page_num + 1,
            "chunk_id": f"page_{page_num}_chunk_{chunk_idx}"
        })

print(f"Created {len(chunks_with_metadata)} chunks with metadata\n")

# Show example
for i, chunk_data in enumerate(chunks_with_metadata[:2]):
    print(f"=== Chunk {chunk_data['chunk_id']} (Page {chunk_data['page']}) ===")
    print(chunk_data['text'][:200] + "...\n")
```

### Key Improvement
Now you can show users: "Answer based on Page 3, Chunk 2"

---

## DAY 2: Add Citations

### What's a Citation?
When answering, include: (Source: Page X)

### Code: RAG with Citations

Create file: `10_rag_with_citations.py`

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# [Setup vector store as before...]

# =======================
# Custom RAG with Citations
# =======================
def answer_with_citations(query, rag_chain):
    """Get answer and show which documents were used"""
    result = rag_chain.invoke({"input": query})
    
    answer = result['answer']
    
    # Get source documents
    sources = result.get('context', [])
    
    print(f"Q: {query}")
    print(f"\nA: {answer}")
    
    # Show sources
    if sources:
        print(f"\nSources:")
        for i, doc in enumerate(sources):
            print(f"  [{i+1}] {doc.page_content[:100]}...")
    
    return answer

# Usage
query = "What is the main finding?"
answer_with_citations(query, rag_chain)
```

---

## DAY 3: Handle Multiple PDFs Better

### Code: PDF Directory Loader

Create file: `11_directory_loader.py`

```python
from pathlib import Path
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# Create a "papers" folder and put PDFs there
papers_folder = "./papers"

if not Path(papers_folder).exists():
    print(f"Create folder: {papers_folder}")
    print("Put your PDF files there")
else:
    # Load all PDFs from folder
    loader = PyPDFDirectoryLoader(papers_folder)
    documents = loader.load()
    
    print(f"Loaded {len(documents)} documents\n")
    
    # Split and embed
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)
    
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key="YOUR_GEMINI_API_KEY"
    )
    
    vectorstore = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        collection_name="papers_db"
    )
    
    print(f"✓ Created vector store with {len(chunks)} chunks")
```

---

## DAY 4-5: Error Handling + Full Integration

### Code: Production-Ready RAG

Create file: `12_production_rag.py`

```python
import os
from pathlib import Path
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

class PDFRAGSystem:
    def __init__(self, pdf_folder="./papers", api_key=None):
        """Initialize RAG system"""
        self.pdf_folder = pdf_folder
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.vectorstore = None
        self.rag_chain = None
        
    def load_documents(self):
        """Load PDFs from folder"""
        try:
            if not Path(self.pdf_folder).exists():
                print(f"Error: Folder '{self.pdf_folder}' not found")
                return False
            
            loader = PyPDFDirectoryLoader(self.pdf_folder)
            documents = loader.load()
            
            if not documents:
                print("No PDFs found in folder")
                return False
            
            print(f"✓ Loaded {len(documents)} pages from PDFs")
            return True
        except Exception as e:
            print(f"Error loading PDFs: {e}")
            return False
    
    def build_vectorstore(self):
        """Build vector database"""
        try:
            loader = PyPDFDirectoryLoader(self.pdf_folder)
            documents = loader.load()
            
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50
            )
            chunks = splitter.split_documents(documents)
            
            embeddings = GoogleGenerativeAIEmbeddings(
                model="models/embedding-001",
                google_api_key=self.api_key
            )
            
            self.vectorstore = Chroma.from_documents(
                chunks,
                embedding=embeddings,
                collection_name="pdf_rag"
            )
            
            print(f"✓ Built vector store with {len(chunks)} chunks")
            return True
        except Exception as e:
            print(f"Error building vector store: {e}")
            return False
    
    def setup_rag_chain(self):
        """Setup RAG chain"""
        try:
            if not self.vectorstore:
                print("Vector store not initialized")
                return False
            
            llm = GoogleGenerativeAI(
                model="gemini-1.5-flash",
                google_api_key=self.api_key
            )
            
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are an expert at analyzing research papers. "
                           "Use the provided documents to answer questions accurately. "
                           "If information isn't in the documents, say so."),
                ("human", "{input}")
            ])
            
            retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})
            question_answer_chain = create_stuff_documents_chain(llm, prompt)
            self.rag_chain = create_retrieval_chain(retriever, question_answer_chain)
            
            print("✓ RAG chain ready")
            return True
        except Exception as e:
            print(f"Error setting up RAG chain: {e}")
            return False
    
    def answer(self, query):
        """Answer a question"""
        try:
            if not self.rag_chain:
                return "RAG system not initialized"
            
            result = self.rag_chain.invoke({"input": query})
            return result['answer']
        except Exception as e:
            return f"Error: {e}"
    
    def initialize(self):
        """Full initialization"""
        if not self.load_documents():
            return False
        if not self.build_vectorstore():
            return False
        if not self.setup_rag_chain():
            return False
        return True

# =======================
# Main Usage
# =======================
if __name__ == "__main__":
    # Initialize system
    rag = PDFRAGSystem(pdf_folder="./papers")
    
    if not rag.initialize():
        print("Failed to initialize RAG system")
        exit(1)
    
    print("\n" + "="*50)
    print("RAG System Ready!")
    print("Type 'exit' to quit\n" + "="*50 + "\n")
    
    # Interactive chat
    while True:
        query = input("You: ").strip()
        if query.lower() == 'exit':
            break
        if not query:
            continue
        
        answer = rag.answer(query)
        print(f"AI: {answer}\n")
```

### Commit
```bash
git add .
git commit -m "Week 3: Advanced RAG with citations, metadata, error handling"
git push origin main
```

### Week 3 Completion Checklist
- [ ] Better chunking with metadata
- [ ] Citations showing sources
- [ ] Handle multiple PDFs cleanly
- [ ] Error handling for failures
- [ ] Class-based structure for reusability
- [ ] Interactive chat working

---

# 🚀 WEEK 4: Deployment (Streamlit)

## Weekly Goal
Deploy your RAG system as a web app anyone can use.

---

## What is Streamlit?
- **Python → Web App** in minutes
- No HTML/CSS needed
- Perfect for ML projects
- Free cloud deployment

---

## DAY 1: Learn Streamlit

### Video: Streamlit Crash Course
- **YouTube Search:** `Streamlit crash course tutorial`
- Watch: 15-20 minutes
- Learn: Basic app structure, UI elements

### Video 2: Streamlit for ML
- **YouTube Search:** `Streamlit machine learning app example`

### Official Docs
Go to **streamlit.io/docs** — super well written

---

## DAY 2-3: Build Streamlit App

### Install:
```bash
pip install streamlit
```

### Code: Streamlit RAG App

Create file: `streamlit_app.py`

```python
import streamlit as st
import os
from pathlib import Path
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# =======================
# Streamlit Config
# =======================
st.set_page_config(
    page_title="AI Research Copilot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Research Copilot")
st.markdown("Ask questions about your research papers")

# =======================
# Sidebar: Settings
# =======================
with st.sidebar:
    st.header("⚙️ Settings")
    
    api_key = st.text_input("Gemini API Key", type="password")
    pdf_folder = st.text_input("PDF Folder Path", value="./papers")
    
    if st.button("🔄 Initialize System"):
        st.session_state.initialized = False
        st.success("Will reinitialize...")

# =======================
# Initialize on First Load
# =======================
if "initialized" not in st.session_state:
    st.session_state.initialized = False
    st.session_state.rag_chain = None

if not st.session_state.initialized and api_key:
    with st.spinner("Loading PDFs and building vector store..."):
        try:
            # Load documents
            loader = PyPDFDirectoryLoader(pdf_folder)
            documents = loader.load()
            
            if not documents:
                st.error("No PDFs found in the folder")
            else:
                # Build vector store
                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=500,
                    chunk_overlap=50
                )
                chunks = splitter.split_documents(documents)
                
                embeddings = GoogleGenerativeAIEmbeddings(
                    model="models/embedding-001",
                    google_api_key=api_key
                )
                
                vectorstore = Chroma.from_documents(
                    chunks,
                    embedding=embeddings,
                    collection_name="pdf_rag"
                )
                
                # Setup LLM
                llm = GoogleGenerativeAI(
                    model="gemini-1.5-flash",
                    google_api_key=api_key
                )
                
                # Setup chain
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "You are an expert at analyzing research papers. "
                               "Use the provided documents to answer questions."),
                    ("human", "{input}")
                ])
                
                retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
                qa_chain = create_stuff_documents_chain(llm, prompt)
                st.session_state.rag_chain = create_retrieval_chain(retriever, qa_chain)
                
                st.session_state.initialized = True
                st.success(f"✓ Loaded {len(documents)} pages from PDFs")
        except Exception as e:
            st.error(f"Error: {e}")

# =======================
# Main Chat Interface
# =======================
if st.session_state.initialized:
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input field
    query = st.chat_input("Ask a question about your papers...")
    
    if query:
        # Display user message
        with st.chat_message("user"):
            st.markdown(query)
        
        st.session_state.messages.append({"role": "user", "content": query})
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    result = st.session_state.rag_chain.invoke({"input": query})
                    answer = result['answer']
                    st.markdown(answer)
                    
                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer}
                    )
                except Exception as e:
                    st.error(f"Error: {e}")

else:
    st.info("👈 Enter your API key in the sidebar to get started")
```

### Run Locally:
```bash
streamlit run streamlit_app.py
```

You should see:
- Title and description
- Sidebar for API key
- Chat interface
- Ask questions and get answers!

### Commit
```bash
git add .
git commit -m "Week 4: Streamlit web app for RAG system"
git push origin main
```

---

## DAY 4-5: Deploy to Cloud

### Option 1: Streamlit Cloud (EASIEST)

1. Push code to GitHub
2. Go to **share.streamlit.io**
3. Sign in with GitHub
4. "New app" → select your repo
5. **Done!** App is live

### Option 2: Hugging Face Spaces

1. Go to **huggingface.co/spaces**
2. Create new space
3. Select Streamlit as SDK
4. Clone the repo and push your code
5. **Done!** App is live

### Option 3: Render

1. Go to **render.com**
2. Create new web service
3. Connect GitHub repo
4. Select Python/Streamlit
5. Deploy
6. **Done!**

### Create `.streamlit/config.toml`

```toml
[server]
headless = true
port = 8501

[client]
showErrorDetails = true
```

### Create `requirements.txt`

```
streamlit
langchain
langchain-community
langchain-google-genai
chromadb
pypdf
sentence-transformers
```

### Deployment Steps:

1. **Commit everything:**
   ```bash
   git add .
   git commit -m "Week 4: Deploy RAG to Streamlit Cloud"
   git push origin main
   ```

2. **Go to Streamlit Cloud:**
   - streamlit.io/cloud
   - Click "New app"
   - Select your GitHub repo
   - Enter: `streamlit_app.py`
   - Click "Deploy"

3. **Wait 2-3 minutes** for deployment

4. **Share your link!** (looks like: `app-abc123.streamlit.app`)

### Week 4 Completion Checklist
- [ ] Streamlit app works locally
- [ ] requirements.txt created
- [ ] Code pushed to GitHub
- [ ] App deployed to cloud
- [ ] Can access from any browser
- [ ] Chat works end-to-end
- [ ] **MILESTONE: You have a deployed product!**

---

# 🤖 WEEK 5: Learn Agents & Tool Calling

## Weekly Goal
Add autonomous decision-making. System decides which tool to use.

**Key Insight:** Agents are how modern AI systems work (ChatGPT, Claude, etc.)

---

## What's an Agent?
- **RAG:** Retrieves documents, generates answer
- **Agent:** Thinks about query, decides which tool to use, executes, reasons over result

### Example
User: "Compare my paper with recent ArXiv papers on the same topic"

**RAG approach:** Retrieve documents, generate answer
**Agent approach:** 
1. Think: "This needs searching"
2. Decide: "Use ArXiv search tool"
3. Execute: Search ArXiv
4. Reason: Compare results
5. Answer: Provide comparison

---

## DAY 1-2: Agent Fundamentals

### Video: LangChain Agents
- **YouTube Search:** `LangChain agents tutorial`
- Watch: 20-30 minutes
- Key concepts: Tools, ReAct pattern, agent loop

### Video 2: Functions and Tools
- **YouTube Search:** `DeepLearning.AI Functions Tools Agents LLMs`
- Official course (very good)
- Watch: Full short course (~1.5 hours)

### Read: LangChain Agent Docs
Go to **python.langchain.com/docs/concepts/agents**

---

## DAY 3: Build Tool 1 — PDF Search Tool

### What It Does
User asks: "What papers are about embeddings?"
Tool searches your PDFs and returns matching papers

### Code: PDF Search Tool

Create file: `13_pdf_search_tool.py`

```python
from typing import Annotated
from langchain_core.tools import tool
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Initialize vector store
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key="YOUR_GEMINI_API_KEY"
)

vectorstore = Chroma(
    collection_name="pdf_rag",
    embedding_function=embeddings
)

@tool
def search_papers(query: str) -> str:
    """
    Search through uploaded research papers.
    Use this when user asks about papers or their content.
    
    Args:
        query: What to search for
    
    Returns:
        Relevant paper excerpts
    """
    results = vectorstore.similarity_search(query, k=3)
    
    if not results:
        return "No papers found matching that query."
    
    response = "Found relevant papers:\n\n"
    for i, result in enumerate(results):
        response += f"{i+1}. {result.page_content[:300]}...\n\n"
    
    return response

# Test the tool
if __name__ == "__main__":
    print(search_papers("What is embeddings?"))
```

---

## DAY 4: Build Tool 2 — ArXiv Search Tool

### What It Does
User asks: "Find recent papers on agents"
Tool searches ArXiv (scientific paper database) and returns titles

### Install:
```bash
pip install arxiv
```

### Code: ArXiv Tool

Create file: `14_arxiv_tool.py`

```python
from typing import Annotated
from langchain_core.tools import tool
import arxiv

@tool
def search_arxiv(query: str) -> str:
    """
    Search ArXiv for recent research papers.
    Use this when user asks about latest papers or recent research.
    
    Args:
        query: What to search for on ArXiv
    
    Returns:
        List of papers with titles and summaries
    """
    try:
        client = arxiv.Client()
        search = arxiv.Search(
            query=query,
            max_results=3,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        
        papers = client.results(search)
        response = "Found recent papers on ArXiv:\n\n"
        
        for i, paper in enumerate(papers):
            response += f"{i+1}. {paper.title}\n"
            response += f"   Authors: {', '.join([a.name for a in paper.authors[:3]])}\n"
            response += f"   URL: {paper.entry_id}\n\n"
        
        return response
    except Exception as e:
        return f"Error searching ArXiv: {e}"

# Test
if __name__ == "__main__":
    print(search_arxiv("agentic AI"))
```

---

## DAY 5: Build Agent with Tools

### Code: Multi-Tool Agent

Create file: `15_agent_with_tools.py`

```python
from typing import Annotated
from langchain_core.tools import tool
from langchain_google_genai import GoogleGenerativeAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
import arxiv

# =======================
# Define Tools
# =======================

@tool
def search_arxiv(query: str) -> str:
    """Search ArXiv for recent papers"""
    try:
        client = arxiv.Client()
        search = arxiv.Search(query=query, max_results=3)
        papers = client.results(search)
        
        response = "Papers from ArXiv:\n"
        for i, paper in enumerate(papers):
            response += f"{i+1}. {paper.title}\n"
        return response
    except Exception as e:
        return f"Error: {e}"

@tool
def search_papers(query: str) -> str:
    """Search uploaded research papers"""
    # Connect to your vector store
    # [Same as before]
    return f"Found papers about {query}"

@tool
def calculator(expression: str) -> str:
    """Do math calculations"""
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Invalid math expression"

tools = [search_arxiv, search_papers, calculator]

# =======================
# Setup Agent
# =======================

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key="YOUR_GEMINI_API_KEY"
)

# Use ReAct prompt
prompt = hub.pull("hwchase17/react")

# Create agent
agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# =======================
# Test Agent
# =======================

if __name__ == "__main__":
    queries = [
        "Find papers on agentic AI from ArXiv",
        "Search my papers for embeddings",
        "What is 123 + 456?"
    ]
    
    for query in queries:
        print(f"\n{'='*50}")
        print(f"Query: {query}")
        print('='*50)
        result = executor.invoke({"input": query})
        print(f"Answer: {result['output']}")
```

### Run:
```bash
python 15_agent_with_tools.py
```

### What's Happening?
1. **Agent sees query:** "Find papers on agentic AI"
2. **Decides:** Use ArXiv search tool
3. **Executes:** Searches ArXiv
4. **Reasons:** Generates answer from results
5. **Returns:** List of papers

### Commit
```bash
git add .
git commit -m "Week 5: Agent system with multiple tools"
git push origin main
```

### Week 5 Completion Checklist
- [ ] Understand agent concept
- [ ] Built PDF search tool
- [ ] Built ArXiv search tool
- [ ] Built working agent with tools
- [ ] Agent can choose which tool to use
- [ ] Can test all tools independently

---

# 🔗 WEEK 6: Multi-Tool Agent System

## Weekly Goal
Integrate all tools into one cohesive agentic RAG system.

---

## DAY 1-2: Setup Multi-Tool Environment

### Code: Complete Agent RAG System

Create file: `16_complete_agent_rag.py`

```python
import os
from typing import Annotated
from langchain_core.tools import tool
from langchain_google_genai import GoogleGenerativeAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitter import RecursiveCharacterTextSplitter
import arxiv

# =======================
# Setup Vector Store
# =======================

def setup_vectorstore(api_key, pdf_folder="./papers"):
    """Load PDFs and create vector store"""
    loader = PyPDFDirectoryLoader(pdf_folder)
    documents = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)
    
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )
    
    vectorstore = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        collection_name="agent_rag"
    )
    
    return vectorstore

# =======================
# Define Tools
# =======================

vectorstore = None

@tool
def search_own_papers(query: str) -> str:
    """
    Search through YOUR uploaded research papers.
    Use when user asks about their own papers or documents.
    """
    if not vectorstore:
        return "Vector store not initialized"
    
    results = vectorstore.similarity_search(query, k=2)
    
    if not results:
        return "No matching papers found"
    
    response = "From your papers:\n"
    for i, result in enumerate(results):
        response += f"{i+1}. {result.page_content[:250]}...\n\n"
    
    return response

@tool
def search_arxiv_papers(query: str) -> str:
    """
    Search ArXiv for recent research papers.
    Use when user asks about latest research or recent papers.
    """
    try:
        client = arxiv.Client()
        search = arxiv.Search(
            query=query,
            max_results=3,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        
        papers = list(client.results(search))
        
        if not papers:
            return f"No papers found on ArXiv for '{query}'"
        
        response = f"Recent papers on ArXiv about {query}:\n\n"
        for i, paper in enumerate(papers):
            response += f"{i+1}. {paper.title}\n"
            response += f"   Authors: {', '.join([a.name for a in paper.authors[:2]])}\n"
            response += f"   Published: {paper.published.strftime('%Y-%m-%d')}\n"
            response += f"   Summary: {paper.summary[:200]}...\n\n"
        
        return response
    except Exception as e:
        return f"Error searching ArXiv: {e}"

@tool
def generate_comparison(topic: str) -> str:
    """
    Compare your papers with recent research on a topic.
    Use when user wants to compare their work with latest research.
    """
    own = search_own_papers(topic)
    arxiv = search_arxiv_papers(topic)
    
    comparison = f"Comparison for '{topic}':\n\n"
    comparison += f"YOUR PAPERS:\n{own}\n"
    comparison += f"RECENT RESEARCH:\n{arxiv}\n"
    
    return comparison

@tool
def summarize_topic(topic: str) -> str:
    """
    Summarize a topic based on your papers and recent research.
    """
    own_info = search_own_papers(topic)
    arxiv_info = search_arxiv_papers(topic)
    
    return f"Summary of {topic}:\n\nYour Research:\n{own_info}\n\nRecent Research:\n{arxiv_info}"

# =======================
# Setup Agent
# =======================

def create_agent(api_key, pdf_folder="./papers"):
    """Create and return agent executor"""
    global vectorstore
    
    # Setup vector store
    vectorstore = setup_vectorstore(api_key, pdf_folder)
    
    # Initialize LLM
    llm = GoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key
    )
    
    # Define tools
    tools = [
        search_own_papers,
        search_arxiv_papers,
        generate_comparison,
        summarize_topic
    ]
    
    # Create agent
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=5
    )
    
    return executor

# =======================
# Main
# =======================

if __name__ == "__main__":
    api_key = os.getenv("GEMINI_API_KEY") or input("Enter Gemini API key: ")
    
    print("Initializing agent...")
    agent = create_agent(api_key)
    
    print("\n" + "="*50)
    print("Multi-Tool Agent RAG Ready!")
    print("="*50 + "\n")
    
    test_queries = [
        "What's in my papers about embeddings?",
        "Find recent papers on embeddings from ArXiv",
        "Compare my papers with recent embeddings research",
        "Summarize what's known about RAG systems"
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        print("-" * 50)
        result = agent.invoke({"input": query})
        print(f"Answer: {result['output']}\n")
```

---

## DAY 3-4: Update Streamlit App with Agent

Create file: `streamlit_agent_app.py`

```python
import streamlit as st
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import tool
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitter import RecursiveCharacterTextSplitter
import arxiv

# =======================
# Streamlit Config
# =======================
st.set_page_config(
    page_title="AI Research Copilot - Agentic",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Research Copilot (Agentic)")
st.markdown("Ask questions. Agent decides which tools to use.")

# =======================
# Sidebar
# =======================
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Gemini API Key", type="password")
    pdf_folder = st.text_input("PDF Folder", value="./papers")
    
    st.markdown("---")
    st.markdown("### Tools Available")
    st.markdown("- 📄 Search Your Papers")
    st.markdown("- 🔬 Search ArXiv")
    st.markdown("- 📊 Compare Research")
    st.markdown("- 📝 Summarize Topics")

# =======================
# Initialize Agent
# =======================
@st.cache_resource
def setup_agent(api_key, pdf_folder):
    # Load documents
    loader = PyPDFDirectoryLoader(pdf_folder)
    documents = loader.load()
    
    if not documents:
        return None
    
    # Setup vector store
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)
    
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )
    
    vectorstore = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        collection_name="agent_rag"
    )
    
    # Define tools
    @tool
    def search_own_papers(query: str) -> str:
        """Search your papers"""
        results = vectorstore.similarity_search(query, k=2)
        if not results:
            return "No papers found"
        response = "From your papers:\n"
        for i, r in enumerate(results):
            response += f"{i+1}. {r.page_content[:200]}...\n"
        return response
    
    @tool
    def search_arxiv_papers(query: str) -> str:
        """Search ArXiv"""
        try:
            client = arxiv.Client()
            search = arxiv.Search(query=query, max_results=3)
            papers = list(client.results(search))
            response = "From ArXiv:\n"
            for i, p in enumerate(papers):
                response += f"{i+1}. {p.title}\n"
            return response
        except:
            return "ArXiv search failed"
    
    tools = [search_own_papers, search_arxiv_papers]
    
    # Create agent
    llm = GoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key
    )
    
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools, max_iterations=5)
    
    return executor

# =======================
# Main Interface
# =======================
if api_key and pdf_folder:
    if st.button("🔄 Initialize Agent"):
        setup_agent.clear()
    
    agent = setup_agent(api_key, pdf_folder)
    
    if agent:
        st.success("✓ Agent ready!")
        
        # Chat interface
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        query = st.chat_input("Ask about your research...")
        
        if query:
            with st.chat_message("user"):
                st.markdown(query)
            st.session_state.messages.append({"role": "user", "content": query})
            
            with st.chat_message("assistant"):
                with st.spinner("Agent thinking..."):
                    result = agent.invoke({"input": query})
                    answer = result['output']
                    st.markdown(answer)
            
            st.session_state.messages.append({"role": "assistant", "content": answer})
    else:
        st.error("No PDFs found or initialization failed")
else:
    st.info("👈 Set up API key and PDF folder in sidebar")
```

Run:
```bash
streamlit run streamlit_agent_app.py
```

---

## DAY 5: Deploy Agent Version

### Commit
```bash
git add .
git commit -m "Week 6: Complete multi-tool agentic RAG system"
git push origin main
```

### Update Streamlit Cloud
1. Push code to GitHub
2. Go to Streamlit Cloud
3. Click "Update" or let it auto-update
4. **Done!**

### Week 6 Completion Checklist
- [ ] Agent can use multiple tools
- [ ] Tools work independently
- [ ] Agent decides which tool to use
- [ ] Streamlit app integrated with agent
- [ ] App deployed to cloud
- [ ] Can ask complex queries (compare, summarize, search)

---

# 📊 WEEK 7: Evaluation, Polish & Shipping

## Weekly Goal
Make system production-ready and portfolio-perfect.

---

## DAY 1-2: Testing & Evaluation

### Concept: How Good Is Your System?

**Metrics to Track:**
- **Relevance:** Does retrieved document match query?
- **Accuracy:** Is the answer correct?
- **Tool Usage:** Which tools get used most?
- **Speed:** How fast are responses?

### Code: Basic Evaluation

Create file: `17_evaluation.py`

```python
import time
from datetime import datetime

class RAGEvaluator:
    def __init__(self):
        self.queries = []
        self.results = []
    
    def evaluate_query(self, query, agent_executor):
        """Test a query and track metrics"""
        start_time = time.time()
        
        result = agent_executor.invoke({"input": query})
        
        end_time = time.time()
        duration = end_time - start_time
        
        evaluation = {
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "answer": result['output'],
            "duration_seconds": duration,
            "success": True
        }
        
        self.results.append(evaluation)
        return evaluation
    
    def print_report(self):
        """Print evaluation report"""
        print("\n" + "="*50)
        print("EVALUATION REPORT")
        print("="*50)
        print(f"Total Queries: {len(self.results)}")
        
        if self.results:
            avg_time = sum(r['duration_seconds'] for r in self.results) / len(self.results)
            print(f"Average Response Time: {avg_time:.2f}s")
            
            print("\nQueries Tested:")
            for i, r in enumerate(self.results):
                print(f"{i+1}. {r['query']} ({r['duration_seconds']:.2f}s)")

# Test the evaluator
if __name__ == "__main__":
    evaluator = RAGEvaluator()
    
    test_queries = [
        "What is embeddings?",
        "Find papers on embeddings",
        "Compare my research with recent papers",
        "Summarize RAG systems"
    ]
    
    # Note: This would need actual agent_executor
    # evaluator.evaluate_query("test", agent_executor)
    # evaluator.print_report()
```

---

## DAY 3: Documentation

### Create Comprehensive README

Create file: `README.md`

```markdown
# 🤖 AI Research Copilot - Agentic RAG System

A production-ready agentic RAG system that helps researchers analyze papers and discover related work.

## Features

- **Multi-Tool Agent:** System autonomously decides which tool to use
- **PDF Search:** Query your uploaded research papers
- **ArXiv Integration:** Find recent papers on any topic
- **Research Comparison:** Compare your work with latest research
- **Topic Summarization:** Automatic summaries based on your papers + ArXiv

## Architecture

```
User Query
   ↓
Agent (decides tool)
   ├→ PDF Search Tool (your papers)
   ├→ ArXiv Search Tool (recent research)
   ├→ Comparison Tool
   └→ Summarization Tool
   ↓
Generate Answer
```

## Quick Start

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/ai-research-copilot.git
cd ai-research-copilot

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Setup

1. Get a free Gemini API key: https://ai.google.dev/aistudio
2. Create a `papers` folder and add your PDFs
3. Set environment variable:
   ```bash
   export GEMINI_API_KEY="your_key_here"
   ```

### Run

```bash
streamlit run streamlit_agent_app.py
```

Visit `http://localhost:8501`

## How It Works

1. **User Asks Question:** "Compare my paper with recent embeddings research"
2. **Agent Decides:** "I need to search papers + arxiv + compare"
3. **Executes Tools:** Runs search_own_papers, search_arxiv, generates comparison
4. **Returns Answer:** Shows relevant results and comparison

## Technologies

- **LangChain:** Agent framework
- **Gemini API:** LLM backbone
- **ChromaDB:** Vector database
- **Streamlit:** Web interface
- **ArXiv:** Paper search
- **PyPDF:** PDF processing

## Project Structure

```
ai-research-copilot/
├── streamlit_agent_app.py       # Main web app
├── 16_complete_agent_rag.py     # Agent system
├── requirements.txt              # Dependencies
├── papers/                        # Your PDF files
└── README.md
```

## Deployment

### Streamlit Cloud (Recommended)

1. Push to GitHub
2. Go to https://share.streamlit.io
3. Deploy from repo
4. **Done!**

### Hugging Face Spaces

1. Create space with Streamlit SDK
2. Push code
3. App auto-deploys

## Example Queries

- "What's in my papers about embeddings?"
- "Find recent papers on agentic AI from ArXiv"
- "Compare my embeddings work with latest research"
- "Summarize what's known about RAG systems"

## Evaluation

See `17_evaluation.py` for metrics tracking.

## Future Improvements

- [ ] Save conversation history
- [ ] Multi-turn conversation with context
- [ ] Citation formatting (BibTeX, APA)
- [ ] Topic clustering
- [ ] Fine-tuned on academic papers
- [ ] LangGraph for complex reasoning

## License

MIT

## Author

Your Name

## Feedback

Found a bug? Have an idea? Open an issue on GitHub!
```

---

## DAY 4: Create Demo & Video

### Write Demo Script

Create file: `DEMO.md`

```markdown
# Demo Script for AI Research Copilot

## Setup (1 min)
1. Open: https://your-app.streamlit.app
2. Enter Gemini API key
3. Point to papers folder

## Demo Queries (5 min)

### Query 1: Search Your Papers (1 min)
```
"What embeddings techniques are discussed in my papers?"
```
Expected: Agent uses PDF search tool, shows relevant excerpts

### Query 2: Find Recent Research (1 min)
```
"Find recent papers on embeddings from ArXiv"
```
Expected: Agent searches ArXiv, shows 3 recent papers with links

### Query 3: Compare Research (2 min)
```
"Compare my embeddings work with recent research"
```
Expected: Agent runs both tools, shows comparison

### Query 4: Summarize Topic (1 min)
```
"Summarize what's known about RAG systems"
```
Expected: Agent combines your papers + ArXiv, provides summary

## Key Points to Highlight
- Agent autonomously chooses tools
- No manual tool selection needed
- Combines multiple sources
- Production-ready code
- Deployed on cloud
```

### Record Demo Video
1. Open screen recorder (OBS, ScreenFlow, or built-in)
2. Walk through demo queries
3. Show ArXiv integration working
4. Highlight agent decision-making
5. Upload to YouTube (unlisted or public)

---

## DAY 5: Final Polish & Shipping

### Checklist Before Shipping

- [ ] All code on GitHub
- [ ] README is complete and clear
- [ ] requirements.txt has all dependencies
- [ ] App deployed and working on cloud
- [ ] Tested all tools and queries
- [ ] No API keys in code (use environment variables)
- [ ] Error handling for edge cases
- [ ] Response time acceptable (<5 sec)
- [ ] Clean code comments
- [ ] Demo video recorded

### Make Final Commit

```bash
git add .
git commit -m "Week 7: Complete agentic RAG system - production ready"
git push origin main
```

### Update Your Portfolio

Add to your portfolio/resume:

```
AI Research Copilot - Agentic RAG System
- Multi-tool agent that autonomously searches papers and recent research
- Technologies: LangChain, Gemini API, ChromaDB, Streamlit, ArXiv
- Features: PDF search, ArXiv integration, research comparison, summarization
- Deployed on Streamlit Cloud (link)
- GitHub: github.com/YOUR_USERNAME/ai-research-copilot
```

### Share Your Project

1. **GitHub:** Share your repo link
2. **LinkedIn:** Post about what you built and learned
3. **Portfolio:** Add to your website
4. **Interview:** "I built an agentic RAG system that..." (great story!)

---

# ✅ FINAL CHECKLIST: You've Built!

### Week 0
- [x] Python, VS Code, Git installed
- [x] GitHub repo created
- [x] Virtual environment working

### Week 1
- [x] LLM fundamentals understood
- [x] Gemini API chatbot working
- [x] Embeddings + vector similarity working
- [x] ChromaDB storing vectors
- [x] Mini RAG system (no LLM) working

### Week 2
- [x] PDF extraction working
- [x] Smart text chunking implemented
- [x] Full PDF RAG pipeline with LangChain
- [x] Multiple PDFs supported
- [x] **MILESTONE: V1 shipped on Streamlit Cloud**

### Week 3
- [x] Advanced chunking with metadata
- [x] Citations showing sources
- [x] Better error handling
- [x] Production-ready code structure

### Week 4
- [x] Streamlit web app created
- [x] Chat interface working
- [x] Deployed to cloud
- [x] **MILESTONE: Public app with working chat**

### Week 5
- [x] Agent concepts learned
- [x] PDF search tool working
- [x] ArXiv search tool working
- [x] Multi-tool agent system

### Week 6
- [x] Complete agent RAG system
- [x] All tools integrated
- [x] Streamlit app updated with agent
- [x] **MILESTONE: Agent system deployed**

### Week 7
- [x] Evaluation metrics tracked
- [x] Comprehensive README
- [x] Demo video recorded
- [x] Clean code + no API keys
- [x] **FINAL: Production-ready project shipped!**

---

# 🎓 What You've Learned

## Concepts
✅ LLMs and how they work
✅ Embeddings and vector similarity
✅ RAG (Retrieval Augmented Generation)
✅ Vector databases
✅ Agent architecture and ReAct pattern
✅ Tool calling and autonomous agents
✅ Prompt engineering
✅ LangChain framework
✅ Deployment and production systems

## Skills
✅ Python programming
✅ Working with APIs
✅ Building ML systems
✅ Debugging and testing
✅ Deploying to cloud
✅ Writing documentation
✅ System architecture

## Portfolio Impact
✅ One complete, deployed project
✅ Demonstrates full GenAI stack
✅ Shows understanding of trending concepts (RAG, agents)
✅ Clean, documented code on GitHub
✅ Production-ready implementation
✅ Impressive for placement interviews

---

# 💡 Next Steps After Week 7

### Short Term (Next 2 weeks)
1. Get feedback on your system
2. Add 1-2 more features (citations, exports, etc)
3. Write a blog post explaining RAG
4. Use in your actual research (dogfood it)

### Medium Term (Next Month)
1. Learn LangGraph for complex reasoning
2. Implement evaluation metrics (RAGAS)
3. Fine-tune for academic domain
4. Add more tools (Google Scholar, Semantic Scholar)

### Long Term (For Placements)
1. Reference this project in interviews
2. Show how you built it end-to-end
3. Discuss what you learned about agents
4. Talk about improvements you'd make

---

**🚀 You're ready. Start with Week 0 Setup today.**

**Good luck! 🎓**

---

## Quick Reference: YouTube Searches

```
Week 0: "Git and GitHub Crash Course Traversy Media"
Week 1: "Intro to Large Language Models Andrej Karpathy"
Week 1: "Embeddings StatQuest"
Week 1: "Tokens in Large Language Models StatQuest"
Week 2: "LangChain Tutorial for Beginners"
Week 2: "Extract text from PDF Python pypdf"
Week 2: "Text chunking for RAG explained"
Week 3: "Semantic chunking for RAG"
Week 4: "Streamlit crash course tutorial"
Week 5: "LangChain agents tutorial"
Week 5: "DeepLearning.AI Functions Tools Agents LLMs"
Week 6: "ReAct agent pattern explained"
Week 7: "LangSmith for LLM monitoring"

All should be 10-30 minutes, practical focused.
```

---

**Document Version:** 1.0
**Last Updated:** 2024
**Status:** Ready to execute
