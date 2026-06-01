

from shared.schemas import RetrievedChunk

class ContextBuilder:

    def build(
        self,
        chunks: list[RetrievedChunk]
    ) -> str:

        sections = []

        for i, chunk in enumerate(chunks, start=1):
            sections.append(
                f"[Document {i}]\n{chunk.chunk.text}"
            )

        return "\n\n".join(sections)
