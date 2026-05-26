# 2026/05/26 - Separate Active / Passive / Shared architecture

## Conclusion

- The system is organized into four top-level layers:
  - `active/` (user-driven execution)
  - `passive/` (background or batch processing)
  - `shared/` (common infrastructure and data models)
  - `main.py` (entry point / orchestrator)
- Each layer has a clear responsibility and does not depend on internal implementation details of other layers.
- Communication between layers is done through shared interfaces and shared resources (VectorDB, schemas, config).

## Reason

- RAG systems naturally require separation between offline processing (ingestion) and online processing (querying).
- Mixing ingestion and query logic increases latency and makes scaling difficult.
- Clear execution-context separation improves maintainability and future extensibility.
- Shared infrastructure (LLM, vector store, schemas) must be reused by both active and passive layers.

## Details

### 1. active/ (User-driven execution layer)

Responsible for real-time or interactive operations triggered by user input.

Includes:

- `query/`
  - `retriever.py`: Vector search logic
  - `prompt_builder.py`: Prompt construction using retrieved context
  - `generator.py`: LLM response generation
  - `pipeline.py`: Orchestration of the query flow

- `chat/`
  - `history.py`: Conversation state management

This layer must not perform heavy ingestion or data preprocessing.

---

### 2. passive/ (Background processing layer)

Responsible for offline or batch processing tasks.

Includes:

- `ingest/`
  - `pdf/`
    - `_types.py`: Internal types used only inside ingestion pipeline
    - `base.py`: Base classes for loaders/chunkers
    - `loader.py`: PDF loading
    - `chunker.py`: Text segmentation into chunks
    - `factory.py`: Loader/chunker selection logic
  - `embedding/`
    - `embedder.py`: Embedding generation logic

This layer is responsible for building and updating the knowledge base stored in the vector database.

---

### 3. shared/ (Common infrastructure layer)

Responsible for shared components used by both active and passive layers.

Includes:

- `config.py`: Global configuration
- `schemas.py`: Shared data models (e.g., Document, Chunk, QueryResult)
- `llm/`
  - `client.py`: LLM interface abstraction
- `vectorstore/`
  - `chroma_store.py`: Vector database access layer
- `utils/`
  - `logger.py`: Logging utilities

This layer must not contain business logic specific to ingestion or query flows.

---

### 4. data/ (Runtime storage layer)

Stores persistent or generated artifacts:

- `chroma/`: Vector database storage
- `pdf/`: Raw input documents
- `sqlite/`: Optional structured storage (e.g., chat history or metadata)

---

### 5. main.py (Entry point)

Acts as the system orchestrator.

Typical responsibilities:

- Decide whether ingestion should run (initial setup or update)
- Trigger active query pipeline
- Coordinate system startup flow

---

## Architecture principle

- Separation is based on **execution context**, not functionality.
  - `active` = runtime/user interaction path
  - `passive` = offline/background processing path
- All cross-layer communication goes through `shared/` or `data/`.
- Direct dependency between `active` and `passive` is forbidden.

---

## Dependency rule

Allowed dependency direction:

- `active → shared`
- `passive → shared`
- `shared → data (read/write via controlled interfaces)`
- `main.py → all layers`

Forbidden:

- `active → passive`
- `passive → active`
- `shared → active/passive`

---

## Design intent

This architecture is designed to:

- Separate latency-sensitive and heavy computation workloads
- Enable future scaling of ingestion as a standalone pipeline
- Keep query path minimal and fast
- Allow vector store and LLM backend to be replaced independently
