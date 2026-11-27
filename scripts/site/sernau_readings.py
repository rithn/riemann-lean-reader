"""Shared reading prose for the static pages, Markdown copies and Lean reader."""

from markdown_it import MarkdownIt


MARKDOWN = MarkdownIt("commonmark", {"html": False})


def reading_markdown(record, edition, *, preview=False):
    if record["origin"] == "explorer-draft":
        label = {
            "passed": "Written by AI, checked against the code",
            "pending": "Draft, under review" if preview else None,
        }.get(record["review"])
        if label:
            sentences = []
            for claim in record["draft"]:
                sources = []
                for cite in claim["citations"]:
                    module = cite["module"].removeprefix(record["group"] + ".")
                    start, end = cite["line"], cite["endLine"]
                    lines = str(start) if start == end else f"{start}–{end}"
                    sources.append(f'[{module} {lines}]({cite["github"]})')
                sentences.append(f'{claim["sentence"]} ({" · ".join(sources)})')
            return f'**{label}**\n\n{" ".join(sentences)}'

    excerpt = record.get("excerpt")
    if not excerpt:
        return ""
    upstream = excerpt["text"].strip()
    # Declaration docstrings can include the Lean delimiters in the pinned range.
    upstream = upstream.removeprefix("/--").removesuffix("-/").strip()
    quote = "\n".join(f"> {line}" if line else ">" for line in upstream.splitlines())
    docs = {doc["id"]: doc["href"] for doc in edition["documents"]}
    result = (
        f'[Upstream documentation written by Claude]({excerpt["github"]})\n\n'
        f'{quote}\n\n'
        f'Copyright 2026 Anthropic, PBC. [Apache License 2.0]({docs["license"]}) · '
        f'[Upstream notice]({docs["notice"]}).'
    )

    remainder = record.get("remainder")
    if remainder:
        text = remainder["text"].strip()
        if text:
            # Render the source as Markdown inside a disclosure, with HTML disabled.
            result += f'\n\n[Rest of upstream introduction]({remainder["github"]})'
    return result
