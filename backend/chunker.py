import re
from config import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_markdown(text: str, source: str) -> list[dict]:
    # Split on markdown headers first, then by size
    sections = re.split(r"(?=^#{1,3} )", text, flags=re.MULTILINE)
    chunks = []

    for section in sections:
        section = section.strip()
        if not section:
            continue
        if len(section) <= CHUNK_SIZE:
            chunks.append({"text": section, "source": source})
        else:
            start = 0
            while start < len(section):
                end = min(start + CHUNK_SIZE, len(section))
                chunk = section[start:end].strip()
                if chunk:
                    chunks.append({"text": chunk, "source": source})
                if end >= len(section):
                    break
                start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks
